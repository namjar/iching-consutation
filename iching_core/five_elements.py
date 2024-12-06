from typing import Dict, List, Tuple
from enum import Enum

class FiveElements:
    """五行关系分析类"""
    
    # 五行基本属性
    ELEMENTS = ["金", "木", "水", "火", "土"]
    
    # 五行生克关系
    RELATIONS = {
        "生": {  # 相生关系
            "金": "水",
            "水": "木",
            "木": "火",
            "火": "土",
            "土": "金"
        },
        "克": {  # 相克关系
            "金": "木",
            "木": "土",
            "土": "水",
            "水": "火",
            "火": "金"
        },
        "泄": {  # 相泄关系
            "金": "土",
            "土": "火",
            "火": "木",
            "木": "水",
            "水": "金"
        },
        "化": {  # 相化关系
            "金": "火",
            "火": "水",
            "水": "土",
            "土": "木",
            "木": "金"
        }
    }
    
    # 五行纳甲
    NAJIA = {
        "甲": "木", "乙": "木",
        "丙": "火", "丁": "火",
        "戊": "土", "己": "土",
        "庚": "金", "辛": "金",
        "壬": "水", "癸": "水"
    }
    
    # 五行方位
    DIRECTIONS = {
        "金": "西",
        "木": "东",
        "水": "北",
        "火": "南",
        "土": "中"
    }
    
    # 五行季节
    SEASONS = {
        "金": "秋",
        "木": "春",
        "水": "冬",
        "火": "夏",
        "土": "四季"
    }
    
    # 五行颜色
    COLORS = {
        "金": "白",
        "木": "青",
        "水": "黑",
        "火": "赤",
        "土": "黄"
    }
    
    # 五行时辰
    HOURS = {
        "金": ["申", "酉"],
        "木": ["寅", "卯"],
        "水": ["子", "亥"],
        "火": ["巳", "午"],
        "土": ["辰", "戌", "丑", "未"]
    }
    
    # 五行脏腑
    ORGANS = {
        "金": ["肺", "大肠"],
        "木": ["肝", "胆"],
        "水": ["肾", "膀胱"],
        "火": ["心", "小肠"],
        "土": ["脾", "胃"]
    }
    
    # 五行情志
    EMOTIONS = {
        "金": ["悲"],
        "木": ["怒"],
        "水": ["恐"],
        "火": ["喜"],
        "土": ["思"]
    }
    
    # 五行气候
    WEATHER = {
        "金": ["燥"],
        "木": ["风"],
        "水": ["寒"],
        "火": ["热"],
        "土": ["湿"]
    }
    
    # 五行味道
    TASTES = {
        "金": "辛",
        "木": "酸",
        "水": "咸",
        "火": "苦",
        "土": "甘"
    }
    
    # 五行数字
    NUMBERS = {
        "金": [4, 9],
        "木": [3, 8],
        "水": [1, 6],
        "火": [2, 7],
        "土": [5, 10]
    }
    
    # 八卦五行属性
    TRIGRAM_ELEMENTS = {
        "乾": "金",
        "兑": "金",
        "离": "火",
        "震": "木",
        "巽": "木",
        "坎": "水",
        "艮": "土",
        "坤": "土"
    }

    def get_element_attributes(self, element: str) -> Dict:
        """获取五行的完整属性"""
        if element not in self.ELEMENTS:
            raise ValueError(f"Invalid element: {element}")
            
        return {
            "element": element,
            "direction": self.DIRECTIONS[element],
            "season": self.SEASONS[element],
            "color": self.COLORS[element],
            "hours": self.HOURS[element],
            "organs": self.ORGANS[element],
            "emotions": self.EMOTIONS[element],
            "weather": self.WEATHER[element],
            "taste": self.TASTES[element],
            "numbers": self.NUMBERS[element],
            "nature": self.get_element_nature(element)
        }

    def get_element_nature(self, element: str) -> Dict:
        """获取五行的性质和特征"""
        natures = {
            "金": {
                "性质": ["刚健", "收敛", "肃杀"],
                "特征": ["坚韧", "锐利", "清洁"],
                "物象": ["金属", "岩石", "矿物"],
                "职能": ["断绝", "决断", "取舍"]
            },
            "木": {
                "性质": ["生发", "向上", "舒展"],
                "特征": ["柔韧", "曲直", "生长"],
                "物象": ["树木", "草药", "花卉"],
                "职能": ["疏达", "条达", "升发"]
            },
            "水": {
                "性质": ["寒冷", "向下", "润泽"],
                "特征": ["柔弱", "滋润", "通达"],
                "物象": ["江河", "雨露", "泉源"],
                "职能": ["浸润", "滋养", "藏精"]
            },
            "火": {
                "性质": ["炎热", "向上", "光明"],
                "特征": ["温暖", "明亮", "活跃"],
                "物象": ["日月", "星辰", "火光"],
                "职能": ["温煦", "蒸腾", "推动"]
            },
            "土": {
                "性质": ["厚重", "中和", "承载"],
                "特征": ["稳重", "包容", "中正"],
                "物象": ["山岳", "大地", "田土"],
                "职能": ["生化", "承载", "统摄"]
            }
        }
        return natures[element]

    def get_trigram_element(self, trigram: str) -> str:
        """获取卦象的五行属性"""
        if trigram not in self.TRIGRAM_ELEMENTS:
            raise ValueError(f"Invalid trigram: {trigram}")
        return self.TRIGRAM_ELEMENTS[trigram]

    def get_element_recommendations(self, element: str) -> Dict:
        """获取五行平衡建议"""
        recommendations = {
            "金": {
                "增强": ["佩戴金属饰品", "居于西方", "食用辛味食物"],
                "环境": ["保持环境整洁", "适当通风", "减少湿度"],
                "行为": ["培养决断力", "保持纪律", "注重效率"],
                "避免": ["过度压抑", "环境混乱", "意志不坚"]
            },
            "木": {
                "增强": ["亲近自然", "食用酸味食物", "晨练"],
                "环境": ["增加绿植", "保持通风", "充足光照"],
                "行为": ["保持运动", "正面思考", "创新发展"],
                "避免": ["郁结不舒", "压抑情绪", "缺乏活动"]
            },
            "水": {
                "增强": ["亲水活动", "食用咸味食物", "充足休息"],
                "环境": ["保持安静", "适度潮湿", "柔和光线"],
                "行为": ["静心冥想", "充足睡眠", "知识积累"],
                "避免": ["过度疲劳", "环境燥热", "意志消沉"]
            },
            "火": {
                "增强": ["晒太阳", "食用苦味食物", "社交活动"],
                "环境": ["明亮光线", "温暖空间", "红色调"],
                "行为": ["保持热情", "积极交际", "乐观向上"],
                "避免": ["情绪激动", "过度兴奋", "缺乏节制"]
            },
            "土": {
                "增强": ["接地气", "食用甘味食物", "规律作息"],
                "环境": ["整洁有序", "黄色调", "稳定温度"],
                "行为": ["保持中正", "脚踏实地", "注重调和"],
                "避免": ["过度思虑", "饮食无度", "环境混乱"]
            }
        }
        return recommendations[element]

    def get_relation(self, element1: str, element2: str) -> Dict:
        """分析两个五行之间的关系"""
        if element1 not in self.ELEMENTS or element2 not in self.ELEMENTS:
            raise ValueError("Invalid elements")
            
        # 检查各种关系
        relation_type = None
        for rel_type, rel_map in self.RELATIONS.items():
            if rel_map[element1] == element2:
                relation_type = rel_type
                break
                
        # 计算关系强度
        strength = self.get_relationship_strength(element1, element2)
        
        return {
            "type": relation_type or "同类" if element1 == element2 else "异类",
            "strength": strength,
            "description": self._get_relation_description(relation_type, element1, element2),
            "favorable": relation_type in ["生", "化"] or element1 == element2
        }
        
    def analyze_relationship_cycle(self, element: str) -> Dict:
        """分析五行的完整关系循环"""
        cycles = {
            "生": [],  # 生成循环
            "克": [],  # 克制循环
            "泄": [],  # 泄气循环
            "化": []   # 转化循环
        }
        
        # 获取每种关系的完整循环
        for cycle_type in cycles.keys():
            current = element
            for _ in range(5):
                next_element = self.RELATIONS[cycle_type][current]
                cycles[cycle_type].append((current, next_element))
                current = next_element
                
        return {
            "element": element,
            "cycles": cycles,
            "analysis": self._analyze_cycles(cycles, element)
        }
        
    def get_relationship_strength(self, element1: str, element2: str) -> float:
        """计算两个五行关系的强度 (0-1)"""
        base_strength = {
            "生": 0.8,   # 相生关系基础强度
            "克": 0.6,   # 相克关系基础强度
            "泄": 0.4,   # 相泄关系基础强度
            "化": 0.7,   # 相化关系基础强度
            "同类": 1.0,  # 同类关系基础强度
            "异类": 0.3   # 异类关系基础强度
        }
        
        # 获取关系类型
        relation = self.get_relation(element1, element2)
        strength = base_strength[relation["type"]]
        
        # 根据季节调整强度
        current_season = self.SEASONS[element1]
        if current_season == self.SEASONS[element2]:
            strength *= 1.2
            
        # 根据方位调整强度
        if self.DIRECTIONS[element1] == self.DIRECTIONS[element2]:
            strength *= 1.1
            
        return min(1.0, strength)
        
    def get_relationship_recommendations(self, element1: str, element2: str) -> Dict:
        """根据五行关系提供具体建议"""
        relation = self.get_relation(element1, element2)
        
        # 基础建议模板
        base_recommendations = {
            "生": {
                "增强": ["注重滋养关系", "保持稳定供给", "建立良性循环"],
                "调节": ["适度补充", "维持平衡", "避免过度"],
                "注意": ["防止消耗过度", "关注反馈", "保持适度"]
            },
            "克": {
                "增强": ["把握适度", "建立制衡", "明确边界"],
                "调节": ["避免过激", "保持理性", "寻求平衡"],
                "注意": ["防止伤害", "注意限度", "保持克制"]
            },
            "泄": {
                "增强": ["适度释放", "保持流通", "注重转化"],
                "调节": ["控制节奏", "维持动力", "避免耗散"],
                "注意": ["防止衰竭", "保持储备", "注意补充"]
            },
            "化": {
                "增强": ["促进转化", "把握时机", "注重质变"],
                "调节": ["控制进度", "保持方向", "维持动力"],
                "注意": ["防止偏离", "注意稳定", "关注效果"]
            }
        }
        
        # 获取关系类型的具体建议
        type_recommendations = base_recommendations.get(
            relation["type"],
            {
                "增强": ["保持现状", "稳定发展", "适度调整"],
                "调节": ["维持平衡", "适度改善", "注意协调"],
                "注意": ["避免冲突", "保持距离", "寻求共识"]
            }
        )
        
        # 根据关系强度调整建议
        strength = relation["strength"]
        if strength > 0.8:
            emphasis = "当前关系强度较高，建议："
        elif strength > 0.5:
            emphasis = "当前关系强度适中，建议："
        else:
            emphasis = "当前关系强度较弱，建议："
            
        return {
            "relation_info": relation,
            "recommendations": type_recommendations,
            "emphasis": emphasis,
            "specific_actions": self._get_specific_actions(element1, element2, relation)
        }
        
    def _get_relation_description(self, relation_type: str, element1: str, element2: str) -> str:
        """获取五行关系的描述"""
        if relation_type == "生":
            return f"{element1}生{element2}，关系有利，注重滋养"
        elif relation_type == "克":
            return f"{element1}克{element2}，关系受制，需要平衡"
        elif relation_type == "泄":
            return f"{element1}泄于{element2}，关系消耗，注意补充"
        elif relation_type == "化":
            return f"{element1}化为{element2}，关系转化，把握变化"
        elif element1 == element2:
            return f"同属{element1}，关系和谐，注重稳定"
        else:
            return f"{element1}与{element2}异类，关系疏离，需要协调"
            
    def _analyze_cycles(self, cycles: Dict, element: str) -> Dict:
        """分析五行循环的特点"""
        analysis = {}
        
        for cycle_type, cycle_list in cycles.items():
            # 分析该元素在循环中的位置
            position = next(i for i, (e, _) in enumerate(cycle_list) if e == element)
            
            # 分析循环特点
            analysis[cycle_type] = {
                "position": position,
                "next_element": cycle_list[position][1],
                "cycle_length": len(cycle_list),
                "complete": cycle_list[-1][1] == cycle_list[0][0],
                "description": self._get_cycle_description(cycle_type, position)
            }
            
        return analysis
        
    def _get_cycle_description(self, cycle_type: str, position: int) -> str:
        """获取循环位置的描述"""
        descriptions = {
            "生": ["初始", "发展", "成熟", "转化", "完成"],
            "克": ["主导", "受制", "缓冲", "调节", "平衡"],
            "泄": ["储备", "释放", "消耗", "补充", "恢复"],
            "化": ["原始", "变化", "转型", "新生", "回归"]
        }
        
        return f"在{cycle_type}的循环中处于{descriptions[cycle_type][position]}阶段"
        
    def _get_specific_actions(self, element1: str, element2: str, relation: Dict) -> List[str]:
        """获取具体的行动建议"""
        actions = []
        
        # 根据关系类型提供具体行动
        if relation["type"] == "生":
            actions.extend([
                f"可以通过{self.TASTES[element1]}味食物来增强{element1}的特性",
                f"在{self.DIRECTIONS[element1]}方位活动有助于关系发展",
                f"适合在{self.SEASONS[element1]}季节采取行动"
            ])
        elif relation["type"] == "克":
            actions.extend([
                f"注意避免在{self.SEASONS[element2]}季节采取重要行动",
                f"可以用{element2}的{self.COLORS[element2]}色调来缓和关系",
                f"通过{self.get_element_recommendations(element2)['增强'][0]}来平衡关系"
            ])
        elif relation["type"] == "泄":
            actions.extend([
                f"建议在{self.DIRECTIONS[element2]}方位进行调节",
                f"可以通过{self.get_element_recommendations(element1)['增强'][0]}来维持能量",
                f"注意在{self.SEASONS[element1]}季节进行能量储备"
            ])
        else:
            actions.extend([
                f"可以选择在{self.HOURS[element1][0]}时辰行动",
                f"通过{self.get_element_recommendations(element2)['行为'][0]}来促进转化",
                f"注意调动{self.EMOTIONS[element1][0]}情志的力量"
            ])
            
        return actions