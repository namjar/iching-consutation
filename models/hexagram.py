from typing import List, Dict, Tuple
from datetime import datetime

class Hexagram:
    def __init__(self):
        self.name: str = ""  # 本卦名
        self.changed_name: str = ""  # 变卦名
        self.lines: List[int] = []  # 爻列表
        self.changing_lines: List[int] = []  # 动爻位置
        self.time: datetime = datetime.now()  # 起卦时间
        self.topic: str = ""  # 预测主题
        self.gong: str = ""  # 所属宫
        self.original_trigrams: Tuple[str, str] = ("", "")  # 本卦上下卦
        self.changed_trigrams: Tuple[str, str] = ("", "")  # 变卦上下卦
        self.gan_zhi: List[str] = []  # 干支信息
        self.celestial_stem: str = ""  # 天干
        self.terrestrial_branch: str = ""  # 地支
        self.six_relatives: List[str] = []  # 六亲
        self.six_spirits: List[str] = []  # 六神

HEXAGRAM_DATA: Dict[str, Dict] = {
    "乾_乾": {
        "name": "乾为天",
        "meaning": "纯阳",
        "description": "元亨利贞",
        "nature": "刚健中正"
    },
    "坤_坤": {
        "name": "坤为地",
        "meaning": "纯阴",
        "description": "元亨利牝马之贞",
        "nature": "柔顺中正"
    },
    "震_乾": {
        "name": "震天雷",
        "meaning": "雷天大壮",
        "description": "利见大人",
        "nature": "刚健奋进"
    },
    "坤_震": {
        "name": "地雷复",
        "meaning": "返归复始",
        "description": "先迷后得",
        "nature": "反复无常"
    },
    "坎_乾": {
        "name": "水天需",
        "meaning": "待时而动",
        "description": "有孚光亨",
        "nature": "谦逊等待"
    },
    "乾_坎": {
        "name": "天水讼",
        "meaning": "争讼",
        "description": "有孚窒惕",
        "nature": "慎重决断"
    },
    "艮_乾": {
        "name": "山天大畜",
        "meaning": "止而不止",
        "description": "利贞不家食吉",
        "nature": "蓄养待时"
    },
    "乾_艮": {
        "name": "天山遁",
        "meaning": "遁世离俗",
        "description": "小利贞",
        "nature": "韬光养晦"
    },
    "离_乾": {
        "name": "火天大有",
        "meaning": "丰盛光明",
        "description": "元亨",
        "nature": "光明盛大"
    },
    "乾_离": {
        "name": "天火同人",
        "meaning": "上下和同",
        "description": "同人于野亨",
        "nature": "和顺共济"
    },
    "兑_乾": {
        "name": "泽天夬",
        "meaning": "决断果断",
        "description": "扬于王庭",
        "nature": "刚决果断"
    },
    "乾_兑": {
        "name": "天泽履",
        "meaning": "脚踏实地",
        "description": "履虎尾不咥人",
        "nature": "谨慎踏实"
    },
    "震_坤": {
        "name": "雷地豫",
        "meaning": "顺势而动",
        "description": "利建侯行师",
        "nature": "愉悦和顺"
    },
    "坤_巽": {
        "name": "地风升",
        "meaning": "向上提升",
        "description": "元亨用见大人",
        "nature": "谦虚上进"
    },
    "坎_坤": {
        "name": "水地比",
        "meaning": "亲近团结",
        "description": "吉原筮元永贞无咎",
        "nature": "亲和团结"
    },
    "坤_坎": {
        "name": "地水师",
        "meaning": "众众齐心",
        "description": "贞丈人吉无咎",
        "nature": "统率群众"
    },
    "艮_坤": {
        "name": "山地剥",
        "meaning": "消退衰落",
        "description": "不利有攸往",
        "nature": "消退退守"
    },
    "坤_艮": {
        "name": "地山谦",
        "meaning": "谦逊虚心",
        "description": "亨君子有终",
        "nature": "谦虚自持"
    },
    "离_坤": {
        "name": "火地晋",
        "meaning": "循序渐进",
        "description": "康侯用锡马蕃庶",
        "nature": "稳健进取"
    },
    "坤_离": {
        "name": "地火明夷",
        "meaning": "晦暗不明",
        "description": "利艰贞",
        "nature": "晦暗隐忍"
    },
    "兑_坤": {
        "name": "泽地萃",
        "meaning": "聚集会合",
        "description": "亨王假有庙",
        "nature": "汇聚和合"
    },
    "坤_兑": {
        "name": "地泽临",
        "meaning": "临下观察",
        "description": "元亨利贞",
        "nature": "观察治理"
    },
    "震_震": {
        "name": "震为雷",
        "meaning": "震动不安",
        "description": "亨",
        "nature": "警觉恐惧"
    },
    "巽_震": {
        "name": "风雷益",
        "meaning": "损上益下",
        "description": "利有攸往",
        "nature": "利益他人"
    },
    "坎_震": {
        "name": "水雷屯",
        "meaning": "起始维艰",
        "description": "元亨利贞",
        "nature": "开始困难"
    },
    "震_坎": {
        "name": "雷水解",
        "meaning": "解除束缚",
        "description": "利西南",
        "nature": "解除困境"
    },
    "艮_震": {
        "name": "山雷颐",
        "meaning": "修养自身",
        "description": "贞吉观颐",
        "nature": "修身养性"
    },
    "震_艮": {
        "name": "雷山小过",
        "meaning": "行事谨慎",
        "description": "亨利贞",
        "nature": "谨小慎微"
    },
    "离_震": {
        "name": "火雷噬嗑",
        "meaning": "决断明确",
        "description": "亨贞凶",
        "nature": "明断果决"
    },
    "震_离": {
        "name": "雷火丰",
        "meaning": "盛大丰满",
        "description": "亨小利有攸往",
        "nature": "丰盛茂盛"
    },
    "兑_震": {
        "name": "泽雷随",
        "meaning": "顺从随和",
        "description": "元亨利贞无咎",
        "nature": "谦和顺从"
    },
    "震_兑": {
        "name": "雷泽归妹",
        "meaning": "依附从属",
        "description": "征凶无攸利",
        "nature": "归依服从"
    },
    "巽_巽": {
        "name": "巽为风",
        "meaning": "谦顺随和",
        "description": "小亨利有攸往",
        "nature": "柔顺谦和"
    },
    "坎_巽": {
        "name": "水风井",
        "meaning": "循序渐进",
        "description": "改邑不改井",
        "nature": "稳健进取"
    },
    "巽_坎": {
        "name": "风水涣",
        "meaning": "分散消散",
        "description": "亨王假有庙",
        "nature": "分散疏解"
    },
    "艮_巽": {
        "name": "山风蛊",
        "meaning": "振革补弊",
        "description": "元亨利涉大川",
        "nature": "改革创新"
    },
    "巽_艮": {
        "name": "风山渐",
        "meaning": "渐进发展",
        "description": "女归吉利贞",
        "nature": "循序渐进"
    },
    "离_巽": {
        "name": "火风鼎",
        "meaning": "稳重图变",
        "description": "元吉亨",
        "nature": "革故鼎新"
    },
    "巽_离": {
        "name": "风火家人",
        "meaning": "家庭和睦",
        "description": "利女贞",
        "nature": "和睦团结"
    },
    "兑_巽": {
        "name": "泽风大过",
        "meaning": "激动过度",
        "description": "栋桡利有攸往",
        "nature": "过分激进"
    },
    "巽_兑": {
        "name": "风泽中孚",
        "meaning": "诚信感通",
        "description": "豚鱼吉利涉大川",
        "nature": "诚信感人"
    },
    "坎_坎": {
        "name": "坎为水",
        "meaning": "险难重重",
        "description": "有孚维心亨",
        "nature": "险难困厄"
    },
    "艮_坎": {
        "name": "山水蒙",
        "meaning": "蒙昧初开",
        "description": "亨匪我求童蒙",
        "nature": "启蒙教化"
    },
    "坎_艮": {
        "name": "水山蹇",
        "meaning": "险难困阻",
        "description": "利西南",
        "nature": "艰难困阻"
    },
    "离_坎": {
        "name": "火水未济",
        "meaning": "事业未成",
        "description": "亨小狐汔济",
        "nature": "未竟之象"
    },
    "坎_离": {
        "name": "水火既济",
        "meaning": "成功亨通",
        "description": "亨小利贞",
        "nature": "功成名就"
    },
    "兑_坎": {
        "name": "泽水困",
        "meaning": "困难重重",
        "description": "亨贞大人吉无咎",
        "nature": "困境求变"
    },
    "坎_兑": {
        "name": "水泽节",
        "meaning": "节制适度",
        "description": "亨苦节不可贞",
        "nature": "节制自持"
    },
    "艮_艮": {
        "name": "艮为山",
        "meaning": "止而不进",
        "description": "艮其背不获其身",
        "nature": "稳重保守"
    },
    "离_艮": {
        "name": "火山旅",
        "meaning": "短暂停留",
        "description": "小亨贞吉",
        "nature": "漂泊不定"
    },
    "艮_离": {
        "name": "山火贲",
        "meaning": "文明美化",
        "description": "亨小利有攸往",
        "nature": "装饰美化"
    },
    "兑_艮": {
        "name": "泽山咸",
        "meaning": "互相感应",
        "description": "亨利贞取女吉",
        "nature": "感应相合"
    },
    "艮_兑": {
        "name": "山泽损",
        "meaning": "损上益下",
        "description": "有孚元吉无咎",
        "nature": "损益互补"
    },
    "离_离": {
        "name": "离为火",
        "meaning": "光明显著",
        "description": "利贞亨畜牝牛吉",
        "nature": "明亮光大"
    },
    "兑_离": {
        "name": "泽火革",
        "meaning": "改革创新",
        "description": "己日乃孚元亨利贞",
        "nature": "革故鼎新"
    },
    "离_兑": {
        "name": "火泽睽",
        "meaning": "乖违背反",
        "description": "小事吉",
        "nature": "乖违孤立"
    },
    "兑_兑": {
        "name": "兑为泽",
        "meaning": "喜悦和乐",
        "description": "亨利贞",
        "nature": "愉悦欢乐"
    }
}

