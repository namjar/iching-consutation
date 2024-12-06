from typing import Dict, List, Tuple
from enum import Enum

class TrigramNature(Enum):
    """八卦性质枚举"""
    YANG = "阳"
    YIN = "阴"

class TrigramPosition(Enum):
    """八卦位置枚举"""
    UPPER = "上卦"
    LOWER = "下卦"

class Trigrams:
    """八卦基础类"""
    
    # 八卦基本数据
    TRIGRAM_DATA = {
        "乾": {
            "象": "天",
            "性质": TrigramNature.YANG,
            "五行": "金",
            "方位": "西北",
            "动物": "马",
            "人伦": "父",
            "身体": "头",
            "卦象": [1, 1, 1],  # 1表示阳爻，0表示阴爻
            "特性": ["刚健", "君子", "创造"],
            "含义": "刚健中正，充满活力，具有领导才能",
            "吉凶": "大吉",
            "卦德": ["元亨利贞"],
            "季节": "秋",
            "数字": 1,
            "颜色": "紫"
        },
        "兑": {
            "象": "泽",
            "性质": TrigramNature.YIN,
            "五行": "金",
            "方位": "西",
            "动物": "羊",
            "人伦": "少女",
            "身体": "口",
            "卦象": [1, 1, 0],
            "特性": ["悦乐", "喜悦", "和顺"],
            "含义": "喜悦和畅，与人和睦，具有亲和力",
            "吉凶": "吉",
            "卦德": ["亨"],
            "季节": "秋",
            "数字": 2,
            "颜色": "白"
        },
        "离": {
            "象": "火",
            "性质": TrigramNature.YIN,
            "五行": "火",
            "方位": "南",
            "动物": "雉",
            "人伦": "中女",
            "身体": "目",
            "卦象": [1, 0, 1],
            "特性": ["明丽", "文明", "丽泽"],
            "含义": "光明磊落，文明昌盛，具有智慧",
            "吉凶": "吉",
            "卦德": ["亨利贞"],
            "季节": "夏",
            "数字": 3,
            "颜色": "赤"
        },
        "震": {
            "象": "雷",
            "性质": TrigramNature.YANG,
            "五行": "木",
            "方位": "东",
            "动物": "龙",
            "人伦": "长男",
            "身体": "足",
            "卦象": [0, 0, 1],
            "特性": ["动", "起", "振发"],
            "含义": "雷厉风行，震撼奋起，具有决断力",
            "吉凶": "吉凶参半",
            "卦德": ["亨"],
            "季节": "春",
            "数字": 4,
            "颜色": "青"
        },
        "巽": {
            "象": "风",
            "性质": TrigramNature.YIN,
            "五行": "木",
            "方位": "东南",
            "动物": "鸡",
            "人伦": "长女",
            "身体": "股",
            "卦象": [1, 1, 0],
            "特性": ["入", "巽", "顺从"],
            "含义": "谦逊温和，随风潜入，具有适应性",
            "吉凶": "吉",
            "卦德": ["亨"],
            "季节": "春",
            "数字": 5,
            "颜色": "紫"
        },
        "坎": {
            "象": "水",
            "性质": TrigramNature.YANG,
            "五行": "水",
            "方位": "北",
            "动物": "豕",
            "人伦": "中男",
            "身体": "耳",
            "卦象": [0, 1, 0],
            "特性": ["陷", "险", "潜藏"],
            "含义": "险中求通，智慧深邃，具有洞察力",
            "吉凶": "凶",
            "卦德": ["亨"],
            "季节": "冬",
            "数字": 6,
            "颜色": "黑"
        },
        "艮": {
            "象": "山",
            "性质": TrigramNature.YANG,
            "五行": "土",
            "方位": "东北",
            "动物": "狗",
            "人伦": "少男",
            "身体": "手",
            "卦象": [1, 0, 0],
            "特性": ["止", "静", "安定"],
            "含义": "稳重安静，不轻举妄动，具有耐性",
            "吉凶": "吉",
            "卦德": ["亨"],
            "季节": "四季",
            "数字": 7,
            "颜色": "黄"
        },
        "坤": {
            "象": "地",
            "性质": TrigramNature.YIN,
            "五行": "土",
            "方位": "西南",
            "动物": "牛",
            "人伦": "母",
            "身体": "腹",
            "卦象": [0, 0, 0],
            "特性": ["顺", "承", "柔顺"],
            "含义": "柔顺包容，厚德载物，具有承载力",
            "吉凶": "吉",
            "卦德": ["元亨利牝马之贞"],
            "季节": "四季",
            "数字": 8,
            "颜色": "黄"
        }
    }

    # 汉字部首与五行对应关系
    RADICALS = {
        "金": {
            "金属类": ["金", "钅", "釒"],
            "器物类": ["刂", "刀", "匕", "匚", "匸", "卩", "厂", "厶", "干", "幺"],
            "坚硬类": ["石", "玉", "冂", "冖", "冫", "凵"],
            "锐利类": ["刃", "刊", "刑", "刨", "刷", "券", "刺", "劈"]
        },
        "木": {
            "植物类": ["木", "朩", "竹", "艹", "艸", "屮", "卉"],
            "生长类": ["禾", "米", "麦", "韭", "萆", "蒡", "芝"],
            "枝干类": ["条", "杆", "枝", "柄", "桠", "梗", "棍"],
            "果实类": ["果", "李", "杏", "桃", "梅", "柿", "枣"]
        },
        "水": {
            "水流类": ["水", "氵", "氺", "沝", "汆", "沪"],
            "冰雪类": ["冰", "冻", "凉", "凝", "冱"],
            "雨露类": ["雨", "雪", "霜", "露", "雲", "霞"],
            "流动类": ["永", "泳", "漾", "潺", "湍", "澜"]
        },
        "火": {
            "火光类": ["火", "灬", "炎", "焱", "熛", "燚"],
            "光明类": ["日", "旦", "旺", "昌", "明", "晶"],
            "温热类": ["炊", "烤", "煮", "炒", "烹", "煎"],
            "上升类": ["升", "昇", "焕", "炫", "烁", "煌"]
        },
        "土": {
            "土地类": ["土", "地", "坤", "垚", "堆", "塾"],
            "山岳类": ["山", "屵", "屹", "岗", "峦", "岭"],
            "建筑类": ["宀", "广", "厂", "廠", "庁", "廳"],
            "器皿类": ["皿", "盂", "盆", "盘", "碗", "鼎"]
        }
    }
    
    # 部首五行属性映射
    RADICAL_ELEMENTS = {
        # 金
        "金": "金", "钅": "金", "釒": "金", "刀": "金", "刂": "金", "匕": "金",
        "匚": "金", "匸": "金", "卩": "金", "厂": "金", "厶": "金", "干": "金",
        "幺": "金", "石": "金", "玉": "金", "冂": "金", "冖": "金", "冫": "金",
        "凵": "金",
        
        # 木
        "木": "木", "朩": "木", "竹": "木", "艹": "木", "艸": "木", "屮": "木",
        "禾": "木", "米": "木", "麦": "木", "韭": "木", "卉": "木",
        
        # 水
        "水": "水", "氵": "水", "氺": "水", "沝": "水", "汆": "水", "冰": "水",
        "雨": "水", "雪": "水", "霜": "水", "露": "水", "雲": "水", "霞": "水",
        "永": "水",
        
        # 火
        "火": "火", "灬": "火", "炎": "火", "焱": "火", "熛": "火", "燚": "火",
        "日": "火", "旦": "火", "明": "火", "晶": "火", "升": "火", "昇": "火",
        
        # 土
        "土": "土", "地": "土", "坤": "土", "垚": "土", "山": "土", "屵": "土",
        "宀": "土", "广": "土", "皿": "土"
    }

    @classmethod
    def get_trigram_attributes(cls, trigram_name: str) -> Dict:
        """获取八卦的完整属性"""
        if trigram_name not in cls.TRIGRAM_DATA:
            raise ValueError(f"Invalid trigram name: {trigram_name}")
        return cls.TRIGRAM_DATA[trigram_name]

    @classmethod
    def get_trigram_by_lines(cls, lines: List[int]) -> str:
        """根据爻线获取八卦名"""
        for name, data in cls.TRIGRAM_DATA.items():
            if data["卦象"] == lines:
                return name
        raise ValueError(f"Invalid trigram lines: {lines}")

    @classmethod
    def get_trigram_relations(cls, trigram1: str, trigram2: str) -> Dict:
        """分析两个八卦之间的关系"""
        t1 = cls.TRIGRAM_DATA[trigram1]
        t2 = cls.TRIGRAM_DATA[trigram2]
        
        relations = []
        
        # 检查五行关系
        if t1["五行"] == t2["五行"]:
            relations.append(("五行", "同行", "相生"))
        
        # 检查方位关系
        directions = ["东", "南", "西", "北"]
        d1 = t1["方位"]
        d2 = t2["方位"]
        if d1 in directions and d2 in directions:
            idx1 = directions.index(d1)
            idx2 = directions.index(d2)
            if abs(idx1 - idx2) == 2:
                relations.append(("方位", "相对", "相克"))
            elif abs(idx1 - idx2) == 1:
                relations.append(("方位", "相邻", "相生"))
        
        # 检查阴阳关系
        if t1["性质"] == t2["性质"]:
            relations.append(("阴阳", "同性", "相助"))
        else:
            relations.append(("阴阳", "异性", "相补"))
        
        return {
            "trigrams": (trigram1, trigram2),
            "relations": relations,
            "nature": "相生" if len([r for r in relations if r[2] == "相生"]) > len([r for r in relations if r[2] == "相克"]) else "相克"
        }

    @classmethod
    def get_trigram_meaning(cls, trigram: str, aspect: str = None) -> str:
        """获取八卦在特定方面的含义"""
        data = cls.TRIGRAM_DATA[trigram]
        
        if aspect is None:
            return data["含义"]
            
        aspects = {
            "事业": f"在事业方面，{trigram}卦象征着{data['特性'][0]}，建议{data['特性'][2]}",
            "感情": f"在感情方面，与{data['人伦']}之象相关，表现为{data['特性'][1]}",
            "健康": f"在健康方面，主{data['身体']}，需注意{data['特性'][0]}",
            "方向": f"在方向上，宜向{data['方位']}方",
            "时节": f"在时令上，属{data['季节']}季",
            "数字": f"在数字上，与{data['数字']}相关",
            "颜色": f"在颜色上，宜{data['颜色']}色"
        }
        
        return aspects.get(aspect, data["含义"])

    @classmethod
    def get_trigram_combinations(cls) -> List[Dict]:
        """获取所有可能的八卦组合及其关系"""
        combinations = []
        trigrams = list(cls.TRIGRAM_DATA.keys())
        
        for i in range(len(trigrams)):
            for j in range(i, len(trigrams)):
                t1 = trigrams[i]
                t2 = trigrams[j]
                relation = cls.get_trigram_relations(t1, t2)
                combinations.append({
                    "trigrams": (t1, t2),
                    "relation": relation
                })
        
        return combinations

    @classmethod
    def analyze_name_elements(cls, name: str) -> Dict:
        """分析姓名中的五行属性"""
        from collections import Counter
        
        # 获取所有部首
        radicals = []
        for char in name:
            # 这里需要一个获取汉字部首的函数，可以使用第三方库如 cnradicals
            # 暂时使用简化版本
            if char in cls.RADICAL_ELEMENTS:
                radicals.append(char)
        
        # 统计五行
        element_counts = Counter()
        for radical in radicals:
            if radical in cls.RADICAL_ELEMENTS:
                element = cls.RADICAL_ELEMENTS[radical]
                element_counts[element] += 1
        
        # 分析五行比例
        total = sum(element_counts.values()) or 1
        element_ratios = {element: count/total for element, count in element_counts.items()}
        
        # 确定主要五行
        main_element = max(element_counts.items(), key=lambda x: x[1])[0] if element_counts else None
        
        # 获取五行建议
        recommendations = []
        if main_element:
            missing_elements = set(cls.ELEMENTS) - set(element_counts.keys())
            if missing_elements:
                recommendations.append(f"可以考虑补充{', '.join(missing_elements)}的特质")
            
            # 检查五行平衡
            if len(element_counts) < 3:
                recommendations.append("五行分布较为单一，建议适当平衡")
            elif max(element_ratios.values()) > 0.5:
                recommendations.append("某一五行比重过大，可以考虑调节平衡")
        
        return {
            "radicals": radicals,
            "element_counts": dict(element_counts),
            "element_ratios": element_ratios,
            "main_element": main_element,
            "recommendations": recommendations
        }

    @classmethod
    def get_radical_meaning(cls, radical: str) -> Dict:
        """获取部首的五行属性和含义"""
        element = cls.RADICAL_ELEMENTS.get(radical)
        if not element:
            return None
            
        # 查找部首所属类别
        category = None
        for cat, rads in cls.RADICALS[element].items():
            if radical in rads:
                category = cat
                break
        
        meanings = {
            "金": {
                "金属类": "坚强、锐利",
                "器物类": "实用、工具",
                "坚硬类": "坚固、稳定",
                "锐利类": "果断、决断"
            },
            "木": {
                "植物类": "生长、向上",
                "生长类": "发展、繁荣",
                "枝干类": "支撑、延伸",
                "果实类": "成就、收获"
            },
            "水": {
                "水流类": "灵活、适应",
                "冰雪类": "清澈、纯净",
                "雨露类": "滋润、恩泽",
                "流动类": "变通、流畅"
            },
            "火": {
                "火光类": "光明、热情",
                "光明类": "智慧、明达",
                "温热类": "温暖、活力",
                "上升类": "上进、发展"
            },
            "土": {
                "土地类": "稳重、包容",
                "山岳类": "高大、巍峨",
                "建筑类": "保护、安全",
                "器皿类": "容纳、积累"
            }
        }
        
        return {
            "radical": radical,
            "element": element,
            "category": category,
            "meaning": meanings[element].get(category, "未知含义")
        }