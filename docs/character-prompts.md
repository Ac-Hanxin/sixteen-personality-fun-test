# 16 型角色插画提示词（Image2 用）

本文件为 16 种类型各提供一条角色生成提示词与一句精简人格总结。**按项目维护者的决定，每个角色保留其社区俗称的标志性道具或特征**（如 INTP 手持药水瓶），同时通过差异化设计（不同的服装款式、发型、姿势、构图与统一扁平画风）与第三方品牌的角色形象拉开距离。

## 风险与边界（维护者已知情）

- 「拿烧瓶的人」「拿电钻的人」这类**概念不受版权保护**，任何品牌都不能垄断；受版权保护的是 16Personalities 角色的**具体设计表达**（特定发型、服装、配色、姿势的组合）。
- 因此每条提示词在保留俗称道具之外，对其余视觉元素做了刻意差异化，并统一使用扁平矢量画风（16P 为厚涂 3D 风）。生成后若某张图与 16P 角色「一眼即似」，请重新生成——实质性相似仍有衍生作品与不正当竞争风险。
- 16Personalities 的角色插画**原图**仍属其版权资产（见其官网 Terms 第 6 条），任何时候不要把原图或其描摹/微调版本放进仓库。

## 关于「社区俗称」

每个类型条目下的**社区俗称**（如「药水姐」「紫老头」）是中文社区对 16Personalities 角色形象的迷因称呼，不是 16P 官方文本，也不是本项目的正式命名，列在这里用于识别与检索，并作为生成图保留的标志性特征来源。俗称**文字本身不写进提示词代码块**（避免模型直接联想品牌角色），其标志物以英文道具描述的方式进入提示词。

## 使用方法

1. 每条提示词已包含统一的「风格锚点」，**整段复制**粘贴进 Image2 即可，不要拆开。
2. 建议比例 1:1（用于 README 网格）；生成 1 张满意后，如工具支持风格参考图，把它作为后续 15 张的参考以保证成套。
3. 组色规则：NT 深蓝 / NF 青绿 / SJ 琥珀 / SP 赭红作为画面点缀色；三个「老头」角色（INTJ/INFJ/ISTJ）按俗称使用紫/绿/蓝角色主色，组色退为背景点缀。
4. 生成后逐张对照下方「规避清单」检查。

## 规避清单（每张生成后自查）

- **不得与 16P 角色撞设计**：长袍/斗篷式服装（尤其紫袍老者造型）、贝雷帽画家造型、与 16P 角色相同的发型发色 + 服装组合、厚涂 3D 渲染风。出现即重新生成。
- 一般项：不要 3D 渲染、厚涂油画、写实照片风；不要水印、文字、logo。

## 通用负面提示（如工具支持 negative prompt）

```
3d render, painterly, photorealistic, watermark, text, logo, long robe, cloak, beret, copying existing brand mascot
```

---

## NT 组（深蓝点缀）

### INTJ · 系统蓝图师

社区俗称：紫老头（紫薯老头）

性格关键词：长期结构、独立判断、推演、稳步推进

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, upper-body portrait of one original character, centered, plain very-light background #f7f8fb, no text, no logo. A silver-haired senior strategist with a neatly trimmed beard, wearing a modern purple cardigan over a shirt (not a robe), standing at a drafting table unrolling a large blueprint of a future city skyline, holding a brass drawing compass, calm confident expression, planning diagrams pinned on the wall behind, deep navy accents in the background.
```

精简总结：先在脑中搭好长期结构，再全力投入。

### INTP · 原理拆解者

社区俗称：药水姐（薯条姐、小瓶子）

性格关键词：拆解、追问假设、概念框架、更新解释

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, upper-body portrait of one original character, centered, plain very-light background #f7f8fb, no text, no logo. A relaxed young woman with a loose low ponytail and round glasses, wearing an oversized navy cardigan, sitting cross-legged and holding up a small glass flask of gently bubbling teal liquid with a curious sideways glance, an old brass clockwork and scattered gears on the floor beside her along with an open notebook of diagrams, deep navy accent palette.
```