YAO_TEXT: Dict[str, Dict[int, str]] = {
    "乾_乾": {
        1: "潜龙勿用。",
        2: "见龙在田，利见大人。",
        3: "君子终日乾乾，夕惕若，厉无咎。",
        4: "或跃在渊，无咎。",
        5: "飞龙在天，利见大人。",
        6: "亢龙有悔。"
    },
    "坤_坤": {
        1: "履霜，坚冰至。",
        2: "直方大，不习无不利。",
        3: "含章可贞，或从王事，无成有终。",
        4: "括囊，无咎无誉。",
        5: "黄裳，元吉。",
        6: "龙战于野，其血玄黄。"
    },
    "震_坎": {
        1: "初六，磐桓，利居贞，利建侯。",
        2: "六二，屯如邅如，乘马班如。匪寇婚媾，女子贞不字，十年乃字。",
        3: "六三，即鹿无虞，惟入于林中。君子几不如舍，往吝。",
        4: "六四，乘马班如，求婚媾，往吉，无不利。",
        5: "九五，屯其膏，小贞吉，大贞凶。",
        6: "上六，乘马班如，泣血涟如。"
    },
    "坎_乾": {
        1: "初九，需于郊，利用恒，无咎。",
        2: "九二，需于沙，小有言。",
        3: "九三，需于泥，致寇至。",
        4: "六四，需于血，出自穴。",
        5: "九五，需于酒食，贞吉。",
        6: "上六，入于穴，有不速之客三人来，敬之终吉。"
    }
}