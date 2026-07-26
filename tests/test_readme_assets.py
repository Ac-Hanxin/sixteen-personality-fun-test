import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
ASSETS = (
    ROOT / "assets" / "assessment-flow.svg",
)


class ReadmeAssetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.readme = README.read_text(encoding="utf-8")

    def test_readme_contains_evidence_limits_and_all_assets(self):
        for phrase in ("48 题", "25,568", "CC BY-NC-SA 4.0", "不是官方 MBTI", "仅供娱乐与自我探索"):
            self.assertIn(phrase, self.readme)
        for asset in ASSETS:
            self.assertIn(f"assets/{asset.name}", self.readme)

    def test_readme_links_primary_sources(self):
        for url in (
            "https://openpsychometrics.org/tests/OJTS/",
            "https://openpsychometrics.org/tests/OJTS/development/",
            "https://openpsychometrics.org/tests/OEJTS/comparison/",
            "https://creativecommons.org/licenses/by-nc-sa/4.0/",
        ):
            self.assertIn(url, self.readme)

    def test_privacy_claims_match_the_actual_conversation_boundary(self):
        assessment_flow = (ROOT / "assets" / "assessment-flow.svg").read_text(encoding="utf-8")
        for document in (self.readme, assessment_flow):
            self.assertNotIn("答案不出本地", document)
            self.assertNotIn("不上传答案", document)
            self.assertIn("不把答案写入本地文件", document)
            self.assertIn("不另行提交给 OJTS", document)
            self.assertIn("第三方测试服务", document)
            self.assertIn("受平台数据政策与配置约束", document)

    def test_boundary_copy_matches_the_scoring_algorithm(self):
        assessment_flow = (ROOT / "assets" / "assessment-flow.svg").read_text(encoding="utf-8")
        for document in (self.readme, assessment_flow):
            self.assertNotIn("接近边界会被标记", document)
            self.assertNotIn("提示接近与平分", document)
            self.assertIn("完全平分标记为 X", document)
            self.assertIn("非平分展示分差并给出最接近的第二候选", document)

    def test_svgs_are_static_local_xml(self):
        for asset in ASSETS:
            root = ET.parse(asset).getroot()
            xml = asset.read_text(encoding="utf-8").lower()
            remote_xml = xml.replace("http://www.w3.org/2000/svg", "")
            self.assertTrue(root.tag.endswith("svg"))
            self.assertNotIn("<script", xml)
            self.assertNotIn("http://", remote_xml)
            self.assertNotIn("https://", remote_xml)

    def test_character_image_is_compact_and_referenced(self):
        img = ROOT / "assets" / "type-characters.webp"
        self.assertTrue(img.is_file())
        self.assertLess(img.stat().st_size, 800 * 1024)
        self.assertIn("assets/type-characters.webp", self.readme)

    def test_readme_visual_assets_exist_and_are_compact(self):
        for name in ("banner.webp", "flow-triptych.webp", "evidence-funnel.webp", "sample-analysis-intp.webp", "sample-share-intp.webp"):
            img = ROOT / "assets" / name
            self.assertTrue(img.is_file(), img)
            self.assertLess(img.stat().st_size, 1024 * 1024, img)
            self.assertIn(f"assets/{name}", self.readme)

    def test_avatars_exist_for_all_sixteen_types(self):
        codes = (
            "intj intp entj entp infj infp enfj enfp "
            "istj isfj estj esfj istp isfp estp esfp"
        ).split()
        for code in codes:
            img = ROOT / "assets" / "avatars" / f"{code}.webp"
            self.assertTrue(img.is_file(), img)
            self.assertLess(img.stat().st_size, 60 * 1024, img)
            self.assertEqual(img.read_bytes()[:4], b"RIFF", img)

    def test_question_scene_images_exist_for_all_48_items(self):
        names = [f"q{i:02d}" for i in range(1, 41)] + [f"s{i:02d}" for i in range(1, 9)]
        for name in names:
            img = ROOT / "assets" / "questions" / f"{name}.webp"
            self.assertTrue(img.is_file(), img)
            self.assertLess(img.stat().st_size, 150 * 1024, img)
            self.assertEqual(img.read_bytes()[:4], b"RIFF", img)

    def test_likert_labels_display_agree_first_and_map_to_five(self):
        import re
        html = (ROOT / "web" / "index.html").read_text(encoding="utf-8")
        block = re.search(r'LIKERT_LABELS = \[(.*?)\];', html, re.S).group(1)
        items = re.findall(r'\["[^"]*",\s*"([^"]+)"\]', block)
        self.assertEqual(len(items), 5)
        self.assertNotIn("不", items[0], "顶部选项必须是符合方向（数值 5）")
        self.assertIn("不", items[4], "底部选项必须是不符合方向（数值 1）")
        self.assertIn("5 - i", html, "展示顺序反转后，分值必须按 5 - i 映射")

    def test_web_version_references_local_assets(self):
        html = (ROOT / "web" / "index.html").read_text(encoding="utf-8")
        self.assertIn("data.js", html)
        self.assertIn("scoring.js", html)
        self.assertIn("../assets/avatars/", html)
        self.assertIn("../assets/type-characters.webp", html)
        self.assertIn("localStorage", html)
        self.assertTrue((ROOT / "web" / "data.js").is_file())
        self.assertTrue((ROOT / "web" / "scoring.js").is_file())
        self.assertTrue((ROOT / "web" / "avatars64.js").is_file())


if __name__ == "__main__":
    unittest.main()