精简总结：拆开问题看清规则，再决定接不接受。

### ENTJ · 目标统筹者

社区俗称：大姐头（霸总、小暴君）

性格关键词：目标拆解、资源组合、推进、直率

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, upper-body portrait of one original character, centered, plain very-light background #f7f8fb, no text, no logo. A commanding woman with a sleek high bun, wearing a sharp navy power suit, standing before a large roadmap board marked with mountain-peak milestones and small red flags, one arm extended pointing forward, sticky notes arranged in neat columns, confident posture, deep navy accent palette.
```

精简总结：把模糊愿望变成目标、资源和节点。

### ENTP · 可能性试验家

社区俗称：骨折眉毛（杠精）

性格关键词：碰撞、反例、试验、灵活转向

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, upper-body portrait of one original character, centered, plain very-light background #f7f8fb, no text, no logo. A playful inventor with spiky hair and one sharply angular zigzag eyebrow raised mid-grin, wearing a navy hoodie, juggling three glowing lightbulbs of different shapes, forked path arrows and question marks swirling around, a paper plane flying past, deep navy accent palette.
```

精简总结：在观点碰撞中发现新可能，用实验验证。

## NF 组（青绿点缀）

### INFJ · 深层洞察者

社区俗称：绿老头（魔法老头、抹茶老头）

性格关键词：洞察、长期意义、原则、安静投入

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, upper-body portrait of one original character, centered, plain very-light background #f7f8fb, no text, no logo. A silver-bearded elder with kind deep-set eyes, wearing a sage-green knit shawl over modern clothes (not a robe), holding a small warm glowing lantern in soft mist, quiet listening posture, layered translucent silhouettes of people fading in the background, serene expression, teal accents in the mist.
```

精简总结：读懂言行背后的意义，守住长期原则。

### INFP · 内心故事家

社区俗称：小蝴蝶

性格关键词：真实感受、想象、价值、温和坚定

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, upper-body portrait of one original character, centered, plain very-light background #f7f8fb, no text, no logo. A dreamy writer with a loose teal cardigan and a low braid, sitting by a window writing in a kraft-paper journal, small teal-and-cream butterflies drifting up from the pages along with folding origami stars, a potted plant and a cup of tea on the desk, soft warm window light, gentle distant gaze.
```

精简总结：循着真实感受，为经历赋予自己的意义。

### ENFJ · 共鸣引导者

社区俗称：宝剑哥（大剑哥）

性格关键词：感知需要、鼓励、凝聚、共同愿景

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, upper-body portrait of one original character, centered, plain very-light background #f7f8fb, no text, no logo. A warm mentor in a teal jacket, standing on a small arched bridge and extending one hand to help a simplified figure across, the other hand resting on a rounded ceremonial short sword planted tip-down like a walking staff, round speech bubbles connecting overhead into a rising arch, soft sunrise tones, encouraging open posture.
```

精简总结：感知关系中的需要，用愿景带动大家。

### ENFP · 灵感点火者

社区俗称：快乐小狗

性格关键词：新鲜连接、热情、感染、自由探索

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, upper-body portrait of one original character, centered, plain very-light background #f7f8fb, no text, no logo. An energetic spark-bringer in a teal windbreaker, mid-jump lighting a trail of colorful idea-sparks like fireflies, a small excited fluffy dog leaping alongside, strings of connected dots linking simplified figures around, floating confetti dots, bright excited expression, dynamic diagonal composition.
```

精简总结：被新鲜想法点亮，也用热情点亮别人。

## SJ 组（琥珀点缀）

### ISTJ · 稳序守护者

社区俗称：蓝老头（机器人）

