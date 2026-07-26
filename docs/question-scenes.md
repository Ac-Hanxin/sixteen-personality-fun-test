# 48 题场景化拆解（生图用）

每题拆解为一个拟人化场景，配合网页版题目展示，帮助用户一眼代入、凭直觉作答。
对应的生图执行计划见 `docs/image-generation-plan.md`，成品图为 `assets/questions/` 下的 48 张 WebP。

## 场景设计要点

- 场景与题目表达的是**同一种行为/倾向**，没有跑偏或加戏；
- 画面只呈现「情境」，不剧透答案方向（不画对错、不画鄙视链）；
- 二极题（S1–S8）左右两幅是**同一件事的两种做法**，对照公平、不捧一踩一。

## 生图使用说明

1. 每条提示词已包含统一风格锚点与固定主角描述，**整段复制**，不要拆开。
2. 建议比例 1:1（网页题卡用，正方形）；先生成 1 张满意后，作为后续 47 张的风格参考图以保证成套。
3. 固定主角（贯穿全套，提高系列感）：**短发年轻人，芥末黄圆领毛衣 + 深色长裤**，中性长相，不对应任何一型人格。
4. 风格与 16 型角色插画一致：扁平矢量、纯色 + 10% 浅色阴影、`#f7f8fb` 浅底。
5. 负面提示词（如工具支持）：

```
3d render, painterly, photorealistic, watermark, text, logo, words, letters, long robe, cloak, beret, copying existing brand mascot
```

6. 出图后自查：无文字无水印；主角形象与参考图一致；与 16Personalities 角色无「一眼即似」。

---

## 第一部分：场景选择题（Q1–Q40）

### Q1 🫥（计分键 I）

- 原题：人一多，我更喜欢待在边上，不想被大家盯着看。
- 场景拆解：热闹的客厅派对，人群在中央围成圈笑闹；主角端着饮料贴在墙边，半个身子藏在大型绿植后面，表情放松但绝不往中心走。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A lively living-room party with a crowd laughing in a circle at the center; in the foreground a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers stands at the very edge of the room holding a drink, half hidden behind a tall potted plant, relaxed but clearly staying out of the spotlight.
```

### Q2 🫠（计分键 I）

- 原题：饭局上有人起哄「来讲个笑话」，我只想原地消失。
- 场景拆解：圆桌饭局，几只手起哄地指向主角，所有目光聚过来；主角僵在座位上尬笑，额头冒汗，恨不得钻进椅子底下。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A round dinner table where several simplified figures playfully point at one young person with short black hair in a mustard-yellow crewneck sweater and dark trousers, who is frozen in a stiff awkward grin with a sweat drop, sinking lower into the chair as if wishing to vanish, a spare spotlight glow isolating them.
```

### Q3 🤐（计分键 I）

- 原题：开会时就算有不同想法，我也常常先憋着不说。
- 场景拆解：会议室里别人在发言，主角嘴前有一个小拉链，头顶思考泡泡里装着完整的想法图表，手放在桌上没举起来。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A meeting room where a colleague presents at a whiteboard; a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers sits quietly with a small zipper across their lips, a thought bubble above holding a fully formed diagram of their own idea, one hand resting flat on the table instead of raised.
```

### Q4 🤝（计分键 E）

- 原题：朋友越多越好，我巴不得走到哪儿都有熟人。
- 场景拆解：主角走在一条生活化的街道上，沿途水果摊主、咖啡师、邻居、快递小哥都笑着跟他挥手打招呼，人与人之间有连线。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A cheerful street where a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers walks down the sidewalk while a fruit vendor, a barista, a neighbor and a delivery courier all wave hello to them, dotted connection lines linking the protagonist to each greeter.
```

### Q5 🎉（计分键 E）

- 原题：聚会冷场时，我通常是那个把气氛重新炒热的人。
- 场景拆解：聚会上众人低头玩手机、气氛凝固；主角站到中间高举蓝牙音箱，彩带和音符炸开，大家被点燃抬头。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A party gone flat with guests slumped over their phones; at the center a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers stands up holding a small speaker overhead as confetti and music notes burst out, the guests lifting their heads and lighting up.
```

### Q6 📣（计分键 E）

- 原题：我一高兴就容易咋咋呼呼，存在感藏不住。
- 场景拆解：主角手舞足蹈讲故事，夸张的声波环和感叹号从身上炸开，周围朋友笑着捂耳朵。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A young person with short black hair in a mustard-yellow crewneck sweater and dark trousers telling a story with huge animated gestures, bold sound-wave rings and exclamation marks bursting outward, two nearby friends laughing while half covering their ears.
```

