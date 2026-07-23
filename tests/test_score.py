import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("score", ROOT / "scripts" / "score.py")
score = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(score)
BANK = score.load_bank(ROOT / "references" / "questions.json")


class ScoreTests(unittest.TestCase):
    def test_uniform_vectors_match_known_scale_totals(self):
        for answer, expected in ((1, 4), (3, 18), (5, 32)):
            scores = score.score_answers(BANK, [answer] * 48)
            self.assertEqual(scores, {letter: expected for letter in "EISNTFJP"})

    def test_public_site_parity_fixtures(self):
        def raw_public_hidden_fields_to_semantic_scores(raw_public):
            semantic = dict(raw_public)
            semantic["E"], semantic["I"] = raw_public["I"], raw_public["E"]
            return semantic

        fixtures = {
            "V1": (
                [1] * 48,
                {"E": 4, "I": 4, "S": 4, "N": 4, "T": 4, "F": 4, "J": 4, "P": 4},
            ),
            "V2": (
                [3] * 48,
                {"E": 18, "I": 18, "S": 18, "N": 18, "T": 18, "F": 18, "J": 18, "P": 18},
            ),
            "V3": (
                [5] * 48,
                {"E": 32, "I": 32, "S": 32, "N": 32, "T": 32, "F": 32, "J": 32, "P": 32},
            ),
            "V4": (
                [1, 2, 3, 4, 5] * 9 + [1, 2, 3],
                {"E": 18, "I": 19, "S": 19, "N": 15, "T": 22, "F": 17, "J": 23, "P": 13},
            ),
            "V5": (
                [5, 4, 3, 2, 1] * 9 + [5, 4, 3],
                {"E": 18, "I": 17, "S": 17, "N": 21, "T": 14, "F": 19, "J": 13, "P": 23},
            ),
        }
        for label, (answers, raw_public) in fixtures.items():
            with self.subTest(vector=label):
                local_semantic = score.score_answers(BANK, answers)
                public_semantic = raw_public_hidden_fields_to_semantic_scores(raw_public)
                self.assertEqual(local_semantic, public_semantic)
                if label in {"V4", "V5"}:
                    self.assertNotEqual(raw_public, local_semantic)
                    self.assertEqual(
                        (raw_public["E"], raw_public["I"]),
                        (local_semantic["I"], local_semantic["E"]),
                    )

    def test_each_pole_can_reach_36(self):
        for pole in "EISNTFJP":
            answers = score.answers_targeting_pole(BANK, pole)
            self.assertEqual(score.score_answers(BANK, answers)[pole], 36)

    def test_all_neutral_is_complete_boundary(self):
        result = score.summarize_scores(score.score_answers(BANK, [3] * 48))
        self.assertEqual(result["raw_type"], "XXXX")
        self.assertEqual(result["boundary_axes"], ["E/I", "S/N", "T/F", "J/P"])

    def test_target_letters_produce_all_sixteen_types(self):
        expected = {
            f"{e}{s}{t}{j}"
            for e in "EI" for s in "SN" for t in "TF" for j in "JP"
        }
        actual = set()
        for type_code in sorted(expected):
            answers = score.answers_targeting_type(BANK, type_code)
            result = score.summarize_scores(score.score_answers(BANK, answers))
            actual.add(result["raw_type"])
        self.assertEqual(actual, expected)

    def test_parser_rejects_bad_answer_count_and_range(self):
        with self.assertRaisesRegex(ValueError, "48"):
            score.parse_answers("1,2,3")
        with self.assertRaisesRegex(ValueError, "1 到 5"):
            score.parse_answers(",".join(["6"] * 48))

    def test_cli_reports_clean_error_without_traceback(self):
        import subprocess
        import sys

        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "score.py"), "--answers", "1,2,3"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 1)
        self.assertIn("错误：", proc.stderr)
        self.assertIn("48", proc.stderr)
        self.assertNotIn("Traceback", proc.stderr)


if __name__ == "__main__":
    unittest.main()
