# 16 型人格测试 · 48 题场景图生成计划

本文件是一套完整的生图委托：把「目标效果 → 输出标准 → 逐图提示词」整套交给生图模型执行即可。
场景拆解依据见 `docs/question-scenes.md`。

## 一、目标与效果

为中文 16 型人格趣味测试的 48 道题目各配一张场景插图。用户在手机上一题一图地答题，图片的作用是：

- **一秒代入**：看到画面就明白题目在描述什么生活场景，不用咬文嚼字；
- **降低理解成本**：画面只呈现情境本身，不评判对错、不暗示该选哪个答案；
- **成套感**：48 张图像一套连环画，同一个主角贯穿始终，画风完全统一。

## 二、输出标准

- **数量**：共 48 张。Q1–Q40 为单幅场景图；S1–S8 为左右分屏对照图（同一主角、同一场景的两种做法，中间细分隔线）。
- **比例与尺寸**：1:1 正方形，不低于 1024×1024，输出 PNG（后续由项目脚本统一压缩转 WebP）。
- **文件命名**：`q01.png` … `q40.png`，`s01.png` … `s08.png`，与下方清单一一对应。
- **禁忌**：画面内不出现任何文字、字母、数字、水印、logo；不要 3D 渲染、厚涂油画、写实照片风；不要模仿任何现有人格测试品牌的角色设计。
- **内容红线**：二极题左右两边必须公平对照，不允许一边画得光鲜、另一边画得落魄。

### 风格锚点（全套唯一画风，48 张必须一致）

- 扁平矢量插画，现代编辑插画感；几何化简洁造型，边缘圆润，无描边或极细同色描边；
- 纯色填色 + 约 10% 浅色投影，无渐变、无噪点、无笔触质感；
- 浅色纯色底 `#f7f8fb`；画面配色限定在：芥末黄（主角毛衣）、海军蓝、赭红、鼠尾草绿 + 中性灰，点缀色克制；
- 配角一律做简化处理（简化五官或无五官的剪影式人物），只有主角有完整五官。

### 角色设定卡（48 张图同一个人，逐项锁定）

- **脸型**：圆润鹅蛋脸，比例约四头身，四肢圆润简化；
- **五官**：黑色豆豆眼（纯圆点）、细长弯眉、小巧鼻、温和的小嘴；表情靠眉毛和嘴型变化，眼睛始终保持豆豆眼样式；
- **发型**：黑色利落短发、齐刘海，48 张不变；
- **服装**：芥末黄圆领毛衣 + 深色直筒长裤 + 白色便鞋，48 张不变；
- **气质**：中性长相、无年龄感，不对应任何一型人格，让用户都能代入。

> 以上两项已翻译成英文并内置到下面每一条提示词里（主角描述句 + 风格开头句），生成时整段复制即可，无需再手动拼接。

## 三、生成流程建议

1. 先生成 `q01.png`，对照上方「风格锚点」和「角色设定卡」逐项确认（脸型、豆豆眼、弯眉、齐刘海短发、四头身、毛衣长裤白鞋、配色、底色）全部满意后，以它作为后续全部图片的风格参考图。
2. 按清单逐张生成，提示词整段使用、不要拆改；若工具支持种子或角色参考功能，全程固定同一设置。
3. 每张出图后快速过一遍：主角五官/发型/服装与参考图一致？无文字水印？场景与题意一致？分屏图左右公平？不合格就重新生成该张。

## 四、逐图提示词清单

### Q1–Q40 单幅场景图

**q01.png** — 人一多，更喜欢待在边上

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. A lively living-room party with a crowd laughing in a circle at the center; in the foreground the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes stands at the very edge of the room holding a drink, half hidden behind a tall potted plant, relaxed but clearly staying out of the spotlight.
```

**q02.png** — 被起哄讲笑话，只想原地消失

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. A round dinner table where several simplified figures playfully point at the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes, who is frozen in a stiff awkward grin with a sweat drop, sinking lower into the chair as if wishing to vanish, a spare spotlight glow isolating them.
```

