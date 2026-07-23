#!/usr/bin/env python3
"""从 references/ 与 assets/avatars/ 生成 web/data.js 与 web/avatars64.js。

data.js：题库 + 16 型文案；avatars64.js：16 张头像的 base64（供 Canvas 出图，
避免 file:// 协议下的画布污染）。改动 references/ 或头像后请重新生成。

用法：python3 scripts/build_web_data.py
"""
import base64
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TAGS = {
    "INTJ": ["计划通", "大脑开十六个窗口", "人间Ctrl+S", "独处充电中", "先赢再说"],
    "INTP": ["逻辑怪", "脑子转不停", "DDL是第一生产力", "冷笑话十级", "社恐但讲理"],
    "ENTJ": ["天生的组长", "效率狂魔", "目标刻进DNA", "人狠话不多", "卷王本王"],
    "ENTP": ["杠精本精", "点子批发商", "三分钟热度冠军", "辩论气氛组", "脑洞不限号"],
    "INFJ": ["人间读心术", "安静的犟种", "共情力拉满", "内耗十级学者", "理想主义钉子户"],
    "INFP": ["小蝴蝶本蝶", "脑内剧场24h", "温柔但有刺", "眼泪批发价", "浪漫与emo齐飞"],
    "ENFJ": ["行走的太阳", "夸夸群群主", "操心的命", "氛围制造机", "先别人后自己"],
    "ENFP": ["快乐小狗本狗", "人间充电宝", "新鲜感收割机", "热情三分钟", "社交恐怖分子"],
    "ISTJ": ["靠谱本谱", "人间闹钟", "规则守门员", "计划表成精", "稳稳的幸福"],
    "ISFJ": ["小护士本护", "细节扫描仪", "有求必应奖", "记性好到可怕", "安静发光体"],
    "ESTJ": ["尺子姐本姐", "Deadline执法者", "效率纠察队", "安排！", "说一不二"],
    "ESFJ": ["男妈妈本妈", "群聊润滑剂", "记得你的生日", "热情永动机", "团建发起人"],
    "ISTP": ["电钻哥本哥", "人狠话不多", "动手派掌门", "冷静维修站", "独来独往"],
    "ISFP": ["小画家本家", "氛围感捕手", "慢热但细腻", "审美在线", "活在当下"],
    "ESTP": ["墨镜哥本哥", "行动派闪电", "刺激探测器", "冲就完了", "现挂之王"],
    "ESFP": ["锤子姐本姐", "快乐放大器", "舞台中心区", "及时行乐代言人", "气氛组组长"],
}

FIELD_MAP = {
    "一句话": "one",
    "画像": "portrait",
    "优势": "strengths",
    "容易踩的坑": "pitfalls",
    "社交": "social",
    "决策": "decision",
    "压力": "stress",
    "观察建议": "advice",
    "社区俗称": "meme",
}


def parse_profiles() -> dict:
    text = (ROOT / "references" / "type-profiles.md").read_text(encoding="utf-8")
    profiles = {}
    for m in re.finditer(r"^## ([EISNTFJP]{4}) · ([^\n]+)\n(.*?)(?=^## |\Z)", text, re.M | re.S):
        code, nick, block = m.group(1), m.group(2).strip(), m.group(3)
        entry = {"nick": nick, "tags": TAGS[code]}
        for label, value in re.findall(r"\*\*(\S+?)：\*\*\s*(.+)", block):
            key = FIELD_MAP.get(label)
            if key:
                entry[key] = value.strip()
        missing = set(FIELD_MAP.values()) - set(entry)
        if missing:
            raise SystemExit(f"{code} 缺少字段：{sorted(missing)}")
        profiles[code] = entry
    if len(profiles) != 16:
        raise SystemExit(f"应解析出 16 个类型，实际 {len(profiles)}")
    return profiles


def main() -> None:
    bank = json.loads((ROOT / "references" / "questions.json").read_text(encoding="utf-8"))
    data = {
        "version": bank["version"],
        "source": bank["source"],
        "items": bank["items"],
        "profiles": parse_profiles(),
    }
    out = ROOT / "web" / "data.js"
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(data, ensure_ascii=False, indent=1)
    out.write_text(
        "// 本文件由 scripts/build_web_data.py 生成，请勿手改。改动 references/ 后请重新生成。\n"
        f"window.OJTS_DATA = {payload};\n",
        encoding="utf-8",
    )
    print(f"written {out} ({out.stat().st_size} bytes)")

    avatars = {}
    for img in sorted((ROOT / "assets" / "avatars").glob("*.webp")):
        b64 = base64.b64encode(img.read_bytes()).decode("ascii")
        avatars[img.stem.upper()] = f"data:image/webp;base64,{b64}"
    if len(avatars) != 16:
        raise SystemExit(f"应有 16 张头像，实际 {len(avatars)} 张，请先运行 slice_avatars.py")
    qr_path = ROOT / "assets" / "qr-web.png"
    qr64 = ""
    if qr_path.is_file():
        qr_b64 = base64.b64encode(qr_path.read_bytes()).decode("ascii")
        qr64 = f'\nwindow.OJTS_QR = "data:image/png;base64,{qr_b64}";\n'
    out64 = ROOT / "web" / "avatars64.js"
    out64.write_text(
        "// 本文件由 scripts/build_web_data.py 生成，请勿手改。头像变更后请重新生成。\n"
        f"window.OJTS_AVATARS = {json.dumps(avatars)};\n" + qr64,
        encoding="utf-8",
    )
    print(f"written {out64} ({out64.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
