# 证据链漏斗图 · 生图提示词（喂给 GPT 等生图模型）

**策略**：模型只画图形、不生成任何文字（中文和数字生图必错）。图拿回来后由项目用 Pillow 叠加简体中文标签与数字（2,230 / 278 / 25,568 / 48），保证内容准确。

## 主提示词（横向漏斗，推荐）

```text
A clean flat-design infographic on a plain very-light background (#f7f8fb): a horizontal filtering funnel composed of four connected rounded trapezoid stages arranged left to right, each stage visibly smaller than the previous one, creating a strong sense of careful selection and refinement. Stage colors in order: deep navy #243B78, teal #2E8B72, warm amber #C08A00, royal blue #5069AC. The first stage is large and wide, the last stage is small and compact, with a subtle narrowing arrow flow between stages. Leave generous empty space above each stage for a title label and below each stage for a number label. Modern editorial style, simple geometric shapes, solid colors with soft shadows, no text, no letters, no numbers, no icons of people, no watermark. Aspect ratio 16:9, 1536x864.
```

## 备选提示词（纵向漏斗）

```text
A clean flat-design infographic on a plain very-light background (#f7f8fb): a vertical funnel with four stacked rounded layers, each layer clearly narrower than the one above, emphasizing a meticulous filtering process from a large pool down to a few finalists. Layer colors from top to bottom: deep navy #243B78, teal #2E8B72, warm amber #C08A00, royal blue #5069AC. Leave empty space on the right side of each layer for a label. Modern editorial style, simple geometric shapes, solid colors with soft shadows, no text, no letters, no numbers, no watermark. Aspect ratio 4:3, 1200x900.
```

## 生成后交回时

把图片文件发给我即可。我会叠加以下文字（无需你处理）：

- `01 题目探索` · `2,230 人参与` · 提交候选题目与意见
- `02 候选池` · `278 道候选内容` · 等待筛选的题目集合
- `03 数据筛选` · `25,568 人参与` · 用于比较与缩减题目
- `04 正式量表` · `48 道正式题` · 40 道陈述 + 8 道双极

如生成结果带任何文字，请回复模型「请严格不要生成任何文字、字母或数字」后重roll。