### Q7 🏃（计分键 S）

- 原题：一聊到「人生的意义是什么」，我就想溜。
- 场景拆解：夜晚沙发上，两位朋友捧着茶仰头聊得投入，头顶是星空与巨大的问号；主角踮着脚从后门悄悄溜走。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A late-night sofa scene where two friends sip tea and gaze upward at a starry sky with a giant question mark, deep in conversation; meanwhile a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers tiptoes out through the back door with a relieved grin.
```

### Q8 🎬（计分键 S）

- 原题：看电影就图个爽，让我分析镜头隐喻我会犯困。
- 场景拆解：沙发上看电影，旁边朋友激动地比划分镜草图和隐喻图卡；主角抱着爆米花头一点一点地打瞌睡，飘出 Zzz。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. Two people watching a movie on a couch: one excitedly sketches storyboard frames and symbol cards mid-air, while the other — a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers — hugs a popcorn bucket and dozes off with floating Zzz letters.
```

### Q9 🏮（计分键 S）

- 原题：用顺手的老办法，我懒得换，一直用下去就挺好。
- 场景拆解：主角满足地用着一台老式收音机/旧笔记本，旁边一台闪亮的新款设备被推开的扶手椅挡住，落灰。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A young person with short black hair in a mustard-yellow crewneck sweater and dark trousers contentedly tuning a vintage radio with a well-worn notebook beside them, while a shiny brand-new gadget sits pushed aside in the corner gathering a small dust cloud.
```

### Q10 🧠（计分键 N）

- 原题：越烧脑的书和文章，我读得越起劲。
- 场景拆解：主角盘腿坐着啃一本厚得夸张的书，头顶齿轮、公式与星光转动，眼睛亮得像灯泡。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A young person with short black hair in a mustard-yellow crewneck sweater and dark trousers sitting cross-legged devouring an absurdly thick book, gears formulas and tiny stars swirling above their head, eyes shining bright with excitement.
```

### Q11 🔍（计分键 N）

- 原题：朋友随口一句话，我能琢磨出三层意思。
- 场景拆解：主角举着放大镜看手机上一条普通聊天消息，消息背后叠出三层半透明的影子，越想越深入。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A young person with short black hair in a mustard-yellow crewneck sweater and dark trousers inspecting a plain chat message on a phone through a magnifying glass, the message casting three translucent layered shadows behind it suggesting deeper and deeper readings, chin-stroking pose.
```

### Q12 🧐（计分键 N）

- 原题：刷到没见过的冷知识，我一定会点进去看。
- 场景拆解：主角窝在被窝里刷手机，一张发光的「冷知识卡片」（发光灯泡+奇怪小动物图案）从屏幕里浮出来，主角和猫一起凑近看。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A young person with short black hair in a mustard-yellow crewneck sweater and dark trousers scrolling a phone under a blanket at night, a glowing trivia card with a lightbulb and a quirky little animal floating out of the screen, both the protagonist and a curious cat leaning in to look.
```

### Q13 🌹（计分键 F）

- 原题：我向往那种轰轰烈烈、像电影一样的感情。
- 场景拆解：天台傍晚，主角仰望漫天烟花，脑内幻想泡泡里上演玫瑰、烟火、雨中奔跑的电影画面。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. On a rooftop at dusk a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers gazes up at grand fireworks, a dreamy thought bubble above showing a cinematic montage of roses sparks and two silhouettes running through rain, eyes full of longing.
```

### Q14 🥺（计分键 F）

- 原题：看到陌生人遇到难处，我心里也会跟着难受半天。
- 场景拆解：雨天街头，主角把伞倾向一位淋雨的陌生人，自己半边肩膀湿透，眼圈泛红。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. On a rainy street a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers tilts their umbrella over a drenched stranger, their own shoulder getting soaked, eyes red-rimmed with heartfelt concern, soft rain lines and muted cool tones.
```

