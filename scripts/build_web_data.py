#!/usr/bin/env python3
"""从 references/ 与 assets/avatars/ 生成 web/data.js 与 web/avatars64.js。

data.js：题库 + 16 型文案；avatars64.js：16 张头像的 base64（供 Canvas 出图，
避免 file:// 协议下的画布污染）。改动 references/ 或头像后请重新生成。

用法：python3 scripts/build_web_data.py
"""
import base64
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SLOGANS = {
    "INTJ": "别人看见的是结果，你早在脑子里放映过结局。",
    "INTP": "白天拆解世界，晚上拆解自己。",
    "ENTJ": "世界很乱，所以你来了。",
    "ENTP": "规矩是用来商量着改的。",
    "INFJ": "你听见的沉默，比多数人的话多。",
    "INFP": "心里下着雨，手里递着伞。",
    "ENFJ": "你一开口，大家就想变成更好的人。",
    "ENFP": "快乐不是运气，是你的出厂设置。",
    "ISTJ": "世界可以没有惊喜，但不能没有你答应过的事。",
    "ISFJ": "你不说爱，但每件小事都知道。",
    "ESTJ": "混乱一看到你，就开始排队。",
    "ESFJ": "你把「热闹」两个字，过成了日常。",
    "ISTP": "话不多，手很稳，问题见你就跑。",
    "ISFP": "你把日子过成了可以收藏的画面。",
    "ESTP": "等风来，不如现在就跳。",
    "ESFP": "你在的地方，快乐自动加一。",
}

MATCHES = {
    "INTJ": "ENFP", "ENFP": "INTJ", "INFJ": "ENTP", "ENTP": "INFJ",
    "INFP": "ENFJ", "ENFJ": "INFP", "INTP": "ENTJ", "ENTJ": "INTP",
    "ISTJ": "ESFP", "ESFP": "ISTJ", "ISFJ": "ESTP", "ESTP": "ISFJ",
    "ISFP": "ESTJ", "ESTJ": "ISFP", "ISTP": "ESFJ", "ESFJ": "ISTP",
}

TAGS = {
    "INTJ": ["计划通", "大脑开十六个窗口", "人间Ctrl+S", "独处充电中", "先赢再说",
             "想太多冠军", "解释费喉咙", "看不上半成品", "验证拖延症", "微笑库存紧张"],
    "INTP": ["逻辑怪", "脑子转不停", "DDL是第一生产力", "冷笑话十级", "社恐但讲理",
             "收不了尾星人", "落地困难户", "审问式聊天", "收藏夹吃灰", "起床困难学者"],
    "ENTJ": ["天生的组长", "效率狂魔", "目标刻进DNA", "人狠话不多", "卷王本王",
             "催命式关心", "直球伤人王", "啥都自己扛", "休息有罪论", "排队绝缘体"],
    "ENTP": ["杠精本精", "点子批发商", "三分钟热度冠军", "辩论气氛组", "脑洞不限号",
             "烂尾楼楼主", "抬杠成瘾", "维护是什么梗", "热度三分钟", "专治不服"],
    "INFJ": ["人间读心术", "安静的犟种", "共情力拉满", "内耗十级学者", "理想主义钉子户",
             "憋大招专业户", "直觉背锅侠", "深度社交挑食", "表面没事人", "自我消耗隐形冠军"],
    "INFP": ["小蝴蝶本蝶", "脑内剧场24h", "温柔但有刺", "眼泪批发价", "浪漫与emo齐飞",
             "鸽子精附体", "内心戏过足", "玻璃心钢化中", "边界感欠费", "emo单曲循环"],
    "ENFJ": ["行走的太阳", "夸夸群群主", "操心的命", "氛围制造机", "先别人后自己",
             "拯救者综合症", "别人的事都归我", "答应过多症", "充电宝没自己", "热情透支户"],
    "ENFP": ["快乐小狗本狗", "人间充电宝", "新鲜感收割机", "热情三分钟", "社交恐怖分子",
             "承诺批发商", "烂尾小能手", "新鲜感瘾君子", "节奏忽高忽低", "专注困难户"],
    "ISTJ": ["靠谱本谱", "人间闹钟", "规则守门员", "计划表成精", "稳稳的幸福",
             "老办法钉子户", "风险放大镜", "惊喜排斥反应", "背锅不吭声", "新鲜事物过敏"],
    "ISFJ": ["小护士本护", "细节扫描仪", "有求必应奖", "记性好到可怕", "安静发光体",
             "老好人协会会长", "委屈收藏夹", "「不」字难出口", "自我排最后", "感谢需求饥渴"],
    "ESTJ": ["尺子姐本姐", "Deadline执法者", "效率纠察队", "安排！", "说一不二",
             "唯一正确论", "隐性困难盲区", "耐心限量供应", "急着替人决定", "变通困难症"],
    "ESFJ": ["男妈妈本妈", "群聊润滑剂", "记得你的生日", "热情永动机", "团建发起人",
             "已读不回恐慌症", "和平主义过头", "自我怀疑循环", "照顾狂魔", "分歧恐惧症"],
    "ISTP": ["电钻哥本哥", "人狠话不多", "动手派掌门", "冷静维修站", "独来独往",
             "症状灭火器", "沟通忘年交", "程序不耐烦", "长期计划是什么", "沉默是金过头"],
    "ISFP": ["小画家本家", "氛围感捕手", "慢热但细腻", "审美在线", "活在当下",
             "真实偏好保密局", "义务拖延症", "玻璃心收藏家", "沉默消化一切", "冲突回避大师"],
    "ESTP": ["墨镜哥本哥", "行动派闪电", "刺激探测器", "冲就完了", "现挂之王",
             "后果明天再说", "油门当刹车", "预案省略号", "刺激瘾君子", "三思是什么"],
    "ESFP": ["锤子姐本姐", "快乐放大器", "舞台中心区", "及时行乐代言人", "气氛组组长",
             "预算是什么梗", "长期任务遗忘症", "热闹止痛片", "独处困难户", "计划？不存在的"],
}

