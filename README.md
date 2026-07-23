<h1 align="center">16 型人格趣味测试</h1>

<p align="center">
  <strong>基于 Open Jungian Type Scales 2.1 的可复现中文测评 Skill</strong><br/>
  <sub>A reproducible, agent-native Chinese workflow for the Open Jungian Type Scales 2.1 — for entertainment only.</sub>
</p>

<p align="center">
  <img alt="48 questions" src="https://img.shields.io/badge/questions-48-2f4b7c?style=flat-square" />
  <img alt="4 axes, 8 poles" src="https://img.shields.io/badge/dimensions-4_axes_8_poles-2f4b7c?style=flat-square" />
  <img alt="Python 3.9+" src="https://img.shields.io/badge/python-3.9%2B-2f4b7c?style=flat-square" />
  <img alt="web version, zero install" src="https://img.shields.io/badge/web-zero_install-2f4b7c?style=flat-square" />
  <img alt="local and deterministic scoring" src="https://img.shields.io/badge/scoring-local_%26_deterministic-2f4b7c?style=flat-square" />
  <img alt="License: CC BY-NC-SA 4.0" src="https://img.shields.io/badge/license-CC_BY--NC--SA_4.0-2f4b7c?style=flat-square" />
</p>

<p align="center">
  <strong>中文</strong> · <a href="README_EN.md">English</a>
</p>

<p align="center">
  <a href="#零安装在线版网页版">网页版</a> ·
  <a href="#一键部署提示词复制发给你的-agent">部署提示词</a> ·
  <a href="#快速开始">快速开始</a> ·
  <a href="#十六型速览">十六型速览</a> ·
  <a href="#计分规则与边界">计分规则</a> ·
  <a href="#可信度来自哪里">可信度</a> ·
  <a href="#隐私">隐私</a> ·
  <a href="#来源署名与许可">许可</a>
</p>

<p align="center">
  <img src="assets/type-characters.webp" width="820" alt="16 型人格角色群像：紫老头、药水姐、大姐头、骨折眉毛、绿老头、小蝴蝶、大剑哥、快乐小狗、蓝老头、小护士、尺子姐、男妈妈、电钻哥、小画家、墨镜哥、锤子姐" />
</p>

---

把你的 AI Agent 变成一位克制、透明的测评主持人：分 6 轮引导作答 **48 题**，本地脚本确定性计分，再生成一份看得懂边界的中文报告。它不猜测、不夸大、不冒充官方——每一个数字都可以回到来源页面核查。

| 能力 | 说明 |
| --- | --- |
| 零安装网页版 | 浏览器打开即测，手机可用；纯前端本地计分，结果卡一键复制发给助理 |
| 一键部署 | 复制一段提示词发给你的 Agent，自动完成克隆、部署、测试与记忆沉淀 |
| 分批引导作答 | 48 题分 6 轮呈现，每轮恰好 8 题；支持空格、中英文逗号、分号分隔，答错只重问错误位置 |
| 本地确定性计分 | `scripts/score.py` 只用 Python 标准库，无外部调用；相同 48 个答案永远得到相同结果 |
| 确定性的边界处理 | 完全平分标记为 X，平分时按固定顺序展示首个候选；非平分展示分差并给出最接近的第二候选 |
| 原创中文画像 | 16 型文案全部采用倾向性措辞：3 项优势、3 项坑、社交、决策、压力与观察建议 |
| 隐私克制 | 不把答案写入本地文件，不另行提交给 OJTS 或第三方测试服务，也不请求姓名等身份信息 |
| 全程可审计 | 题库保留英文原题、题号与计分键；31 项单元测试包含与公开站点逐分对照的固定样本 |

## 零安装在线版（网页版）

不想安装任何东西？仓库自带纯前端网页版，手机浏览器也能用：

**https://a31897240-coder.github.io/sixteen-personality-fun-test/web/**

