import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "render_card.py"
DEMO_ANSWERS = " ".join(str(v) for v in ([5, 4, 3, 2, 1] * 9 + [5, 4, 3]))

try:
    import PIL  # noqa: F401

    HAS_PILLOW = True
except ImportError:
    HAS_PILLOW = False


@unittest.skipUnless(HAS_PILLOW, "长图渲染需要 Pillow")
class RenderCardTests(unittest.TestCase):
    def test_render_card_produces_valid_png(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "card.png"
            proc = subprocess.run(
                [sys.executable, str(SCRIPT), "--answers", DEMO_ANSWERS, "--out", str(out)],
                capture_output=True,
                text=True,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertTrue(out.is_file())
            self.assertGreater(out.stat().st_size, 50 * 1024)
            self.assertEqual(out.read_bytes()[:8], b"\x89PNG\r\n\x1a\n")


if __name__ == "__main__":
    unittest.main()
