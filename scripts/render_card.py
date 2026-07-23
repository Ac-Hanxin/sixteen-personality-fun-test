#!/usr/bin/env python3
"""渲染 16 型人格趣味测试的「分析结果长图」PNG。

用法：
  python3 scripts/render_card.py --answers "<48 个 1-5 整数>" [--out result.png]

需要 Pillow（pip3 install Pillow）。平分时按固定顺序取 candidates 首个，
同一组答案永远得到同一张图。
"""
import argparse
import importlib.util
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("score", ROOT / "scripts" / "score.py")
score = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(score)

FIELD_MAP = {
    "一句话": "one", "画像": "portrait", "优势": "strengths", "容易踩的坑": "pitfalls",
    "社交": "social", "决策": "decision", "压力": "stress", "观察建议": "advice", "社区俗称": "meme",
}
SECTIONS = [
    ("画像", "portrait"), ("优势", "strengths"), ("容易踩的坑", "pitfalls"),
    ("社交", "social"), ("决策", "decision"), ("压力", "stress"), ("观察建议", "advice"),
]
CJK_FONTS = [
    "/System/Library/Fonts/PingFang.ttc",                    # macOS
    "/System/Library/Fonts/STHeiti Medium.ttc",              # macOS 备选
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",  # Linux (Noto)
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",          # Linux (文泉驿)
    "C:/Windows/Fonts/msyh.ttc",                             # Windows 微软雅黑
    "C:/Windows/Fonts/simhei.ttf",                           # Windows 黑体
]


def load_font(size: int):
    from PIL import ImageFont

    for path in CJK_FONTS:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    raise SystemExit("未找到中文字体，请安装 Noto Sans CJK 或微软雅黑后重试。")