- 48 题逐题作答，随时撤销上一题；进度自动保存在本机浏览器（localStorage），刷新或切出后可断点续答，计分全部在本地完成，答案不离开你的设备。
- 结果页包含角色形象、八极分数条、完整画像与「结果卡」，一键复制即可发给你的 AI 助理。
- 想先看结果页长什么样：在链接后加 `#demo`；想直接开测：加 `#quiz`。

仓库作者部署方式：GitHub 仓库 → Settings → Pages → Deploy from a branch → `main` / `(root)`，几分钟后上述链接即可访问。

## 一键部署提示词（复制发给你的 Agent）

**Hermes 版**（演示同款，利用其长期记忆沉淀结果）：

```text
请克隆 GitHub 项目 https://github.com/a31897240-coder/sixteen-personality-fun-test ，将整个目录复制到 ~/.hermes/skills/sixteen-personality-fun-test（保留 SKILL.md、references/、scripts/、assets/ 的相对位置），确认 sixteen-personality-fun-test 技能可用后，带我做一次完整的 16 型人格趣味测试；测试结束后，把结果卡存入你的长期记忆。
```

**通用版**（Claude Code / Codex / 其他支持 Skills 的客户端）：

```text
请克隆 GitHub 项目 https://github.com/a31897240-coder/sixteen-personality-fun-test ，将整个目录复制到我的技能目录（Claude Code 为 ~/.claude/skills/，Codex 为 ~/.codex/skills/，其他客户端以实际配置为准），目录名保持 sixteen-personality-fun-test 并保留内部相对结构，确认技能可用后，带我做一次完整的 16 型人格趣味测试；测试结束后，把结果卡存入你的长期记忆。
```

## 快速开始

**前置要求**

- Python 3.9 或更高版本（计分仅用标准库，零依赖安装；导出结果长图需要 `pip3 install Pillow`）
- 一个支持 Skills 的 Agent 客户端：Codex、Claude Code，或任何能发现 `SKILL.md` 的客户端

**安装**

```bash
git clone https://github.com/a31897240-coder/sixteen-personality-fun-test.git
cd sixteen-personality-fun-test
```

将整个目录复制到客户端的技能目录，并保留 `SKILL.md`、`references/`、`scripts/`、`assets/` 的相对位置：

```bash
# Claude Code（用户级技能目录）
cp -R . ~/.claude/skills/sixteen-personality-fun-test

# Codex（用户级技能目录）
cp -R . ~/.codex/skills/sixteen-personality-fun-test

# Hermes Agent（用户级技能目录）
cp -R . ~/.hermes/skills/sixteen-personality-fun-test
```

不同客户端与版本的技能目录可能不同，请以你当前客户端的配置与技能发现结果为准；本项目不承诺某个未经本机验证的第三方安装命令。

**验证安装**

新开一个会话，输入：

> 帮我做一次完整的 16 型人格趣味测试

Agent 应识别名为 `sixteen-personality-fun-test` 的 Skill：分 6 轮呈现题目，每轮 8 题；收齐并校验 48 个答案后，调用本地计分器生成报告。

**演示 / 复测快捷用法**

不想逐轮作答时，把 48 个答案按 Q1–Q40、S1–S8 的顺序（1–5 的整数，空格或逗号分隔）一次性发给 Agent，校验通过后会直接计分并生成报告，适合演示和复测。

### 不用 Agent，直接计分

如果你已经有一组答案（按 Q1–Q40、S1–S8 顺序的 48 个 1–5 整数），可以跳过对话直接计分：

```bash
python3 scripts/score.py --answers "3 3 3 …（共 48 个，空格或逗号分隔）"
```

输出 JSON 包含八极 `scores`、四轴占比与分差 `axes`、原始类型 `raw_type`（平分轴记为 `X`）、`candidates` 与 `second_candidates`。

## 测评流程

<p align="center">
  <img src="assets/assessment-flow.svg" width="760" alt="测评流程：六轮作答、格式校验、本地计分、边界判断与娱乐化报告" />
</p>

前 40 题为陈述题（1 = 不同意，3 = 中立，5 = 同意），后 8 题为双极词组题（1 = 偏左，3 = 居中，5 = 偏右）。作答过程中可以修改上一轮答案或重新开始。