### Q15 ❤️（计分键 F）

- 原题：大事面前，我最后还是会跟着感觉走。
- 场景拆解：人生岔路口，主角脚边摊着一张画满箭头的地图却不看，闭着眼睛把手放在胸口，胸口的心发着光指向其中一条路。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. At a forked path signpost a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers stands with eyes closed and a hand on their chest, a glowing heart beam pointing down one path, while a detailed arrow-covered map lies ignored at their feet.
```

### Q16 ⚖️（计分键 T）

- 原题：讲道理优先，哪怕听起来有点不近人情。
- 场景拆解：朋友气鼓鼓地吐槽，主角一边递纸巾，一边认真指着一块画满逻辑链条的小白板，天平在旁边端平。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A pouting friend vents with puffed cheeks while a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers kindly offers a tissue with one hand and earnestly points at a small whiteboard of logic-chain diagrams with the other, a balanced scale standing nearby.
```

### Q17 🤨（计分键 T）

- 原题：看到有人当场情绪失控，我脑子里只有一串问号。
- 场景拆解：旁边的人蹲地大哭、情绪爆发；主角僵直地递着纸巾，头顶冒出一长串问号，完全不知所措。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A person crouched on the floor crying with dramatic emotion bursts, while beside them a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers stiffly holds out a tissue with a long trail of question marks floating above their head, utterly baffled.
```

### Q18 👑（计分键 T）

- 原题：与其让人人喜欢我，不如让大家服我、不敢惹我。
- 场景拆解：主角从走廊走过，气场两米八，两侧的人不自觉让出一条路、投来敬畏的目光，主角表情平静有威严。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A young person with short black hair in a mustard-yellow crewneck sweater and dark trousers walking down a hallway with calm commanding presence as simplified figures on both sides instinctively step back to clear a path, watching with awed respect, subtle crown-shaped shadow behind.
```

### Q19 🗂️（计分键 J）

- 原题：桌面乱、计划乱，我就浑身不自在。
- 场景拆解：一张书桌左半边乱糟糟、右半边已被收拾成直角阵列；主角正在把最后一张纸的卷角抚平，文具全部对齐。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A desk split between chaos on the left and a perfectly aligned right-angle arrangement on the right; a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers smoothing the curled corner of the last sheet of paper, stationery lined up in parallel, visible relief on their face.
```

### Q20 🗓️（计分键 J）

- 原题：出门前我要把行程安排明白，心里才踏实。
- 场景拆解：出发前夜，主角站在大日历前贴彩色便签、给清单逐项打勾，行李箱半开躺在地上。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. The night before a trip, a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers sticks color-coded notes onto a big wall calendar and ticks items off a checklist, a half-packed suitcase open on the floor, satisfied focused expression.
```

### Q21 🎒（计分键 J）

- 原题：第二天有重要的事，我头天晚上就把东西收拾好。
- 场景拆解：晚上卧室，主角对照清单把背包收好立在门口，闹钟定到清晨，安心上床。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. At night in a bedroom, a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers finishes packing a backpack against a checklist and stands it upright by the door, an alarm clock set for early morning on the nightstand, everything ready before sleep.
```

### Q22 🎲（计分键 P）

- 原题：周末去哪玩？我基本都是当天早上才决定。
- 场景拆解：周六早上主角还穿着睡衣，往空中抛骰子决定行程，床上摊着一张空白地图，表情兴奋随意。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. Saturday morning, a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers still in pajamas tosses a big die into the air to decide the day's plan, a blank unfolded map spread across the bed behind, carefree excited grin.
```

### Q23 🤷（计分键 P）

- 原题：我偶尔会突然想做一件事，自己也说不清为什么。
- 场景拆解：深夜主角突然从床上弹起来开始画画/组装东西，自己回头耸个肩，头顶一个小问号。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. Late at night a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers suddenly springs out of bed and starts painting at a small easel, glancing back at the viewer with a shrug and a single question mark overhead, moonlight through the window.
```

### Q24 📱（计分键 P）

- 原题：两小时能做完的活儿，我刷刷手机就拖成了三天。
- 场景拆解：电脑屏幕上是做了一半的文档，主角却瘫在椅子上刷手机，手机像磁铁一样吸住视线，身后日历一页页翻过三天。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A half-finished document glows on a computer screen while a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers slouches in the chair absorbed in a phone that pulls their gaze like a magnet, calendar pages flipping past behind them marking three days gone by.
```

