import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILES = ROOT / "references" / "type-profiles.md"
EXPECTED = {
    "INTJ": "系统蓝图师", "INTP": "原理拆解者", "ENTJ": "目标统筹者", "ENTP": "可能性试验家",
    "INFJ": "深层洞察者", "INFP": "内心故事家", "ENFJ": "共鸣引导者", "ENFP": "灵感点火者",
    "ISTJ": "稳序守护者", "ISFJ": "细节照料者", "ESTJ": "秩序推进者", "ESFJ": "氛围联结者",
    "ISTP": "冷静解题者", "ISFP": "感受收藏家", "ESTP": "现场破局者", "ESFP": "快乐放大者",
}
BANNED = ("官方 MBTI", "百分之百准确", "心理学界最准", "建筑师", "调停者", "竞选者")


class ProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = PROFILES.read_text(encoding="utf-8")

    def test_has_exactly_sixteen_unique_type_headings(self):
        headings = re.findall(r"^## ([EISNTFJP]{4}) · (.+)$", self.text, re.MULTILINE)
        self.assertEqual(dict(headings), EXPECTED)

    def test_each_profile_has_required_sections(self):
        for type_code in EXPECTED:
            start = self.text.index(f"## {type_code} ·")
            next_start = self.text.find("\n## ", start + 1)
            block = self.text[start: next_start if next_start != -1 else None]
            for label in ("社区俗称", "一句话", "画像", "优势", "容易踩的坑", "社交", "决策", "压力", "观察建议"):
                self.assertIn(f"**{label}：**", block)

    def test_avoids_banned_or_borrowed_claims(self):
        for phrase in BANNED:
            self.assertNotIn(phrase, self.text)


if __name__ == "__main__":
    unittest.main()
