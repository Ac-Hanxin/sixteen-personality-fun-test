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
    "INTJ": {
        "strengths": ["计划通", "大脑开十六个窗口", "人间Ctrl+S", "独处充电中", "先赢再说", "长线思维", "结构控", "独立判官", "系统优化师", "沉默的靠谱"],
        "flaws": ["想太多冠军", "解释费喉咙", "看不上半成品", "验证拖延症", "微笑库存紧张", "推演到地老天荒", "高冷误会制造机", "标准高到没朋友", "阶段成果鄙视链", "心里话加密通话"],
    },
    "INTP": {
        "strengths": ["逻辑怪", "脑子转不停", "DDL是第一生产力", "冷笑话十级", "社恐但讲理", "假设粉碎机", "概念建筑师", "证据更新者", "深度思考者", "安静的发明家"],
        "flaws": ["收不了尾星人", "落地困难户", "审问式聊天", "收藏夹吃灰", "起床困难学者", "分支开太多", "现实落地盲", "追问连环炮", "袜子不成对", "昼夜颠倒大师"],
    },
    "ENTJ": {
        "strengths": ["天生的组长", "效率狂魔", "目标刻进DNA", "人狠话不多", "卷王本王", "目标粉碎机", "资源磁铁", "决断快刀手", "团队发动机", "压场子专业户"],
        "flaws": ["催命式关心", "直球伤人王", "啥都自己扛", "休息有罪论", "排队绝缘体", "慢一点都不行", "温柔欠费中", "控制欲满格", "休息羞耻症", "别人节奏盲区"],
    },
    "ENTP": {
        "strengths": ["杠精本精", "点子批发商", "三分钟热度冠军", "辩论气氛组", "脑洞不限号", "反例制造机", "跨界连接王", "点子喷泉", "临场变招王", "气氛点火器"],
        "flaws": ["烂尾楼楼主", "抬杠成瘾", "维护是什么梗", "热度三分钟", "专治不服", "坑王本王", "赢了就跑型", "新鲜感奴隶", "收尾困难户", "认真就输心态"],
    },
    "INFJ": {
        "strengths": ["人间读心术", "安静的犟种", "共情力拉满", "内耗十级学者", "理想主义钉子户", "沉默观察家", "意义挖掘机", "长期主义暖炉", "信念定海针", "温柔钉子户"],
        "flaws": ["憋大招专业户", "直觉背锅侠", "深度社交挑食", "表面没事人", "自我消耗隐形冠军", "需要翻译器", "直觉型误判", "深度社恐患者", "期待值过高症", "消失式自我保护"],
    },
    "INFP": {
        "strengths": ["小蝴蝶本蝶", "脑内剧场24h", "温柔但有刺", "眼泪批发价", "浪漫与emo齐飞", "感受显微镜", "想象无边界", "真诚百分百", "价值守门员", "温柔幻想家"],
        "flaws": ["鸽子精附体", "内心戏过足", "玻璃心钢化中", "边界感欠费", "emo单曲循环", "完美主义拖延", "脑补小剧场", "一句顶一万句", "边界感迷路", "选择性失聪"],
    },
    "ENFJ": {
        "strengths": ["行走的太阳", "夸夸群群主", "操心的命", "氛围制造机", "先别人后自己", "人群充电宝", "潜力挖掘机", "组织小太阳", "共情天花板", "鼓励批发商"],
        "flaws": ["拯救者综合症", "别人的事都归我", "答应过多症", "充电宝没自己", "热情透支户", "救世主情结", "情绪超载王", "拒绝困难户", "自己排最后", "热情易耗品"],
    },
    "ENFP": {
        "strengths": ["快乐小狗本狗", "人间充电宝", "新鲜感收割机", "热情三分钟", "社交恐怖分子", "好奇永动机", "热情传染源", "连接小天才", "变化适应王", "快乐发电机"],
        "flaws": ["承诺批发商", "烂尾小能手", "新鲜感瘾君子", "节奏忽高忽低", "专注困难户", "答应太快症", "烂尾收藏家", "三分钟热度王", "日程表装饰家", "新鲜过敏症"],
    },
    "ISTJ": {
        "strengths": ["靠谱本谱", "人间闹钟", "规则守门员", "计划表成精", "稳稳的幸福", "事实核查机", "承诺兑现机", "流程定心丸", "细节保险柜", "耐心的匠人"],
        "flaws": ["老办法钉子户", "风险放大镜", "惊喜排斥反应", "背锅不吭声", "新鲜事物过敏", "老黄历忠实读者", "变化预警器", "风险显微镜", "惊喜处理宕机", "闷声扛活奖"],
    },
    "ISFJ": {
        "strengths": ["小护士本护", "细节扫描仪", "有求必应奖", "记性好到可怕", "安静发光体", "细节记忆王", "无声守护者", "后勤部部长", "温柔的城墙", "靠谱粘合剂"],
        "flaws": ["老好人协会会长", "委屈收藏夹", "「不」字难出口", "自我排最后", "感谢需求饥渴", "不好意思重症", "委屈储蓄罐", "自我隐身术", "拒绝失语症", "感谢探测器"],
    },
    "ESTJ": {
        "strengths": ["尺子姐本姐", "Deadline执法者", "效率纠察队", "安排！", "说一不二", "秩序建筑师", "执行力标杆", "时间管理员", "责任签收员", "结果质检员"],
        "flaws": ["唯一正确论", "隐性困难盲区", "耐心限量供应", "急着替人决定", "变通困难症", "唯一标准答案", "耐心缺货中", "微操控制狂", "犹豫粉碎机", "例外恐惧症"],
    },
    "ESFJ": {
        "strengths": ["男妈妈本妈", "群聊润滑剂", "记得你的生日", "热情永动机", "团建发起人", "氛围恒温器", "关系维护师", "团结小能手", "仪式感总监", "热心肠永动机"],
        "flaws": ["已读不回恐慌症", "和平主义过头", "自我怀疑循环", "照顾狂魔", "分歧恐惧症", "回复焦虑症患者", "和平鸽本鸽", "脑补小作文", "付出记账本", "冷场恐惧症"],
    },
    "ISTP": {
        "strengths": ["电钻哥本哥", "人狠话不多", "动手派掌门", "冷静维修站", "独来独往", "现场诊断师", "动手能力满级", "冷静拆弹员", "效率极简派", "独立操作员"],
        "flaws": ["症状灭火器", "沟通忘年交", "程序不耐烦", "长期计划是什么", "沉默是金过头", "沉默修理工", "计划反对派", "解释省略号", "社交省电模式", "新鲜感探测器"],
    },
    "ISFP": {
        "strengths": ["小画家本家", "氛围感捕手", "慢热但细腻", "审美在线", "活在当下", "五感收藏家", "审美雷达站", "温柔体验派", "当下生活家", "细节诗人"],
        "flaws": ["真实偏好保密局", "义务拖延症", "玻璃心收藏家", "沉默消化一切", "冲突回避大师", "真实想法内网", "明天再说协会", "敏感天线宝宝", "消失爱好者", "评价玻璃罩"],
    },
    "ESTP": {
        "strengths": ["墨镜哥本哥", "行动派闪电", "刺激探测器", "冲就完了", "现挂之王", "机会猎手", "现场指挥官", "勇气即插即用", "现实玩家", "危机拆弹专家"],
        "flaws": ["后果明天再说", "油门当刹车", "预案省略号", "刺激瘾君子", "三思是什么", "先跳再看型", "后果后议制", "等待焦虑症", "细节跳读生", "安静困难户"],
    },
    "ESFP": {
        "strengths": ["锤子姐本姐", "快乐放大器", "舞台中心区", "及时行乐代言人", "气氛组组长", "快乐供应商", "共情小太阳", "现场表演家", "温暖发电机", "真实反应王"],
        "flaws": ["预算是什么梗", "长期任务遗忘症", "热闹止痛片", "独处困难户", "计划？不存在的", "预算刺客本客", "长期任务失忆", "独处充电器欠费", "情绪遮挡器", "计划过敏症"],
    },
}