### Q25 📈（计分键 N·J）

- 原题：我总在琢磨怎么提升自己，根本停不下来。
- 场景拆解：主角沿着台阶一路向上，台阶上依次摆着书、哑铃、打卡表和小旗子，主角边走边在笔记本上记录。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A young person with short black hair in a mustard-yellow crewneck sweater and dark trousers climbing a rising staircase whose steps hold a stack of books a dumbbell a habit tracker and a small summit flag, jotting notes while climbing, upward dynamic composition.
```

### Q26 ⏳（计分键 N·J）

- 原题：一闲下来我就慌，总觉得自己该去干点「正事」。
- 场景拆解：周末沙发，主角刚躺下就坐立不安，头顶的时钟被放大成沙漏压过来，主角半起身伸手去够桌上的待办清单。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. On a weekend sofa a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers tries to relax but sits bolt upright, an oversized hourglass looming above their head, one hand already reaching for the to-do list on the coffee table, restless energy lines.
```

### Q27 🛸（计分键 N·P）

- 原题：我脑子里有些想法，说出来常被人觉得「怪」。
- 场景拆解：餐桌旁主角兴奋地比划，头顶泡泡里飞出小飞碟、恐龙和会飞的猫；对面朋友一脸「啊？」的表情。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. At a dining table a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers gestures enthusiastically while a thought bubble releases a tiny UFO a dinosaur and a flying cat, the friend across the table frozen mid-bite with a baffled expression.
```

### Q28 🎢（计分键 N·P）

- 原题：每天重复一样的生活，我会憋得难受。
- 场景拆解：主角在一台无限循环的跑步机上机械迈步，窗外却是过山车、烟花和远山，主角整个人探向窗户。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A young person with short black hair in a mustard-yellow crewneck sweater and dark trousers trudging on a treadmill looping through identical dull days, while outside the window a roller coaster fireworks and distant mountains glow invitingly, the protagonist leaning their whole body toward the view.
```

### Q29 🚦（计分键 S·J）

- 原题：规则立在那儿，我就会老老实实遵守。
- 场景拆解：深夜无人的路口红灯亮着，路上一辆车都没有，主角依然站在斑马线前安静等灯，另一个人正乱穿马路。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. At an empty late-night intersection with a red light and not a single car, a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers waits patiently at the crosswalk line while another figure jaywalks in the background, calm rule-following posture.
```

### Q30 🫡（计分键 S·J）

- 原题：对老师和领导，我基本是尊重服从的。
- 场景拆解：办公室/教室门口，主角向长辈或领导礼貌地微微鞠躬问好，姿态端正，手里拿着整理好的资料。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. In an office doorway a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers gives a polite slight bow to an older mentor figure, holding neatly organized documents, respectful upright posture, warm neutral tones.
```

### Q31 🛋️（计分键 S·P）

- 原题：人生苦短，能躺着的时候我绝不站着。
- 场景拆解：主角整个人陷进沙发里，一手西瓜一手遥控器，猫也摊成一张饼在旁边，极致松弛。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A young person with short black hair in a mustard-yellow crewneck sweater and dark trousers melted deep into a sofa with a slice of watermelon in one hand and a remote in the other, a cat sprawled flat as a pancake beside them, maximum-relaxation composition with soft cozy tones.
```

### Q32 🛝（计分键 S·P）

- 原题：有省事的路子，我绝不绕远。
- 场景拆解：从山顶到山脚，别人沿着盘山步道绕大圈，主角坐着大滑梯直接滑到终点，还得意地挥手。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. From a hilltop to the bottom, other figures trudge along a long winding switchback path while a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers whooshes straight down a giant slide to the finish, waving smugly, playful diagonal composition.
```

### Q33 🗣️（计分键 E·F）

