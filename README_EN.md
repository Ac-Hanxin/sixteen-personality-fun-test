<p align="center">
  <img src="assets/banner.webp" width="900" alt="16 Personalities Fun Test: based on OJTS 2.1, deterministic local scoring, for entertainment" />
</p>

<p align="center">
  <strong>Turn your answers into a personality report that is honest about its boundaries: 48 questions · deterministic local scoring · type characters · shareable long image · archivable memory card</strong><br/>
  <sub>A reproducible, agent-native Chinese workflow for the Open Jungian Type Scales 2.1 — for entertainment only.</sub>
</p>

<p align="center">
  <a href="https://img.shields.io/badge/web-zero_install-2f4b7c?style=flat-square"><img alt="web version, zero install" src="https://img.shields.io/badge/web-zero_install-2f4b7c?style=flat-square" /></a>
  <a href="https://img.shields.io/badge/license-CC_BY--NC--SA_4.0-2f4b7c?style=flat-square"><img alt="License: CC BY-NC-SA 4.0" src="https://img.shields.io/badge/license-CC_BY--NC--SA_4.0-2f4b7c?style=flat-square" /></a>
</p>

<p align="center">
  <a href="README.md">中文</a> · <strong>English</strong> ·
  <a href="#three-ways-to-use-it">Usage</a> ·
  <a href="#what-you-get">Results</a> ·
  <a href="#the-sixteen-types-at-a-glance">Types</a> ·
  <a href="#credibility--development-evidence">Credibility</a> ·
  <a href="#developers">Developers</a>
</p>

---

> **Note:** the assessment itself — questions, reports, and type profiles — is in **Simplified Chinese**. This README is for developers who want to understand, install, or adapt the project.

## Three ways to use it