CONTRAST = {
    "INTJ": ("别人以为你高冷有距离", "其实你在家给绿植起名字"),
    "INTP": ("别人以为你什么都不在乎", "其实你凌晨三点还在想那道题"),
    "ENTJ": ("别人以为你天生强势", "其实你也会偷偷搜「如何显得亲切」"),
    "ENTP": ("别人以为你杠天杠地", "其实你只是想找人认真聊一次"),
    "INFJ": ("别人以为你温柔好说话", "其实你心里早把人分完了类"),
    "INFP": ("别人以为你安静内向", "其实你脑内正在开演唱会"),
    "ENFJ": ("别人以为你精力无限", "其实你回家只想关机躺平"),
    "ENFP": ("别人以为你社牛本牛", "其实你也需要假装上厕所透气"),
    "ISTJ": ("别人以为你古板无趣", "其实你的收藏夹比谁都精彩"),
    "ISFJ": ("别人以为你不累", "其实你只是不好意思说累"),
    "ESTJ": ("别人以为你严肃吓人", "其实你备忘录里全是可爱表情包"),
    "ESFJ": ("别人以为你社交不累", "其实你也曾在厕所隔间里回血"),
    "ISTP": ("别人以为你冷漠", "其实你帮朋友修好了三台电脑"),
    "ISFP": ("别人以为你佛系", "其实你对美挑剔得要命"),
    "ESTP": ("别人以为你吊儿郎当", "其实关键时刻你最靠得住"),
    "ESFP": ("别人以为你只会玩", "其实朋友难过时你第一个到"),
}

FORTUNE = {
    "INTJ": ("收网", "一张画满箭头的草稿纸"),
    "INTP": ("落地", "半杯冷掉的咖啡"),
    "ENTJ": ("减速带", "空出来的周日晚上"),
    "ENTP": ("收尾", "一本写完的笔记本"),
    "INFJ": ("说出口", "一个可以打扰的朋友"),
    "INFP": ("发布", "一扇能看到云的窗"),
    "ENFJ": ("自己", "一次没人找的下午"),
    "ENFP": ("完成", "一个不许改的死线"),
    "ISTJ": ("试试新", "一条没走过的下班路线"),
    "ISFJ": ("拒绝", "一句练好的「这次不行」"),
    "ESTJ": ("听听看", "一个不催的会议"),
    "ESFJ": ("等等再回", "两小时的飞行模式"),
    "ISTP": ("说一声", "一句发给同伴的进展汇报"),
    "ISFP": ("讲出来", "一个敢评价你的人"),
    "ESTP": ("停三秒", "一条安全绳"),
    "ESFP": ("空一晚", "一个没有安排的晚上"),
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
        entry = {
            "nick": nick,
            "tags": TAGS[code]["strengths"] + TAGS[code]["flaws"],
            "tags_strengths": TAGS[code]["strengths"],
            "tags_flaws": TAGS[code]["flaws"],
            "slogan": SLOGANS[code],
            "match": MATCHES[code],
            "contrast": {
                "surface": re.sub(r"^别人以为你", "", CONTRAST[code][0]),
                "truth": re.sub(r"^其实", "", CONTRAST[code][1]),
            },
            "fortune": {"kw": FORTUNE[code][0], "lucky": FORTUNE[code][1]},
        }
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
