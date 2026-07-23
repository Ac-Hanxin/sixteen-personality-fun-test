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
        entry = {"nick": nick}
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
    out64 = ROOT / "web" / "avatars64.js"
    out64.write_text(
        "// 本文件由 scripts/build_web_data.py 生成，请勿手改。头像变更后请重新生成。\n"
        f"window.OJTS_AVATARS = {json.dumps(avatars)};\n",
        encoding="utf-8",
    )
    print(f"written {out64} ({out64.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