**q03.png** — 有不同想法也常常憋着不说

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. A meeting room where a colleague presents at a whiteboard; the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes sits quietly with a small zipper across their lips, a thought bubble above holding a fully formed diagram of their own idea, one hand resting flat on the table instead of raised.
```

**q04.png** — 走到哪儿都有熟人

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. A cheerful street where the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes walks down the sidewalk while a fruit vendor, a barista, a neighbor and a delivery courier all wave hello to them, dotted connection lines linking the protagonist to each greeter.
```

**q05.png** — 聚会冷场时的救场王

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. A party gone flat with guests slumped over their phones; at the center the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes stands up holding a small speaker overhead as confetti and music notes burst out, the guests lifting their heads and lighting up.
```

**q06.png** — 一高兴就咋咋呼呼

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. The recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes telling a story with huge animated gestures, bold sound-wave rings and exclamation marks bursting outward, two nearby friends laughing while half covering their ears.
```

**q07.png** — 聊到人生意义就想溜

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. A late-night sofa scene where two friends sip tea and gaze upward at a starry sky with a giant question mark, deep in conversation; meanwhile the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes tiptoes out through the back door with a relieved grin.
```

**q08.png** — 让分析镜头隐喻就犯困

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. Two people watching a movie on a couch: one excitedly sketches storyboard frames and symbol cards mid-air, while the other — the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes — hugs a popcorn bucket and dozes off with floating Zzz letters.
```

**q09.png** — 老办法顺手就懒得换

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. The recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes contentedly tuning a vintage radio with a well-worn notebook beside them, while a shiny brand-new gadget sits pushed aside in the corner gathering a small dust cloud.
```

**q10.png** — 越烧脑读得越起劲

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. The recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes sitting cross-legged devouring an absurdly thick book, gears formulas and tiny stars swirling above their head, eyes shining bright with excitement.
```

**q11.png** — 一句话能琢磨出三层意思

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. The recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes inspecting a plain chat message on a phone through a magnifying glass, the message casting three translucent layered shadows behind it suggesting deeper and deeper readings, chin-stroking pose.
```

**q12.png** — 刷到冷知识必点进去

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. The recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes scrolling a phone under a blanket at night, a glowing trivia card with a lightbulb and a quirky little animal floating out of the screen, both the protagonist and a curious cat leaning in to look.
```

**q13.png** — 向往轰轰烈烈的感情

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. On a rooftop at dusk the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes gazes up at grand fireworks, a dreamy thought bubble above showing a cinematic montage of roses sparks and two silhouettes running through rain, eyes full of longing.
```

**q14.png** — 陌生人的难处也会跟着难受

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. On a rainy street the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes tilts their umbrella over a drenched stranger, their own shoulder getting soaked, eyes red-rimmed with heartfelt concern, soft rain lines and muted cool tones.
```

**q15.png** — 大事最后跟着感觉走

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. At a forked path signpost the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes stands with eyes closed and a hand on their chest, a glowing heart beam pointing down one path, while a detailed arrow-covered map lies ignored at their feet.
```

**q16.png** — 讲道理优先

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. A pouting friend vents with puffed cheeks while the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes kindly offers a tissue with one hand and earnestly points at a small whiteboard of logic-chain diagrams with the other, a balanced scale standing nearby.
```

**q17.png** — 看不懂当场情绪失控的人

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. A person crouched on the floor crying with dramatic emotion bursts, while beside them the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes stiffly holds out a tissue with a long trail of question marks floating above their head, utterly baffled.
```

**q18.png** — 宁愿让人服我、不敢惹我

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. The recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes walking down a hallway with calm commanding presence as simplified figures on both sides instinctively step back to clear a path, watching with awed respect, subtle crown-shaped shadow behind.
```

**q19.png** — 乱了浑身不自在

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. A desk split between chaos on the left and a perfectly aligned right-angle arrangement on the right; the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes smoothing the curled corner of the last sheet of paper, stationery lined up in parallel, visible relief on their face.
```

**q20.png** — 出门前把行程安排明白

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. The night before a trip, the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes sticks color-coded notes onto a big wall calendar and ticks items off a checklist, a half-packed suitcase open on the floor, satisfied focused expression.
```

