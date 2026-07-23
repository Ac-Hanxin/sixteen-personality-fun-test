#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


LETTERS = "EISNTFJP"
AXES = (("E", "I"), ("S", "N"), ("T", "F"), ("J", "P"))


def load_bank(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("version") != "OJTS 2.1" or len(data.get("items", [])) != 48:
        raise ValueError("题库版本或题目数量不正确")
    return data


def parse_answers(raw: str) -> list[int]:
    parts = [part for part in re.split(r"[\s,，;；]+", raw.strip()) if part]
    if len(parts) != 48:
        raise ValueError(f"需要 48 个答案，实际收到 {len(parts)} 个")
    try:
        answers = [int(part) for part in parts]
    except ValueError as exc:
        raise ValueError("答案必须是 1 到 5 的整数") from exc
    if any(answer < 1 or answer > 5 for answer in answers):
        raise ValueError("答案必须是 1 到 5 的整数")
    return answers


def score_answers(bank: dict, answers: list[int]) -> dict[str, int]:
    if len(answers) != 48:
        raise ValueError("需要 48 个答案")
    scores = {letter: 0 for letter in LETTERS}
    # Both lengths are validated above; plain zip keeps compatibility with Python 3.9.
    for item, answer in zip(bank["items"], answers):
        if not isinstance(answer, int) or answer < 1 or answer > 5:
            raise ValueError(f"{item['id']} 的答案必须是 1 到 5 的整数")
        if item["kind"] == "likert":
            for key in item["keys"]:
                scores[key] += answer - 1
        elif item["kind"] == "bipolar":
            scores[item["left_key"]] += 5 - answer
            scores[item["right_key"]] += answer - 1
        else:
            raise ValueError(f"未知题型：{item['kind']}")
    return scores


def summarize_scores(scores: dict[str, int]) -> dict:
    raw_letters = []
    axes = []
    boundary_axes = []
    for left, right in AXES:
        left_score, right_score = scores[left], scores[right]
        total = left_score + right_score
        if left_score == right_score:
            chosen = "X"
            boundary_axes.append(f"{left}/{right}")
        else:
            chosen = left if left_score > right_score else right
        raw_letters.append(chosen)
        axes.append({
            "axis": f"{left}/{right}",
            "left": left_score,
            "right": right_score,
            "left_ratio": round(left_score / total, 4),
            "right_ratio": round(right_score / total, 4),
            "difference": abs(left_score - right_score),
            "chosen": chosen,
        })
    raw_type = "".join(raw_letters)
    candidates = [""]
    for position, (left, right) in enumerate(AXES):
        if raw_letters[position] == "X":
            candidates = [prefix + letter for prefix in candidates for letter in (left, right)]
        else:
            candidates = [prefix + raw_letters[position] for prefix in candidates]
    non_boundary = [axis for axis in axes if axis["chosen"] != "X"]
    second_candidates = []
    if not boundary_axes and non_boundary:
        weakest = min(axis["difference"] for axis in non_boundary)
        for axis in non_boundary:
            if axis["difference"] == weakest:
                left, right = axis["axis"].split("/")
                flip = right if axis["chosen"] == left else left
                pos = [pair for pair in ("E/I", "S/N", "T/F", "J/P")].index(axis["axis"])
                second_candidates.append(raw_type[:pos] + flip + raw_type[pos + 1:])
    return {
        "scores": scores,
        "axes": axes,
        "raw_type": raw_type,
        "boundary_axes": boundary_axes,
        "candidates": candidates,
        "second_candidates": sorted(set(second_candidates)),
    }


def answers_targeting_pole(bank: dict, pole: str) -> list[int]:
    answers = []
    for item in bank["items"]:
        if item["kind"] == "likert":
            answers.append(5 if pole in item["keys"] else 1)
        elif item["left_key"] == pole:
            answers.append(1)
        elif item["right_key"] == pole:
            answers.append(5)
        else:
            answers.append(3)
    return answers


def answers_targeting_type(bank: dict, type_code: str) -> list[int]:
    wanted = set(type_code)
    answers = []
    for item in bank["items"]:
        if item["kind"] == "likert":
            answers.append(5 if set(item["keys"]) <= wanted else 1)
        elif item["left_key"] in wanted:
            answers.append(1)
        elif item["right_key"] in wanted:
            answers.append(5)
        else:
            answers.append(3)
    return answers


def main() -> int:
    parser = argparse.ArgumentParser(description="Score OJTS 2.1 answers locally")
    parser.add_argument("--answers", required=True, help="48 integers separated by spaces or commas")
    parser.add_argument(
        "--bank",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "references" / "questions.json",
    )
    args = parser.parse_args()
    result = summarize_scores(score_answers(load_bank(args.bank), parse_answers(args.answers)))
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    import sys

    try:
        raise SystemExit(main())
    except ValueError as exc:
        print(f"错误：{exc}", file=sys.stderr)
        raise SystemExit(1)