## 结果示例

<p align="center">
  <img src="assets/result-preview.svg" width="760" alt="虚构 INTP 结果预览：八极分数与原理拆解者类型展示" />
</p>

预览展示的是虚构结果 **INTP · 原理拆解者**，示例八极分数为 `E 12 / I 27`、`S 15 / N 29`、`T 30 / F 14`、`J 17 / P 25`。这些数字只用于说明报告结构，**不代表任何真实用户**，也不应被解释为诊断或能力评级。

实际报告开头先给结论句（如「根据测试结果，您是 INTP（药水姐）」），再按以下顺序呈现：角色形象、类型与昵称（附社区俗称）、画像、3 项优势、3 项坑、社交、决策、压力、观察建议，以及分差最小时展示的「次人格」（第二候选的角色形象与一句话），然后是八极原始分数、四组占比与分差、边界提示与第二候选，最后是娱乐与许可说明。报告末尾提供两个选项：**保存分析结果**——生成一张包含全部报告内容的 PNG 长图（Agent 端由 `scripts/render_card.py` 渲染，需要 `pip3 install Pillow`；网页版在浏览器内直接生成）；**复制存档提示词**——一段不超过 2000 字符的「结果卡」文本，发给你的 AI 助理请它存入长期记忆，以后分析你的偏好时作为参考之一。

## 十六型速览

上方群像即 16 种类型的角色形象（本项目以 AI 工具生成的原创渲染，提示词与差异化规则见 [`docs/character-prompts.md`](docs/character-prompts.md)）。每种类型的正式昵称与概括：

| 组 | 类型 | 原创昵称 | 社区俗称 | 一句话概括 |
| --- | --- | --- | --- | --- |
| NT | INTJ | 系统蓝图师 | 紫老头 | 先在脑中搭好长期结构，再全力投入。 |
| NT | INTP | 原理拆解者 | 药水姐 | 拆开问题看清规则，再决定接不接受。 |
| NT | ENTJ | 目标统筹者 | 大姐头 | 把模糊愿望变成目标、资源和节点。 |
| NT | ENTP | 可能性试验家 | 骨折眉毛 | 在观点碰撞中发现新可能，用实验验证。 |
| NF | INFJ | 深层洞察者 | 绿老头 | 读懂言行背后的意义，守住长期原则。 |
| NF | INFP | 内心故事家 | 小蝴蝶 | 循着真实感受，为经历赋予自己的意义。 |
| NF | ENFJ | 共鸣引导者 | 大剑哥 | 感知关系中的需要，用愿景带动大家。 |
| NF | ENFP | 灵感点火者 | 快乐小狗 | 被新鲜想法点亮，也用热情点亮别人。 |
| SJ | ISTJ | 稳序守护者 | 蓝老头 | 信任可核对的事实，认真对待每个承诺。 |
| SJ | ISFJ | 细节照料者 | 小护士 | 记住具体需要，用细小行动照顾别人。 |
| SJ | ESTJ | 秩序推进者 | 尺子姐 | 把规则和分工讲清楚，推动事情落地。 |
| SJ | ESFJ | 氛围联结者 | 男妈妈 | 留意每个人是否被接纳，维系群体温度。 |
| SP | ISTP | 冷静解题者 | 电钻哥 | 先观察现场怎么运作，再简洁地修好它。 |
| SP | ISFP | 感受收藏家 | 小画家 | 细致接收当下体验，温和表达珍视之物。 |
| SP | ESTP | 现场破局者 | 墨镜哥 | 快速读取现实机会，直接试错破局。 |
| SP | ESFP | 快乐放大者 | 锤子姐 | 全身心投入当下，把快乐放大给更多人。 |

「社区俗称」是中文社区围绕 16Personalities 角色形象形成的迷因称呼（与上方群像字幕一致），不是任何品牌的官方名称，也不是本项目的正式命名；本项目正式昵称见「原创昵称」列，完整画像见 `references/type-profiles.md`。