**q21.png** — 头天晚上就收拾好

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. At night in a bedroom, the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes finishes packing a backpack against a checklist and stands it upright by the door, an alarm clock set for early morning on the nightstand, everything ready before sleep.
```

**q22.png** — 周末去哪当天早上才定

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. Saturday morning, the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes still in pajamas tosses a big die into the air to decide the day's plan, a blank unfolded map spread across the bed behind, carefree excited grin.
```

**q23.png** — 突然想做一件事说不清为什么

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. Late at night the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes suddenly springs out of bed and starts painting at a small easel, glancing back at the viewer with a shrug and a single question mark overhead, moonlight through the window.
```

**q24.png** — 两小时的活拖成三天

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. A half-finished document glows on a computer screen while the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes slouches in the chair absorbed in a phone that pulls their gaze like a magnet, calendar pages flipping past behind them marking three days gone by.
```

**q25.png** — 总在琢磨怎么提升自己

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. The recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes climbing a rising staircase whose steps hold a stack of books a dumbbell a habit tracker and a small summit flag, jotting notes while climbing, upward dynamic composition.
```

**q26.png** — 一闲下来就慌

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. On a weekend sofa the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes tries to relax but sits bolt upright, an oversized hourglass looming above their head, one hand already reaching for the to-do list on the coffee table, restless energy lines.
```

**q27.png** — 想法说出来常被人觉得怪

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. At a dining table the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes gestures enthusiastically while a thought bubble releases a tiny UFO a dinosaur and a flying cat, the friend across the table frozen mid-bite with a baffled expression.
```

**q28.png** — 重复的生活憋得难受

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. The recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes trudging on a treadmill looping through identical dull days, while outside the window a roller coaster fireworks and distant mountains glow invitingly, the protagonist leaning their whole body toward the view.
```

**q29.png** — 规则立在那儿就会遵守

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. At an empty late-night intersection with a red light and not a single car, the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes waits patiently at the crosswalk line while another figure jaywalks in the background, calm rule-following posture.
```

**q30.png** — 对老师领导尊重服从

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. In an office doorway the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes gives a polite slight bow to an older mentor figure, holding neatly organized documents, respectful upright posture, warm neutral tones.
```

**q31.png** — 能躺着绝不站着

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. The recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes melted deep into a sofa with a slice of watermelon in one hand and a remote in the other, a cat sprawled flat as a pancake beside them, maximum-relaxation composition with soft cozy tones.
```

**q32.png** — 有省事的路子绝不绕远

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. From a hilltop to the bottom, other figures trudge along a long winding switchback path while the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes whooshes straight down a giant slide to the finish, waving smugly, playful diagonal composition.
```

**q33.png** — 秘密说着说着就讲出去了

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. The recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes clamps both hands over their mouth, yet little secret bubbles keep floating out anyway, while a friend leans in closer and closer with an oversized ear, playful tension.
```

**q34.png** — 喜欢一个人表现得特别明显

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. The recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes charging toward a friend carrying an oversized heart sign and a gift box taller than themselves, the friend gasping with hands over mouth, passersby turning to look, confetti in the air.
```

**q35.png** — 一说比赛立马来劲

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. The instant a starter flag goes up, the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes is already mid-lunge with sleeves rolled up and tiny flames in their eyes, a glowing trophy waiting in the distance, explosive forward motion lines.
```

**q36.png** — 觉得自己挺不错的

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. The recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes gives a confident thumbs-up to a full-length mirror wearing sunglasses with a gleaming shine, the mirror reflecting a wall covered in little trophies and certificates, self-assured cheerful mood.
```

**q37.png** — 一句玩笑尴尬到脚趾抠地

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. After a joke at a party all heads turn toward the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes, whose face glows tomato-red with little steam puffs, toes visibly gouging two scratch lines into the floor, a small crack in the ground beckoning nearby.
```

**q38.png** — 事一多当场宕机

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. A ringing phone a stack of documents and popping message bubbles all crash toward the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes at once, their eyes turned into spinning loading icons with a wisp of smoke rising from their head, frozen mid-crash.
```

**q39.png** — 心里翻江倒海嘴上只说没事

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. The recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes smiles calmly while a translucent cutaway of their chest reveals a churning storm cloud inside, a single tiny blank speech bubble at their lips, a friend walking away in the background unaware.
```

**q40.png** — 很难完全把后背交给别人

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. Between the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes and a longtime friend stands a small transparent shield like a half-open door, the protagonist handing a gift only halfway through the gap, polite but guarded distance, soft tension in the composition.
```

