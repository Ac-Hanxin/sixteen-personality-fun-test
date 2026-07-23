import importlib.util
import json
import random
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("score", ROOT / "scripts" / "score.py")
score = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(score)
BANK = score.load_bank(ROOT / "references" / "questions.json")

FIXTURES = {
    "V1": [1] * 48,
    "V2": [3] * 48,
    "V3": [5] * 48,
    "V4": [1, 2, 3, 4, 5] * 9 + [1, 2, 3],
    "V5": [5, 4, 3, 2, 1] * 9 + [5, 4, 3],
}


@unittest.skipUnless(shutil.which("node"), "需要 node 运行网页版计分对照")
class WebParityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        vectors = list(FIXTURES.values())
        rng = random.Random(20260722)
        vectors += [[rng.randint(1, 5) for _ in range(48)] for _ in range(50)]
        with tempfile.NamedTemporaryFile(
            "w", suffix=".json", delete=False, encoding="utf-8"
        ) as fh:
            json.dump(vectors, fh)
            vectors_path = fh.name
        proc = subprocess.run(
            ["node", str(ROOT / "tests" / "web_parity_runner.cjs"), vectors_path],
            capture_output=True,
            text=True,
        )
        Path(vectors_path).unlink()
        if proc.returncode != 0:
            raise RuntimeError(f"node 运行失败：{proc.stderr}")
        cls.js_results = json.loads(proc.stdout)
        cls.py_results = [
            score.summarize_scores(score.score_answers(BANK, v)) for v in vectors
        ]
        cls.vectors = vectors

    def normalize(self, result):
        return json.loads(json.dumps(result, sort_keys=True))

    def test_js_scoring_matches_python_on_all_vectors(self):
        self.assertEqual(len(self.js_results), len(self.py_results))
        for label, js, py in zip(
            ["V1-V5"] * 5 + [f"R{i}" for i in range(50)], self.js_results, self.py_results
        ):
            with self.subTest(vector=label):
                self.assertEqual(self.normalize(js), self.normalize(py))

    def test_fixture_types_match(self):
        for i, name in enumerate(FIXTURES):
            with self.subTest(fixture=name):
                self.assertEqual(
                    self.js_results[i]["raw_type"], self.py_results[i]["raw_type"]
                )


if __name__ == "__main__":
    unittest.main()