## 计分规则与边界

测评共 **48 题**：前 40 道为陈述题，后 8 道为双极词组题。计分器分别累加 E、I、S、N、T、F、J、P 八个极的分数，每个极的理论范围为 **0–36**，随后在 E/I、S/N、T/F、J/P 四组中分别比较两侧分数，组合出四字母原始类型。

- **完全平分标记为 X**；含 X 时展示全部候选类型，并按固定顺序展示首个候选的画像——同一组答案永远得到同一结果，不提供手动调换。
- **非平分展示分差并给出最接近的第二候选**；如果多个维度的最小分差并列，第二候选可能不止一个。
- 计分不调用外部模型或在线接口；答案仍在当前对话中由平台处理。

## 与官方网站的已知差异：E/I 轴

本项目按题目语义计分——同意「聚会时我往往能够带动气氛」会增加 E 分。

截至 2026 年 7 月，openpsychometrics.org 的 OJTS 2.1 在线版本在 E/I 轴上的服务端计分与其页面自身的题注相反：其前端代码将 Q1–Q3 注释为 I、Q4–Q6 注释为 E，服务端却把 Q4–Q6 的分值计入 I（双极题 S4、S8 同样相反）。S/N、T/F、J/P 三轴本项目与官方网站完全一致；E/I 轴上，同一组答案在两边得到的字母可能不同。

你可以这样复现：在官方网站作答时，将 *I want a huge social circle.*、*I am the life of the party.*、*I make lots of noise.* 三题选 Strongly agree、其余全部中立——语义上应偏向 E，官方网站却会显示 I 开头的类型。本项目的单元测试用两组固定样本（V4、V5）逐分记录了上述差异。

## 可信度来自哪里

这里的「可信」不是权威背书，而是把来源、方法、计算和限制同时摊开，允许读者自行核查。

| 可核查维度 | 本项目如何做到 | 你可以怎样验证 |
| --- | --- | --- |
| 来源可查 | 保留 OJTS 2.1 英文原题、题号、计分键、版本与作者署名 | 对照 `references/questions.json` 与下方第一手来源 |
| 开发方法可查 | 列出开发方公开的样本与筛选数字，不把它们包装成临床认证 | 阅读 OJTS 开发页面与 OEJTS 比较页面 |
| 计分可复算 | `scripts/score.py` 只用本地确定性规则；相同 48 个答案得到相同分数与类型 | 运行本地测试，或逐项按计分键复算 |
| 平分确定性展示 | 完全平分标记为 X；非平分展示分差并给出最接近的第二候选 | 查看原始八极分数、候选类型和分差 |

## 开发证据

<p align="center">
  <img src="assets/evidence-chain.svg" width="760" alt="OJTS 公开开发证据链：从参与者与候选内容到 48 道正式题" />
</p>

OJTS 开发方公开页面描述了从候选内容到正式量表的筛选过程：**2,230** 人参与题目探索，候选池包含 **278** 道内容，后续使用 **25,568** 人的数据进行筛选，最终形成 **48** 道正式题。

这些 **2,230、278、25,568、48** 均来自 OJTS 开发方公开页面，是开发过程的可核查说明，**不是独立临床认证**，也不能证明它适合医疗诊断、招聘筛选或其他高风险决策。

## 能说什么 / 不能说什么

| 能说什么 | 不能说什么 |
| --- | --- |
| 「这次答案更偏向 I 与 N。」 | 「你天生注定就是这个类型。」 |
| 「这个结果可以作为自我观察的起点。」 | 「它能诊断心理状况或人格障碍。」 |
| 「分差较小，另一侧偏好也可能在不同情境出现。」 | 「该类型证明你适合或不适合某份工作。」 |
| 「这是基于 OJTS 2.1 的中文娱乐型工作流。」 | 「这是官方 MBTI 测试、临床工具或 16Personalities 产品。」 |