### S1–S8 左右分屏对照图

**s01.png** — 倾向怀疑 ／ 愿意相信

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. Split-screen composition with a thin divider: LEFT panel — the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes inspects a gift offered by a stranger through a magnifying glass with question marks overhead; RIGHT panel — the same character accepts the same gift with both hands and a warm trusting smile, a small sun overhead.
```

**s02.png** — 随性混乱 ／ 井然有序

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. Split-screen composition with a thin divider: LEFT panel — the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes works calmly at a chaotic desk with papers flying a tilted coffee cup and a cat on the keyboard; RIGHT panel — the same character works at the same desk with labeled file boxes aligned in a perfect row, everything tidy.
```

**s03.png** — 关注整体图景 ／ 关注具体细节

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. Split-screen composition with a thin divider: LEFT panel — the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes stands on a hilltop unfolding a wide panorama map, gazing at the whole valley; RIGHT panel — the same character crouches in grass studying the veins of a single leaf through a microscope.
```

**s04.png** — 精力外放 ／ 平和内敛

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. Split-screen composition with a thin divider: LEFT panel — the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes radiates lightning-bolt energy at the center of a jumping cheering crowd; RIGHT panel — the same character sits alone by an evening window cradling a cup of hot tea with a quiet content smile.
```

**s05.png** — 跟随内心感受 ／ 遵循理性判断

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. Split-screen composition with a thin divider: LEFT panel — at a forked path the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes walks with eyes closed following a glowing floating heart; RIGHT panel — at the same fork the same character follows a glowing floating brain while checking a comparison chart in hand.
```

**s06.png** — 提前准备 ／ 临场发挥

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. Split-screen composition with a thin divider: LEFT panel — the night before a talk the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes packs notes an outfit and a water bottle against a checklist; RIGHT panel — one minute before the same talk the same character hops on stage empty-handed, improvising with a big grin.
```

**s07.png** — 关注当下 ／ 关注未来

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. Split-screen composition with a thin divider: LEFT panel — on a picnic blanket the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes leans in to admire a single flower and a lunchbox in warm sunlight; RIGHT panel — on the same meadow the same character looks through a telescope at a distant city skyline and starfield on the horizon.
```

**s08.png** — 独自工作状态最佳 ／ 团队协作状态最佳

```
Flat vector illustration, clean modern editorial style, rounded geometric shapes, solid flat colors with subtle 10% tint shading, no gradients, plain very-light background #f7f8fb, limited palette of mustard yellow navy terracotta and sage with neutral grays, background characters drawn as simplified figures with minimal or no facial features, no text, no logo. Split-screen composition with a thin divider: LEFT panel — in a quiet single room the recurring protagonist: a young East Asian person with a round oval face, simple black dot eyes, thin curved eyebrows, a tiny nose and a small gentle mouth, short neat black hair with straight bangs, about four heads tall with soft rounded limbs, wearing a mustard-yellow crewneck sweater, dark straight-leg trousers and white slip-on shoes works in deep focus with a rising flow line; RIGHT panel — the same character brainstorms with teammates around a whiteboard, idea sparks flying between everyone.
```

---

## 五、验收清单（全部生成完后过一遍）

- [ ] 48 张齐全，命名与清单一一对应（q01–q40、s01–s08）
- [ ] 主角在 48 张图里是同一个人，逐项对齐角色设定卡：鹅蛋脸、豆豆眼、细长弯眉、小鼻小嘴、齐刘海黑色短发、四头身、芥末黄毛衣 + 深色长裤 + 白鞋
- [ ] 画风全套统一：扁平矢量、圆润几何、无渐变、限定配色、`#f7f8fb` 浅底；配角均为简化人物
- [ ] 全部 1:1、≥1024px、无文字无水印无 logo
- [ ] 画风统一，且与项目现有 16 型角色插画（`assets/avatars/`）放在一起不违和
- [ ] 每张场景与对应题意一致；S 系列左右对照公平
- [ ] 与 16Personalities 等品牌角色无「一眼即似」