def load_profile(code: str) -> dict:
    text = (ROOT / "references" / "type-profiles.md").read_text(encoding="utf-8")
    m = re.search(rf"^## {code} · ([^\n]+)\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        raise SystemExit(f"references/type-profiles.md 中找不到类型 {code}")
    entry = {"nick": m.group(1).strip()}
    for label, value in re.findall(r"\*\*(\S+?)：\*\*\s*(.+)", m.group(2)):
        if label in FIELD_MAP:
            entry[FIELD_MAP[label]] = value.strip()
    return entry


def wrap(draw, text, font, max_width):
    lines, line = [], ""
    for ch in text:
        if draw.textlength(line + ch, font=font) > max_width and line:
            space = line.rfind(" ")
            if space > 0 and ch.isascii() and not ch.isspace():
                lines.append(line[:space])
                line = line[space + 1:] + ch
            else:
                lines.append(line)
                line = ch
        else:
            line += ch
    if line:
        lines.append(line)
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description="渲染分析结果长图 PNG")
    parser.add_argument("--answers", required=True, help="48 个 1-5 的整数，空格或逗号分隔")
    parser.add_argument("--out", type=Path, default=None, help="输出 PNG 路径")
    args = parser.parse_args()

    try:
        from PIL import Image, ImageDraw
    except ImportError:
        raise SystemExit("缺少 Pillow，请先运行：pip3 install Pillow")

    bank = score.load_bank(ROOT / "references" / "questions.json")
    try:
        answers = score.parse_answers(args.answers)
    except ValueError as exc:
        raise SystemExit(f"错误：{exc}")
    result = score.summarize_scores(score.score_answers(bank, answers))
    chosen = result["candidates"][0]  # 固定规则：平分也确定，不可手动调换
    profile = load_profile(chosen)
    today = date.today().isoformat()
    out = args.out or Path(f"result-card-{chosen}-{today}.png")

    W, PAD = 1080, 56
    CW = W - PAD * 2
    fonts = {
        "title": load_font(30), "small": load_font(24), "type": load_font(72),
        "nick": load_font(36), "body": load_font(27), "h3": load_font(31),
        "note": load_font(23), "footer": load_font(22),
    }
    avatar = Image.open(ROOT / "assets" / "avatars" / f"{chosen.lower()}.webp").convert("RGB")
    avatar_h = round(240 * avatar.height / avatar.width)
    avatar = avatar.resize((240, avatar_h), Image.LANCZOS)

    probe = ImageDraw.Draw(Image.new("RGB", (W, 10)))

    def layout(draw, measure, canvas_img=None):
        y = 44

        def text(s, x, font, color, align="left"):
            if not measure:
                draw.text((x, y), s, font=font, fill=color, anchor={"left": "la", "center": "ma"}[align])

        def wrapped(s, font, color, line_h, align="left"):
            nonlocal y
            for ln in wrap(draw, s, font, CW):
                y += line_h
                text(ln, W / 2 if align == "center" else PAD, font, color, align)

        def divider():
            nonlocal y
            y += 22
            if not measure:
                draw.line([(PAD, y), (W - PAD, y)], fill="#E3E7EE", width=2)
            y += 22

        text("16 型人格趣味测试 · 分析报告", PAD, fonts["title"], "#56627A")
        y += 48
        text(f"{today} · 基于 OJTS 2.1 · 仅供娱乐", PAD, fonts["small"], "#8A93A6")
        y += 28
        if not measure:
            canvas_img.paste(avatar, ((W - 240) // 2, y))
        y += avatar_h + 40
        text("根据测试结果，您是", W / 2, fonts["body"], "#56627A", "center")
        y += 108
        text(f"{chosen}（{profile['meme']}）", W / 2, fonts["type"], "#243B78", "center")
        y += 80
        text(profile["nick"], W / 2, fonts["nick"], "#172033", "center")
        y += 56
        wrapped(profile["one"], fonts["body"], "#56627A", 40, "center")
        divider()

        for label, key in SECTIONS:
            y += 24 + 34
            text(label, PAD, fonts["h3"], "#243B78")
            y += 8
            wrapped(profile[key], fonts["body"], "#394760", 44)

        second_list, second_note = [], None
        if result["second_candidates"]:
            weakest = min(a["difference"] for a in result["axes"])
            axes_str = "、".join(a["axis"] for a in result["axes"] if a["difference"] == weakest)
            others = result["second_candidates"][1:]
            extra = f"（另有 {len(others)} 个同样接近的类型：{'、'.join(others)}）" if others else ""
            second_list = [result["second_candidates"][0]]
            second_note = f"你在 {axes_str} 维度分差最小（{weakest} 分），这个类型的偏好也可能在不同情境出现{extra}："
        elif result["boundary_axes"] and len(result["candidates"]) > 1:
            extra = f"（共 {len(result['candidates'])} 个候选，其余不再展开）" if len(result["candidates"]) > 2 else ""
            second_list = [result["candidates"][1]]
            second_note = f"原始类型含平分维度（{result['raw_type']}），主结果为固定顺序首个候选；此候选与你的答案同样接近{extra}："
        if second_note:
            y += 10 + 34
            text("第二候选人格", PAD, fonts["h3"], "#243B78")
            y += 8
            wrapped(second_note, fonts["small"], "#56627A", 34)
            for t in second_list:
                sp = load_profile(t)
                sav = Image.open(ROOT / "assets" / "avatars" / f"{t.lower()}.webp").convert("RGB")
                sah = round(96 * sav.height / sav.width)
                sav = sav.resize((96, sah), Image.LANCZOS)
                y += 18
                top = y
                if not measure:
                    canvas_img.paste(sav, (PAD, top))
                tx = PAD + 116
                if not measure:
                    draw.text((tx, top + 8), f"{t} · {sp['nick']}（{sp['meme']}）",
                              font=fonts["body"], fill="#172033", anchor="la")
                lines = wrap(draw, sp["one"], fonts["small"], CW - 116)
                for i, ln in enumerate(lines):
                    if not measure:
                        draw.text((tx, top + 42 + i * 32), ln,
                                  font=fonts["small"], fill="#56627A", anchor="la")
                text_h = 42 + (len(lines) - 1) * 32 + 28
                y = top + max(sah, text_h) + 6
        divider()

        y += 6
        text("八极分数", PAD, fonts["h3"], "#243B78")
        y += 14
        for a in result["axes"]:
            left, right = a["axis"].split("/")
            y += 40
            text(f"{left} {a['left']} / {right} {a['right']}", PAD, fonts["body"], "#172033")
            y += 40
            bw1 = round(CW * a["left_ratio"])
            if not measure:
                draw.rectangle([PAD, y, PAD + bw1, y + 22], fill="#A2AFC7")
                draw.rectangle([PAD + bw1, y, PAD + CW, y + 22], fill="#5069AC")
            y += 22 + 24
            note = "完全平分（X）" if a["chosen"] == "X" else f"偏向 {a['chosen']} · 分差 {a['difference']}"
            text(f"{round(a['left_ratio']*100)}% : {round(a['right_ratio']*100)}% · {note}",
                 PAD, fonts["note"], "#56627A")
            y += 34
        if result["second_candidates"]:
            y += 6
            wrapped("最接近的第二候选：" + "、".join(result["second_candidates"]), fonts["small"], "#56627A", 34)
        if result["boundary_axes"]:
            y += 6
            wrapped(
                f"完全平分维度：{'、'.join(result['boundary_axes'])}（原始类型 {result['raw_type']}，按固定规则展示首个候选 {chosen}）",
                fonts["small"], "#56627A", 34,
            )
        divider()
        wrapped(
            "改编自 Eric Jorgenson 的 OJTS 2.1（CC BY-NC-SA 4.0）· 与 16Personalities、The Myers-Briggs Company 均无关联 · 非诊断、非临床",
            fonts["footer"], "#8A93A6", 32, "center",
        )
        y += 40
        return y

    height = layout(probe, True)
    img = Image.new("RGB", (W, height), "#FFFFFF")
    layout(ImageDraw.Draw(img), False, img)
    img.save(out, "PNG")
    print(f"已生成长图：{out}（{W}x{height}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