本项目**不是官方 MBTI**，仅供娱乐与自我探索。不得把结果用于临床、医学、教育分流、招聘、绩效或其他对个人有重大影响的判断。

## 隐私

运行时只读取本地题库并调用本地 Python 标准库脚本；本 Skill 不把答案写入本地文件，也不另行提交给 OJTS 或第三方测试服务，并且不请求姓名、账号或其他身份信息。答案仍在当前对话中由平台处理，对话内容如何存储与使用受平台数据政策与配置约束，不属于本 Skill 的控制范围。网页版的所有计分在浏览器本地完成，答案不离开你的设备。

## 项目结构

```
sixteen-personality-fun-test/
├── SKILL.md                  # Agent 工作流：提问、校验、计分、报告与边界规则
├── agents/openai.yaml        # Codex 客户端的展示元数据
├── references/
│   ├── questions.json        # OJTS 2.1 题库：中英对照原题 + 计分键 + 来源信息
│   └── type-profiles.md      # 16 型原创中文画像素材（含社区俗称）
├── scripts/
│   ├── score.py              # 确定性计分 CLI（仅标准库）
│   ├── render_card.py        # 渲染分析结果长图 PNG（需要 Pillow）
│   ├── build_web_data.py     # 由 references/ 生成 web/data.js 与 web/avatars64.js
│   └── slice_avatars.py      # 由 4×4 群像切割 16 张单人头像
├── web/
│   ├── index.html            # 零安装网页版（手机可用，纯前端本地计分，可生成长图）
│   ├── scoring.js            # score.py 的 JS 等价实现（测试与 Python 版逐分对照）
│   ├── data.js               # 题库与画像数据（脚本生成，请勿手改）
│   └── avatars64.js          # 头像 base64 数据（供 Canvas 出图，脚本生成）
├── assets/
│   ├── type-characters.webp  # 16 型角色群像（README 头图）
│   ├── avatars/              # 16 张单人角色头像（报告与网页版引用）
│   └── *.svg                 # 文档图形（静态、无脚本、无远程引用）
├── docs/character-prompts.md # 16 型角色插画的 AI 生成提示词与差异化规则
├── tests/                    # 31 项单元测试
└── LICENSE                   # CC BY-NC-SA 4.0
```

## 运行测试

```bash
python3 -m unittest discover -s tests -v
```

31 项测试覆盖：计分正确性（含与公开站点对照的固定样本）、网页版 JS 与 Python 计分逐分对照（需要本机装有 node，未安装时自动跳过）、题库完整性、16 型文案结构与措辞边界、SKILL.md 契约，以及本 README 与其图像资产的一致性。

## 来源、署名与许可

- [Open Jungian Type Scales 主页](https://openpsychometrics.org/tests/OJTS/)
- [OJTS 开发方法与题目筛选](https://openpsychometrics.org/tests/OJTS/development/)
- [Open Extended Jungian Type Scales 比较页面](https://openpsychometrics.org/tests/OEJTS/comparison/)
- [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/)

本包改编自 Eric Jorgenson 的 Open Jungian Type Scales / Open Extended Jungian Type Scales，并按 **CC BY-NC-SA 4.0** 提供。改编内容包括简体中文翻译、Agent 交互工作流、确定性计分实现、原创类型文案与原创 SVG 文档图形；README 中的 16 型角色插画为本项目以 AI 工具生成的原创渲染。中文翻译力求自然且保留原题含义；如有歧义，应以保留的英文原文与来源页面为核查基准。

本项目与 Eric Jorgenson、The Myers-Briggs Company 或 16Personalities 均无关联，也未获其认可。本项目不包含 16Personalities 的题目、官方类型名称、插画原作或报告文案；「社区俗称」为中文社区迷因，并非 16Personalities 官方内容。

完整许可与署名声明见 [`LICENSE`](LICENSE)。

## 作者与交流

- 抖音：[@你的抖音号](https://www.douyin.com/user/你的主页ID)——演示视频、使用反馈与版本更新
- 欢迎 Issues 与 PR：题库勘误、翻译建议、客户端适配反馈