| | Who | How |
| --- | --- | --- |
| **A · Web version** | Anyone, phone-friendly | Open **https://Ac-Hanxin.github.io/sixteen-personality-fun-test/web/** and start — nothing to install; `#demo` shows a sample result |
| **B · One-prompt deploy** | People with an AI agent | Paste a prompt below to your agent: clone, install, assess, and save to long-term memory |
| **C · Manual install** | Developers | See the [Developers](#developers) sections |

**The prompt for B (copy & paste)**

Hermes edition (its long-term memory keeps the result):

```text
请克隆 GitHub 项目 https://github.com/Ac-Hanxin/sixteen-personality-fun-test ，将整个目录复制到 ~/.hermes/skills/sixteen-personality-fun-test（保留 SKILL.md、references/、scripts/、assets/ 的相对位置），确认 sixteen-personality-fun-test 技能可用后，带我做一次完整的 16 型人格趣味测试；测试结束后，把结果卡存入你的长期记忆。
```

Generic edition (Claude Code / Codex / other skill-capable clients):

```text
请克隆 GitHub 项目 https://github.com/Ac-Hanxin/sixteen-personality-fun-test ，将整个目录复制到我的技能目录（Claude Code 为 ~/.claude/skills/，Codex 为 ~/.codex/skills/，其他客户端以实际配置为准），目录名保持 sixteen-personality-fun-test 并保留内部相对结构，确认技能可用后，带我做一次完整的 16 型人格趣味测试；测试结束后，把结果卡存入你的长期记忆。
```

(The prompts are intentionally in Chinese — they drive a Chinese-language assessment.)

## What you get

A report you can share — and hand to your AI assistant to remember:

- **Verdict line**: "根据测试结果，您是 INTP（药水姐）" — deterministic, no manual override; identical answers always produce the identical result
- **Main type + near type (第二候选人格)**: character art, portrait, 3 strengths, 3 pitfalls, social style, decisions, stress, observation tips; exactly one near type when the margin is smallest
- **Eight-pole scores**: raw scores, ratios, and differences across E/I, S/N, T/F, J/P; exact ties are marked X
- **Three ways to take it with you**: **share poster** (group-colored vertical card with the character, meme tags, fun meters, second-candidate type and a QR code — built for social feeds), **analysis long image** (the full report, for keeping), **archive prompt** (≤2000 characters — paste to your assistant for long-term memory, to be one reference in future decision analysis)

<table>
  <tr>
    <td width="46%"><img src="assets/sample-share-intp.webp" width="100%" alt="Share poster sample: INTP with meme tags, fun meters, second candidate and QR code" /></td>
    <td width="54%"><img src="assets/sample-analysis-intp.webp" width="100%" alt="Analysis long-image sample: full INTP report with profile, second candidate and eight-pole scores" /></td>
  </tr>
  <tr>
    <td align="center"><sub>Share poster (the author's own result)</sub></td>
    <td align="center"><sub>Analysis long image (the author's own result)</sub></td>
  </tr>
</table>

## Three steps from answers to image

<p align="center">
  <img src="assets/flow-triptych.webp" width="900" alt="The real three steps: answering, the author's INTP analysis long image, and the share poster" />
</p>

The first 40 items are statements (1 = disagree, 3 = neutral, 5 = agree); the last 8 are bipolar word pairs (1 = left pole, 3 = middle, 5 = right pole). The web version auto-saves progress to your browser's localStorage — refresh and resume anytime.

## The sixteen types at a glance

<p align="center">
  <img src="assets/type-characters.webp" width="820" alt="16 personality type characters with their Chinese community nicknames" />
</p>

Characters are original AI-generated renders (prompts and divergence rules in [`docs/character-prompts.md`](docs/character-prompts.md)). The project's own nicknames and one-line summaries:

| Group | Type | Project nickname | Community meme | One-liner (translated) |
| --- | --- | --- | --- | --- |
| NT · 紫人组 | INTJ | 系统蓝图师 | 紫老头 | Build the long-term structure in your head first, then commit. |
| NT · 紫人组 | INTP | 原理拆解者 | 药水姐 | Take the problem apart, see the rules, then decide whether to accept the answer. |
| NT · 紫人组 | ENTJ | 目标统筹者 | 大姐头 | Turn vague wishes into goals, resources, and milestones. |
| NT · 紫人组 | ENTP | 可能性试验家 | 骨折眉毛 | Find new openings in debate and test which possibilities survive. |
| NF · 绿人组 | INFJ | 深层洞察者 | 绿老头 | Read the meaning behind words and actions; hold long-term principles. |
| NF · 绿人组 | INFP | 内心故事家 | 小蝴蝶 | Follow authentic feelings and give experiences personal meaning. |
| NF · 绿人组 | ENFJ | 共鸣引导者 | 大剑哥 | Sense what relationships need and rally people toward a shared vision. |
| NF · 绿人组 | ENFP | 灵感点火者 | 快乐小狗 | Lit up by new people and ideas — and lighting up others in return. |
| SJ · 蓝人组 | ISTJ | 稳序守护者 | 蓝老头 | Trust verifiable facts and stable processes; honor every commitment. |
| SJ · 蓝人组 | ISFJ | 细节照料者 | 小护士 | Remember specific needs and care through small, concrete acts. |
| SJ · 蓝人组 | ESTJ | 秩序推进者 | 尺子姐 | Make rules, roles, and deadlines explicit; push work to completion. |
| SJ · 蓝人组 | ESFJ | 氛围联结者 | 男妈妈 | Notice who feels left out; keep the group's warmth alive. |
| SP · 黄人组 | ISTP | 冷静解题者 | 电钻哥 | Watch how the scene works, then fix it with the simplest action. |
| SP · 黄人组 | ISFP | 感受收藏家 | 小画家 | Take in the moment in fine detail; express what you treasure gently. |
| SP · 黄人组 | ESTP | 现场破局者 | 墨镜哥 | Read real opportunities fast and break deadlocks by direct trial. |
| SP · 黄人组 | ESFP | 快乐放大者 | 锤子姐 | Dive into the moment and amplify joy for everyone around. |

The "community meme" names are Chinese internet nicknames for the 16Personalities characters (matching the captions in the hero image). They are not any brand's official names and not this project's official naming — the project's own nicknames are in the "Project nickname" column; full profiles live in `references/type-profiles.md`.

## Credibility & development evidence

"Credible" here does not mean authoritative endorsement — it means sources, method, computation, and limits are all laid out for you to check.

- **Traceable source**: `references/questions.json` keeps OJTS 2.1 original English items, IDs, scoring keys, version, and author attribution — compare it with the first-hand sources below.
- **Reproducible scoring**: `scripts/score.py` uses only local deterministic rules (Python standard library, no external calls); identical 48 answers always yield identical scores and type. The web version's `web/scoring.js` is its score-by-score JS equivalent.
- **Deterministic boundaries**: **exact ties are marked X**, with the first candidate (fixed order) shown; **non-tied axes show the difference and the closest second candidate**; ties for the smallest difference can yield multiple second candidates.
- **Fully open screening**: Appendix A of the OJTS development page publishes the full list of screened items; selection was empirical — items survived only if they discriminated self-reported types, not because of theory.
- **Leading independent comparison**: on the developer's OEJTS comparison of several online tests, the OJTS shows the strongest agreement between self-reported type and test result (linked below).
- **Tested**: 32 unit tests — fixtures compared score-by-score with the public site, JS/Python scoring parity (requires `node`; skipped when absent), bank integrity, wording boundaries, and asset consistency.

**Development evidence**: the OJTS developer's public page describes the screening pipeline — **2,230** people took part in item exploration, a pool of **278** candidate items was generated, data from **25,568** participants was used for screening, and **48** final items were selected.

<p align="center">
  <img src="assets/evidence-funnel.webp" width="640" alt="OJTS 2.1 public development evidence chain: 2,230 contributors, 278 candidate items, screened with 25,568 participants, 48 final items" />
</p>

All of **2,230, 278, 25,568, and 48** come from the developer's public page. They document a traceable development process — they are **not independent clinical certification**, and they cannot show the test is fit for medical diagnosis, hiring, or other high-stakes decisions.

**Known difference from the official site (E/I axis)**: this project scores semantically — agreeing with "I am the life of the party" raises your E score. As of July 2026, the live OJTS 2.1 site at openpsychometrics.org scores the E/I axis opposite to its own page annotations: its front-end comments label Q1–Q3 as I and Q4–Q6 as E, yet the server credits Q4–Q6 to I (bipolar items S4 and S8 likewise). S/N, T/F, and J/P match the official site exactly; on E/I, the same answers can produce opposite letters. Reproduce it: on the official site, answer *Strongly agree* to *I want a huge social circle.*, *I am the life of the party.*, and *I make lots of noise.*, and neutral to everything else — semantically extraverted, yet the site reports a type starting with I. Two fixtures (V4, V5) in our unit tests record this difference score by score.

## Privacy & boundaries

At runtime the skill only reads the local question bank and calls a local Python standard-library script. It never writes answers to local files, never submits them to OJTS or third-party test services, and never asks for names, accounts, or other identity information. Answers are processed by the platform within the current conversation; how conversations are stored and used is governed by the platform's data policy and configuration, which is outside this skill's control. In the web version, all scoring runs locally in your browser — answers never leave your device; resume progress is stored only in your browser and cleared by "重新测试".

| You may say | You may not say |
| --- | --- |
| "These answers lean I and N." | "You are destined to be this type." |
| "This result can be a starting point for self-observation." | "It can diagnose psychological conditions or personality disorders." |
| "The difference is small; the other preference may show up in other contexts." | "This type proves you are or aren't suited for a job." |
| "This is a Chinese entertainment workflow based on OJTS 2.1." | "This is the official MBTI, a clinical tool, or a 16Personalities product." |

This project is **not the official MBTI**; it is for entertainment and self-exploration only. Do not use results for clinical, medical, educational-tracking, hiring, performance, or other decisions with significant personal impact.

## Developers

<details>
<summary><strong>Manual install</strong></summary>

Requirements: Python 3.9+ (scoring uses only the standard library; exporting the result image requires `pip3 install Pillow`), plus an agent client that supports Skills.

```bash
git clone https://github.com/Ac-Hanxin/sixteen-personality-fun-test.git
cd sixteen-personality-fun-test

# Claude Code (user-level)
cp -R . ~/.claude/skills/sixteen-personality-fun-test

# Codex (user-level)
cp -R . ~/.codex/skills/sixteen-personality-fun-test

# Hermes Agent (user-level)
cp -R . ~/.hermes/skills/sixteen-personality-fun-test
```

Skill directories vary by client and version; trust your own client's configuration and skill discovery over any install command the project has not verified on your machine. Start a new conversation and type 「帮我做一次完整的 16 型人格趣味测试」 to verify.

**Demo / quick-retake shortcut**: send all 48 answers at once, in Q1–Q40 then S1–S8 order (integers 1–5, separated by spaces or commas). Once validated, the agent scores and reports immediately.

</details>

<details>
<summary><strong>Score without an agent (CLI)</strong></summary>

```bash
python3 scripts/score.py --answers "3 3 3 … (48 values, space or comma separated)"
```

The JSON output contains the eight-pole `scores`, per-axis ratios and differences in `axes`, the `raw_type` (tied axes marked `X`), plus `candidates` and `second_candidates`. Render the long result image:

```bash
pip3 install Pillow
python3 scripts/render_card.py --answers "<48 answers>" --out result.png
```

</details>

<details>
<summary><strong>Project structure</strong></summary>

```
sixteen-personality-fun-test/
├── SKILL.md                  # Agent workflow: questioning, validation, scoring, reporting, boundaries
├── agents/openai.yaml        # Display metadata for Codex clients
├── references/
│   ├── questions.json        # OJTS 2.1 bank: bilingual items + scoring keys + provenance
│   └── type-profiles.md      # Original Chinese profiles for the 16 types (incl. meme names)
├── scripts/
│   ├── score.py              # Deterministic scoring CLI (standard library only)
│   ├── render_card.py        # Renders the long result-image PNG (requires Pillow)
│   ├── build_web_data.py     # Generates web/data.js and web/avatars64.js
│   └── slice_avatars.py      # Slices the 4×4 group image into 16 avatars
├── web/
│   ├── index.html            # Zero-install web version (mobile-friendly, client-side, image export)
│   ├── scoring.js            # JS equivalent of score.py (tested score-by-score against it)
│   ├── data.js               # Question & profile data (generated — do not hand-edit)
│   └── avatars64.js          # Base64 avatars for canvas rendering (generated)
├── assets/                   # Group image, 16 avatars, banner, sample images, SVG graphics
├── docs/character-prompts.md # AI-generation prompts and divergence rules for the characters
├── tests/                    # 32 unit tests
└── LICENSE                   # CC BY-NC-SA 4.0
```

Assessment flow:

<p align="center">
  <img src="assets/assessment-flow.svg" width="760" alt="Assessment flow: six rounds, format validation, local scoring, boundary handling, entertainment report" />
</p>

</details>

<details>
<summary><strong>Running the tests</strong></summary>

```bash
python3 -m unittest discover -s tests -v
```

32 tests cover: scoring correctness (including fixtures compared with the public site), score-by-score parity between the web version's JS and the Python scorer (requires `node`; skipped automatically when absent), question-bank integrity, profile structure and wording boundaries, the SKILL.md contract, and the consistency of this README with its image assets.

</details>

## Sources, attribution & license

- [Open Jungian Type Scales](https://openpsychometrics.org/tests/OJTS/)
- [OJTS development and item screening](https://openpsychometrics.org/tests/OJTS/development/)
- [Open Extended Jungian Type Scales comparison](https://openpsychometrics.org/tests/OEJTS/comparison/)
- [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/)

This package adapts Eric Jorgenson's Open Jungian Type Scales / Open Extended Jungian Type Scales and is provided under **CC BY-NC-SA 4.0**. Adaptations include the Simplified Chinese translation, the agent interaction workflow, the deterministic scoring implementation, original type-profile copy, and original SVG documentation graphics; the 16 type characters in the README are original AI-generated renders. The translation aims to be natural while preserving the original meaning; in case of ambiguity, the retained English originals and the source pages are the reference.

This project is not affiliated with or endorsed by Eric Jorgenson, The Myers-Briggs Company, or 16Personalities. It contains no 16Personalities questions, official type names, original illustrations, or report copy; the "community meme" names are Chinese internet memes, not official 16Personalities content.

See [`LICENSE`](LICENSE) for the full license and attribution statement.

## Author & community

- Douyin (Chinese TikTok): [@your-douyin-handle](https://www.douyin.com/user/your-id) — demo videos, feedback, and release updates
- Issues and PRs are welcome: question-bank errata, translation suggestions, client compatibility reports
