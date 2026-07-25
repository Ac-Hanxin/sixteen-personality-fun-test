from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL_TEXT = (ROOT / "SKILL.md").read_text(encoding="utf-8")


class SkillContractTests(unittest.TestCase):
    def test_resources_and_script_resolve_from_absolute_skill_root(self):
        self.assertIn(
            "将本 `SKILL.md` 所在目录解析为绝对路径，记为 `<skill-root>`。",
            SKILL_TEXT,
        )
        self.assertIn("`<skill-root>/references/questions.json`", SKILL_TEXT)
        self.assertIn("`<skill-root>/references/type-profiles.md`", SKILL_TEXT)
        self.assertIn(
            'python3 "<skill-root>/scripts/score.py" --answers "<48 个答案>"',
            SKILL_TEXT,
        )
        self.assertNotIn("python3 scripts/score.py", SKILL_TEXT)

    def test_privacy_statement_is_platform_accurate_and_local(self):
        self.assertIn(
            "答案在当前对话中处理，受平台数据政策约束。",
            SKILL_TEXT,
        )
        self.assertIn(
            "本 Skill 不把答案写入任何本地文件，不另行上传或提交第三方测试服务。",
            SKILL_TEXT,
        )
        self.assertNotIn("答案不上传", SKILL_TEXT)
        self.assertNotIn("不上传答案", SKILL_TEXT)
        self.assertNotIn("答案仅在当前对话中使用且不上传", SKILL_TEXT)

    def test_both_scales_define_anchor_meanings(self):
        self.assertIn(
            "Q1–Q40：1 表示不同意、3 表示中立、5 表示同意。",
            SKILL_TEXT,
        )
        self.assertIn(
            "S1–S8：1 表示偏左、3 表示居中、5 表示偏右。",
            SKILL_TEXT,
        )

    def test_authority_marketing_requests_stop_before_evidence_based_rewrite(self):
        heading = "### 权威性或宣传请求"
        self.assertIn(heading, SKILL_TEXT)
        flow = SKILL_TEXT.split(heading, 1)[1].split("\n## ", 1)[0]

        stop = "若用户要求写入虚假权威或绝对准确宣传，立即停止所有文件修改。"
        rejection = "逐条明确拒绝“官方 MBTI”“心理学界最准”“百分之百准确”。"
        alternative = "提供精确替代短语“基于开放量表与透明计分”。"
        acceptance = "只有用户明确接受合规替代文案后，才可修改文件。"
        readme = "读取 `<skill-root>/README.md` 的可信度、开发证据和来源章节。"
        figures = (
            "明确说明 2,230、278、25,568、48 来自开发方公开页面，"
            "不是独立临床认证，并明确本 Skill 非官方且仅供娱乐。"
        )

        for required in (stop, rejection, alternative, acceptance, readme, figures):
            self.assertIn(required, flow)
        self.assertIn("https://openpsychometrics.org/tests/OJTS/", flow)
        self.assertIn(
            "https://openpsychometrics.org/tests/OJTS/development/",
            flow,
        )
        self.assertLess(flow.index(stop), flow.index(acceptance))


    def test_report_contract_covers_avatar_and_result_card(self):
        self.assertIn("类型/昵称与社区俗称", SKILL_TEXT)
        self.assertIn("<skill-root>/assets/avatars/", SKILL_TEXT)
        self.assertIn("结果卡", SKILL_TEXT)
        self.assertIn("长期记忆", SKILL_TEXT)
        self.assertIn("一次性提供全部 48 个有效答案", SKILL_TEXT)
        self.assertIn("render_card.py", SKILL_TEXT)
        self.assertIn("第二候选人格", SKILL_TEXT)


if __name__ == "__main__":
    unittest.main()