- 原题：我心里藏不住事，秘密说着说着就讲出去了。
- 场景拆解：主角捂着自己的嘴，但秘密泡泡还是一个接一个从嘴里飘出来，旁边的朋友竖起耳朵越凑越近。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A young person with short black hair in a mustard-yellow crewneck sweater and dark trousers clamps both hands over their mouth, yet little secret bubbles keep floating out anyway, while a friend leans in closer and closer with an oversized ear, playful tension.
```

### Q34 💌（计分键 E·F）

- 原题：喜欢一个人，我会表现得特别明显，藏都藏不住。
- 场景拆解：主角举着巨大的爱心牌子、抱着比人还高的礼物盒冲向朋友，朋友惊喜捂嘴，路人纷纷侧目。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A young person with short black hair in a mustard-yellow crewneck sweater and dark trousers charging toward a friend carrying an oversized heart sign and a gift box taller than themselves, the friend gasping with hands over mouth, passersby turning to look, confetti in the air.
```

### Q35 🏆（计分键 E·T）

- 原题：一说要比赛、要 PK，我立马来劲。
- 场景拆解：有人刚举起「比赛开始」的小旗，主角已经撸起袖子冲出去半步，眼里燃着小火苗，远处奖杯发光。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. The instant a starter flag goes up, a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers is already mid-lunge with sleeves rolled up and tiny flames in their eyes, a glowing trophy waiting in the distance, explosive forward motion lines.
```

### Q36 😎（计分键 E·T）

- 原题：说实话，我觉得自己挺不错的。
- 场景拆解：主角对着穿衣镜竖起大拇指，墨镜反着光，镜子里映出满满一面墙的小奖杯和奖状。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A young person with short black hair in a mustard-yellow crewneck sweater and dark trousers gives a confident thumbs-up to a full-length mirror wearing sunglasses with a gleaming shine, the mirror reflecting a wall covered in little trophies and certificates, self-assured cheerful mood.
```

### Q37 😳（计分键 I·F）

- 原题：别人一句玩笑，我能尴尬得脚趾抠地。
- 场景拆解：聚会上一句玩笑后全场看来，主角脸红到冒烟，双脚在地板上抠出两道痕，恨不得钻进旁边的地缝。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. After a joke at a party all heads turn toward a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers, whose face glows tomato-red with little steam puffs, toes visibly gouging two scratch lines into the floor, a small crack in the ground beckoning nearby.
```

### Q38 🤯（计分键 I·F）

- 原题：好几件事同时砸过来，我当场就宕机。
- 场景拆解：电话响、消息弹窗、文件堆同时砸向主角，主角脑袋上冒着烟、眼睛变成加载中的转圈，整个人死机定格。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A ringing phone a stack of documents and popping message bubbles all crash toward a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers at once, their eyes turned into spinning loading icons with a wisp of smoke rising from their head, frozen mid-crash.
```

### Q39 🌫️（计分键 I·T）

- 原题：心里翻江倒海，嘴上也只说得出一句「没事」。
- 场景拆解：主角胸口位置有一团翻涌的风暴云（半透明透视效果），脸上却平静微笑，淡淡说出一个小气泡，朋友已转身走远。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. A young person with short black hair in a mustard-yellow crewneck sweater and dark trousers smiles calmly while a translucent cutaway of their chest reveals a churning storm cloud inside, a single tiny blank speech bubble at their lips, a friend walking away in the background unaware.
```

### Q40 🛡️（计分键 I·T）

- 原题：认识再久，我也很难完全把后背交给别人。
- 场景拆解：主角和朋友之间隔着一面透明的小盾牌/半开的门，主角只把礼物从门缝递出去一半，保持礼貌的距离。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. Between a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers and a longtime friend stands a small transparent shield like a half-open door, the protagonist handing a gift only halfway through the gap, polite but guarded distance, soft tension in the composition.
```

---

## 第二部分：左右倾向题（S1–S8，左右对照分屏图）

统一构图为**左右分屏一张图**：同一主角、同一场景的两种做法，中间细分隔线。
中文场景描述中「左 / 右」对应答题时的 1 分（偏左）和 5 分（偏右）。

### S1（左 T 🤨 倾向怀疑 ／ 右 F 🙏 愿意相信）

