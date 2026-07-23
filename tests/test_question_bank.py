import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "references" / "questions.json"
LETTERS = set("EISNTFJP")


class QuestionBankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(BANK.read_text(encoding="utf-8"))
        cls.items = cls.data["items"]

    def test_metadata_is_traceable(self):
        self.assertEqual(self.data["version"], "OJTS 2.1")
        self.assertEqual(self.data["license"], "CC BY-NC-SA 4.0")
        self.assertIn("openpsychometrics.org/tests/OJTS", self.data["source"])
        self.assertIn("中文翻译", self.data["translation_notice"])

    def test_contains_exactly_48_unique_items(self):
        self.assertEqual(len(self.items), 48)
        self.assertEqual(len({item["id"] for item in self.items}), 48)
        self.assertEqual([item["id"] for item in self.items[:40]], [f"Q{i}" for i in range(1, 41)])
        self.assertEqual([item["id"] for item in self.items[40:]], [f"S{i}" for i in range(1, 9)])

    def test_likert_items_have_bilingual_text_and_valid_keys(self):
        for item in self.items[:40]:
            self.assertEqual(item["kind"], "likert")
            self.assertTrue(item["original_en"].strip())
            self.assertTrue(item["zh_cn"].strip())
            self.assertIn(len(item["keys"]), (1, 2))
            self.assertTrue(set(item["keys"]) <= LETTERS)

    def test_bipolar_items_have_two_valid_poles(self):
        for item in self.items[40:]:
            self.assertEqual(item["kind"], "bipolar")
            for field in ("left_en", "right_en", "left_zh", "right_zh"):
                self.assertTrue(item[field].strip())
            self.assertIn(item["left_key"], LETTERS)
            self.assertIn(item["right_key"], LETTERS)
            self.assertNotEqual(item["left_key"], item["right_key"])


if __name__ == "__main__":
    unittest.main()