FIELD_MAP = {
    "一句话": "one",
    "画像": "portrait",
    "优势": "strengths",
    "容易踩的坑": "pitfalls",
    "社交": "social",
    "决策": "decision",
    "压力": "stress",
    "观察建议": "advice",
    "社区俗称": "meme",
}


def parse_profiles() -> dict:
    text = (ROOT / "references" / "type-profiles.md").read_text(encoding="utf-8")
    profiles = {}
    for m in re.finditer(r"^## ([EISNTFJP]{4}) · ([^\n]+)\n(.*?)(?=^## |\Z)", text, re.M | re.S):
        code, nick, block = m.group(1), m.group(2).strip(), m.group(3)
        entry = {"nick": nick, "tags": TAGS[code], "slogan": SLOGANS[code], "match": MATCHES[code]}
        for label, value in re.findall(r"\*\*(\S+?)：\*\*\s*(.+)", block):
            key = FIELD_MAP.get(label)
            if key:
                entry[key] = value.strip()
        missing = set(FIELD_MAP.values()) - set(entry)
        if missing:
            raise SystemExit(f"{code} 缺少字段：{sorted(missing)}")
        profiles[code] = entry
    if len(profiles) != 16:
        raise SystemExit(f"应解析出 16 个类型，实际 {len(profiles)}")
    return profiles


def main() -> None:
    bank = json.loads((ROOT / "references" / "questions.json").read_text(encoding="utf-8"))
    data = {
        "version": bank["version"],
        "source": bank["source"],
        "items": bank["items"],
        "profiles": parse_profiles(),
    }
    out = ROOT / "web" / "data.js"
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(data, ensure_ascii=False, indent=1)
    out.write_text(
        "// 本文件由 scripts/build_web_data.py 生成，请勿手改。改动 references/ 后请重新生成。\n"
        f"window.OJTS_DATA = {payload};\n",
        encoding="utf-8",
    )
    print(f"written {out} ({out.stat().st_size} bytes)")

    avatars = {}
    for img in sorted((ROOT / "assets" / "avatars").glob("*.webp")):
        b64 = base64.b64encode(img.read_bytes()).decode("ascii")
        avatars[img.stem.upper()] = f"data:image/webp;base64,{b64}"
    if len(avatars) != 16:
        raise SystemExit(f"应有 16 张头像，实际 {len(avatars)} 张，请先运行 slice_avatars.py")
    qr_path = ROOT / "assets" / "qr-web.png"
    qr64 = ""
    if qr_path.is_file():
        qr_b64 = base64.b64encode(qr_path.read_bytes()).decode("ascii")
        qr64 = f'\nwindow.OJTS_QR = "data:image/png;base64,{qr_b64}";\n'
    out64 = ROOT / "web" / "avatars64.js"
    out64.write_text(
        "// 本文件由 scripts/build_web_data.py 生成，请勿手改。头像变更后请重新生成。\n"
        f"window.OJTS_AVATARS = {json.dumps(avatars)};\n" + qr64,
        encoding="utf-8",
    )
    print(f"written {out64} ({out64.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
