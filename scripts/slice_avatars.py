#!/usr/bin/env python3
"""把 4×4 角色群像切成 16 张单人头像（WebP）。

自动检测格子间的浅色分隔带，按内容区域精确切割，避免相邻格子串图。

用法：python3 scripts/slice_avatars.py <群像图片路径>
输出：assets/avatars/<type>.webp（如 intp.webp），文件名全小写。
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "avatars"

# 群像中的类型排布（与图一致：NT、NF、SJ、SP 四行）
ROWS = [
    ["INTJ", "INTP", "ENTJ", "ENTP"],
    ["INFJ", "INFP", "ENFJ", "ENFP"],
    ["ISTJ", "ISFJ", "ESTJ", "ESFJ"],
    ["ISTP", "ISFP", "ESTP", "ESFP"],
]


def content_spans(ratio, threshold=0.6):
    """根据浅色分隔带比例，返回 4 段内容区间 [(start, end), ...]。"""
    idx = np.where(ratio > threshold)[0]
    gutters = []
    if len(idx):
        s = p = int(idx[0])
        for i in idx[1:]:
            i = int(i)
            if i > p + 1:
                gutters.append((s, p))
                s = i
            p = i
        gutters.append((s, p))
    if len(gutters) != 5:
        raise SystemExit(f"应检测到 5 条分隔带，实际 {len(gutters)} 条：{gutters}")
    spans = []
    for a, b in zip(gutters, gutters[1:]):
        spans.append((a[1] + 1, b[0] - 1))
    return spans


def main(src: str) -> None:
    im = Image.open(src).convert("RGB")
    arr = np.asarray(im).astype(int)
    white = (arr > 235).all(axis=2)
    xs = content_spans(white.mean(axis=0))
    ys = content_spans(white.mean(axis=1))
    OUT.mkdir(parents=True, exist_ok=True)
    for r, row in enumerate(ROWS):
        for c, code in enumerate(row):
            x0, x1 = xs[c]
            y0, y1 = ys[r]
            cell = im.crop((x0, y0, x1 + 1, y1 + 1))
            path = OUT / f"{code.lower()}.webp"
            cell.save(path, "WEBP", quality=85, method=6)
            print(f"{code} -> {path.name} {cell.size[0]}x{cell.size[1]} {path.stat().st_size // 1024}KB")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    main(sys.argv[1])