性格关键词：核对、承诺、流程、耐心收尾

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, upper-body portrait of one original character, centered, plain very-light background #f7f8fb, no text, no logo. A silver-haired elder with rectangular glasses, wearing a tidy blue cardigan over a white shirt, holding a clipboard with a checked list, standing beside perfectly stacked labeled boxes and a round wall clock, tidy shelf of binders behind, calm orderly expression, precise symmetrical composition, warm amber accents in the props.
```

精简总结：信任可核对的事实，认真对待每个承诺。

### ISFJ · 细节照料者

社区俗称：小护士

性格关键词：记住偏好、具体行动、稳定支持、边界

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, upper-body portrait of one original character, centered, plain very-light background #f7f8fb, no text, no logo. A caring supporter in a soft amber apron with a small nurse-style cap pinned to her hair, carrying a wooden tray with a teapot and two cups, a corkboard behind with sticky notes marked by tiny hearts and reminders, a folded blanket and a small first-aid kit on the shelf, warm attentive smile.
```

精简总结：记住具体需要，用细小行动照顾别人。

### ESTJ · 秩序推进者

社区俗称：尺子姐

性格关键词：规则、分工、期限、落地检查

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, upper-body portrait of one original character, centered, plain very-light background #f7f8fb, no text, no logo. An organized supervisor with a blunt bob haircut, amber tie and rolled-up sleeves, holding a large wooden ruler upright like a measuring standard while pointing at a row of neatly aligned small traffic cones marking milestones, a whistle on a lanyard around the neck, clear bold posture, structured grid composition, warm amber accent palette.
```

精简总结：把规则和分工讲清楚，推动事情落地。

### ESFJ · 氛围联结者

社区俗称：伞哥（蛋糕哥、男妈妈）

性格关键词：接纳、回应、联结、共同庆祝

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, upper-body portrait of one original character, centered, plain very-light background #f7f8fb, no text, no logo. A sociable host in an amber cardigan, holding a warm-yellow umbrella over a table set with a shared cake and teacups as if sheltering the gathering, string lights and a photo wall of group pictures behind, one foot forward in a welcoming gesture, cozy festive mood, warm amber accent palette.
```

精简总结：留意每个人是否被接纳，维系群体温度。

## SP 组（赭红点缀）

### ISTP · 冷静解题者

社区俗称：电钻哥

性格关键词：现场观察、动手验证、简洁动作、自主

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, upper-body portrait of one original character, centered, plain very-light background #f7f8fb, no text, no logo. A calm fixer with rolled sleeves in a terracotta work shirt and tool belt, crouching to repair a vintage bicycle, holding a compact cordless power drill in one hand, an open toolbox with neatly arranged tools beside, focused relaxed expression, clean workshop corner, terracotta red accent palette.
```

精简总结：先观察现场怎么运作，再简洁地修好它。

### ISFP · 感受收藏家

社区俗称：小画家

性格关键词：当下体验、审美细节、温和、个人节奏

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, upper-body portrait of one original character, centered, plain very-light background #f7f8fb, no text, no logo. A quiet painter with a loose side ponytail and a terracotta smock, holding a round wooden palette and a fine brush, painting sunlight filtering through leaves onto a small tabletop easel, pressed flowers in a glass frame and a watercolor sketchbook nearby, gentle observant mood, terracotta red accent palette.
```

精简总结：细致接收当下体验，温和表达珍视之物。

### ESTP · 现场破局者

社区俗称：墨镜哥

性格关键词：现实机会、直接试错、应变、行动

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, upper-body portrait of one original character, centered, plain very-light background #f7f8fb, no text, no logo. A bold sprinter in a terracotta tracksuit and dark sunglasses, bursting through a paper barrier tape at full speed, dynamic speed lines trailing behind, surprised simplified silhouettes at the edges, confident grin, high-energy action pose, terracotta red accent palette.
```

精简总结：快速读取现实机会，直接试错破局。

### ESFP · 快乐放大者

社区俗称：沙锤姐（锤子姐）

性格关键词：投入当下、及时回应、分享、放大快乐

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, upper-body portrait of one original character, centered, plain very-light background #f7f8fb, no text, no logo. A joyful performer in a terracotta jacket with small sequin dots, shaking a pair of round maracas overhead on a tiny stage, a retro microphone on a stand nearby, warm party lights and paper garlands above, a side table with shared snacks, infectious laughter, soft spotlight glow, terracotta red accent palette.
```

精简总结：全身心投入当下，把快乐放大给更多人。