- 左场景：陌生人递来一个「免费好礼」，主角举着放大镜仔细检查，头顶一串问号。
- 右场景：同样的陌生人递来好礼，主角笑着双手接过，头顶一朵小阳光。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. Split-screen composition with a thin divider: LEFT panel — a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers inspects a gift offered by a stranger through a magnifying glass with question marks overhead; RIGHT panel — the same character accepts the same gift with both hands and a warm trusting smile, a small sun overhead.
```

### S2（左 P 🌪️ 随性混乱 ／ 右 J 🗂️ 井然有序）

- 左场景：主角的书桌纸张乱飞、咖啡杯悬空、猫踩键盘，主角却淡定工作。
- 右场景：同一张书桌，文件盒贴好标签排成直线，主角从容工作。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. Split-screen composition with a thin divider: LEFT panel — a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers works calmly at a chaotic desk with papers flying a tilted coffee cup and a cat on the keyboard; RIGHT panel — the same character works at the same desk with labeled file boxes aligned in a perfect row, everything tidy.
```

### S3（左 N 🌌 关注整体图景 ／ 右 S 🔬 关注具体细节）

- 左场景：主角站在山顶展开一张全景地图，眺望整片山谷的轮廓。
- 右场景：主角蹲在草丛里，用显微镜观察一片叶子的脉络。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. Split-screen composition with a thin divider: LEFT panel — a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers stands on a hilltop unfolding a wide panorama map, gazing at the whole valley; RIGHT panel — the same character crouches in grass studying the veins of a single leaf through a microscope.
```

### S4（左 E ⚡ 精力外放 ／ 右 I 🍵 平和内敛）

- 左场景：主角在人群中央放电般发光，带动大家跳跃欢呼。
- 右场景：同一个傍晚，主角独自在窗边捧一杯热茶，安静微笑。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. Split-screen composition with a thin divider: LEFT panel — a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers radiates lightning-bolt energy at the center of a jumping cheering crowd; RIGHT panel — the same character sits alone by an evening window cradling a cup of hot tea with a quiet content smile.
```

### S5（左 F ❤️ 跟随内心感受 ／ 右 T 🧠 遵循理性判断）

- 左场景：岔路口，主角闭眼跟着一颗发光的心走。
- 右场景：同一个岔路口，主角跟着一颗发光的大脑走，手里还拿着对照表格。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. Split-screen composition with a thin divider: LEFT panel — at a forked path a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers walks with eyes closed following a glowing floating heart; RIGHT panel — at the same fork the same character follows a glowing floating brain while checking a comparison chart in hand.
```

### S6（左 J 🎒 提前准备 ／ 右 P 🎤 临场发挥）

- 左场景：演讲前夜，主角对照清单把资料、西装、水杯整整齐齐装好。
- 右场景：演讲开始前一分钟，主角空着手跳上台，笑着即兴开讲。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. Split-screen composition with a thin divider: LEFT panel — the night before a talk a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers packs notes an outfit and a water bottle against a checklist; RIGHT panel — one minute before the same talk the same character hops on stage empty-handed, improvising with a big grin.
```

### S7（左 S 🌞 关注当下 ／ 右 N 🔭 关注未来）

- 左场景：野餐垫上，主角专注地欣赏眼前的一朵花和便当，阳光正好。
- 右场景：同一片草地，主角用望远镜眺望远方地平线上的城市与星空。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. Split-screen composition with a thin divider: LEFT panel — on a picnic blanket a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers leans in to admire a single flower and a lunchbox in warm sunlight; RIGHT panel — on the same meadow the same character looks through a telescope at a distant city skyline and starfield on the horizon.
```

### S8（左 I 🧘 独自工作状态最佳 ／ 右 E 🤝 团队协作状态最佳）

- 左场景：安静单间里，主角独自专注工作，效率线一路飘升。
- 右场景：会议桌旁，主角和伙伴们围着白板头脑风暴，点子火花四溅。

```
Flat vector illustration, clean modern editorial style, simple geometric shapes, solid colors with subtle 10% tint shading, plain very-light background #f7f8fb, no text, no logo. Split-screen composition with a thin divider: LEFT panel — in a quiet single room a young person with short black hair in a mustard-yellow crewneck sweater and dark trousers works in deep focus with a rising flow line; RIGHT panel — the same character brainstorms with teammates around a whiteboard, idea sparks flying between everyone.
```
