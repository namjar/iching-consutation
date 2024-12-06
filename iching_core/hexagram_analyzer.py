from typing import Dict, List, Tuple
from datetime import datetime
from models.hexagram import Hexagram, HEXAGRAM_DATA, YAO_TEXT
from iching_core.five_elements import FiveElements  # 使用绝对导入

class HexagramAnalyzer:
    """卦象分析类"""
    
    # 五行属性
    FIVE_ELEMENTS = {
        "金": ["兑", "乾"],
        "木": ["震", "巽"],
        "水": ["坎"],
        "火": ["离"],
        "土": ["坤", "艮"]
    }
    
    # 五行生克关系
    FIVE_ELEMENTS_RELATIONS = {
        "生": {
            "金": "水",
            "水": "木",
            "木": "火",
            "火": "土",
            "土": "金"
        },
        "克": {
            "金": "木",
            "木": "土",
            "土": "水",
            "水": "火",
            "火": "金"
        }
    }

    # 六亲关系
    SIX_RELATIVES = {
        "兄弟": {"description": "平等、竞争", "nature": "中性"},
        "子孙": {"description": "后代、结果", "nature": "吉"},
        "妻财": {"description": "财运、收获", "nature": "吉"},
        "官鬼": {"description": "权威、压力", "nature": "凶"},
        "父母": {"description": "长辈、助力", "nature": "吉"}
    }
    
    # 六神关系
    SIX_SPIRITS = {
        "青龙": {"nature": "吉", "attribute": "东方", "meaning": "贵人相助"},
        "朱雀": {"nature": "凶", "attribute": "南方", "meaning": "口舌是非"},
        "勾陈": {"nature": "凶", "attribute": "中央", "meaning": "疾病困扰"},
        "螣蛇": {"nature": "凶", "attribute": "北方", "meaning": "暗处危险"},
        "白虎": {"nature": "凶", "attribute": "西方", "meaning": "意外损失"},
        "玄武": {"nature": "吉", "attribute": "北方", "meaning": "贵人运"}
    }
    
    # 十神关系
    TEN_GODS = {
        "正印": {"nature": "吉", "meaning": "贵人、学习"},
        "偏印": {"nature": "凶", "meaning": "小人、暗算"},
        "正官": {"nature": "吉", "meaning": "正统、权威"},
        "七杀": {"nature": "凶", "meaning": "克制、伤害"},
        "正财": {"nature": "吉", "meaning": "正财、正当收获"},
        "偏财": {"nature": "凶", "meaning": "意外之财"},
        "食神": {"nature": "吉", "meaning": "智慧、才艺"},
        "伤官": {"nature": "凶", "meaning": "破坏、创新"},
        "比肩": {"nature": "中性", "meaning": "自身、竞争"},
        "劫财": {"nature": "凶", "meaning": "损失、破财"}
    }

    def __init__(self, hexagram: Hexagram):
        self.hexagram = hexagram
        self.hexagram_data = HEXAGRAM_DATA.get(f"{hexagram.original_trigrams[0]}_{hexagram.original_trigrams[1]}", {})
        self.yao_text = YAO_TEXT.get(f"{hexagram.original_trigrams[0]}_{hexagram.original_trigrams[1]}", {})
        self.five_elements = FiveElements()

    def generate_analysis(self) -> Dict:
        """生成完整分析报告"""
        return {
            "basic_info": self._get_basic_info(),
            "hexagram_info": self._get_hexagram_info(),
            "yao_layout": self._get_yao_layout(),
            "relationships": self._get_relationships(),
            "recommendations": self._get_recommendations()
        }

    def _get_basic_info(self) -> Dict:
        """获取基础信息"""
        return {
            "time": self.hexagram.time,
            "lunar_date": "癸卯年腊月初五",  # TODO: 实现完整的农历转换
            "gan_zhi_info": self._get_gan_zhi_info(),
            "topic": self.hexagram.topic
        }

    def _get_gan_zhi_info(self) -> str:
        """获取干支信息"""
        # TODO: 实现完整的干支计算
        return "甲子日 戊午时"

    def _get_hexagram_info(self) -> Dict:
        """获取卦象信息"""
        original_name = f"{self.hexagram_data.get('name', '')}"
        original_trigrams = f"{self.hexagram.original_trigrams[0]}下{self.hexagram.original_trigrams[1]}上"
        
        return {
            "original_hexagram_name": original_name,
            "original_trigrams": original_trigrams,
            "hexagram_text": self.hexagram_data.get("description", ""),
            "original_explanation": self.hexagram_data.get("nature", ""),
            "yao_text": self._get_yao_text(),
            "changed_hexagram_name": self._get_changed_hexagram_name(),
            "changed_trigrams": f"{self.hexagram.changed_trigrams[0]}下{self.hexagram.changed_trigrams[1]}上",
            "changed_explanation": self._get_changed_explanation()
        }

    def _get_yao_text(self) -> Dict:
        """获取爻辞"""
        result = {}
        for line_num, line in enumerate(self.hexagram.lines, start=1):
            key = f"line_{line_num}"
            text = self.yao_text.get(str(line_num), "")
            changing = line_num in self.hexagram.changing_lines
            result[key] = {
                "text": text,
                "changing": changing,
                "explanation": self._get_line_explanation(line_num, text, changing)
            }
        return result

    def _get_line_explanation(self, line_num: int, text: str, changing: bool) -> str:
        """获取爻辞解释"""
        base_explanation = f"第{line_num}爻：{text}"
        if changing:
            return f"{base_explanation}（变爻）"
        return base_explanation

    def _get_changed_hexagram_name(self) -> str:
        """获取变卦名称"""
        if not self.hexagram.changing_lines:
            return ""
        changed_key = f"{self.hexagram.changed_trigrams[0]}_{self.hexagram.changed_trigrams[1]}"
        changed_data = HEXAGRAM_DATA.get(changed_key, {})
        return changed_data.get("name", "")

    def _get_changed_explanation(self) -> str:
        """获取变卦解释"""
        if not self.hexagram.changing_lines:
            return ""
        changed_key = f"{self.hexagram.changed_trigrams[0]}_{self.hexagram.changed_trigrams[1]}"
        changed_data = HEXAGRAM_DATA.get(changed_key, {})
        return changed_data.get("nature", "")

    def _get_yao_layout(self) -> Dict:
        """获取爻位排布"""
        layout = {}
        for position, line in enumerate(self.hexagram.lines, start=1):
            layout[f"line_{position}"] = {
                "value": line,
                "changing": position in self.hexagram.changing_lines,
                "position_nature": self._get_position_nature(position),
                "element": self._get_line_element(position),
                "dynamic": self._get_line_dynamic(position, line)
            }
        
        return {
            "gong": self.hexagram.gong,
            "lines": layout,
            "shi_ying": self._get_shi_ying(),
            "dynamic_analysis": self._get_dynamic_analysis()
        }

    def _get_line_dynamic(self, position: int, line: int) -> Dict:
        """获取爻的动态特征"""
        is_changing = position in self.hexagram.changing_lines
        position_nature = self._get_position_nature(position)
        line_nature = "阳" if line == 1 else "阴"
        
        return {
            "state": "动爻" if is_changing else "静爻",
            "harmony": line_nature == position_nature.replace("位", ""),
            "strength": self._get_line_strength(position, line, is_changing)
        }

    def _get_line_strength(self, position: int, line: int, is_changing: bool) -> Dict:
        """计算爻的力量强弱"""
        base_strength = 0.5  # 基础强度
        
        # 位置加成
        if position in [3, 4]:  # 中爻
            base_strength += 0.1
        elif position in [5, 2]:  # 得中
            base_strength += 0.05
            
        # 阴阳和谐度
        position_nature = self._get_position_nature(position)
        line_nature = "阳" if line == 1 else "阴"
        if line_nature == position_nature.replace("位", ""):
            base_strength += 0.1
            
        # 动爻加成
        if is_changing:
            base_strength += 0.15
            
        return {
            "value": min(1.0, base_strength),
            "level": self._get_strength_level(base_strength),
            "description": self._get_strength_description(base_strength)
        }

    def _get_strength_level(self, strength: float) -> str:
        """获取强度等级"""
        if strength >= 0.8:
            return "极强"
        elif strength >= 0.6:
            return "较强"
        elif strength >= 0.4:
            return "中等"
        elif strength >= 0.2:
            return "较弱"
        return "极弱"

    def _get_strength_description(self, strength: float) -> str:
        """获取强度描述"""
        level = self._get_strength_level(strength)
        descriptions = {
            "极强": "具有决定性影响",
            "较强": "影响力显著",
            "中等": "影响力一般",
            "较弱": "影响力较小",
            "极弱": "影响力微弱"
        }
        return descriptions.get(level, "影响力未知")

    def _get_dynamic_analysis(self) -> Dict:
        """分析卦象整体动态"""
        changing_count = len(self.hexagram.changing_lines)
        
        if changing_count == 0:
            dynamic_level = "静卦"
            description = "整体稳定，变化较少"
        elif changing_count == 1:
            dynamic_level = "单变卦"
            description = "局部变化，整体稳定"
        elif changing_count == 2:
            dynamic_level = "双变卦"
            description = "多重变化，需要关注"
        else:
            dynamic_level = "多变卦"
            description = "变化剧烈，需要谨慎"
            
        return {
            "level": dynamic_level,
            "count": changing_count,
            "description": description,
            "advice": self._get_dynamic_advice(changing_count)
        }

    def _get_dynamic_advice(self, changing_count: int) -> List[str]:
        """根据动态获取建议"""
        if changing_count == 0:
            return [
                "保持现有策略",
                "稳步推进计划",
                "注意长期发展"
            ]
        elif changing_count == 1:
            return [
                "关注变化方向",
                "适度调整策略",
                "把握关键时机"
            ]
        elif changing_count == 2:
            return [
                "制定应对预案",
                "做好充分准备",
                "注意风险控制"
            ]
        else:
            return [
                "谨慎决策行动",
                "加强风险管理",
                "寻求稳定支持"
            ]

    def _get_relationships(self) -> Dict:
        """获取关系分析"""
        return {
            "shi_yao": self._analyze_shi_yao(),
            "ying_yao": self._analyze_ying_yao(),
            "liu_qin": self._analyze_liu_qin(),
            "wu_xing": self._analyze_wu_xing(),
            "shi_shen": self._analyze_shi_shen()
        }

    def _get_recommendations(self) -> Dict:
        """获取建议"""
        return {
            "short_term": self._get_short_term_advice(),
            "medium_term": self._get_medium_term_advice(),
            "long_term": self._get_long_term_advice(),
            "risks": self._get_risk_advice()
        }

    def analyze_five_elements(self) -> Dict:
        """分析卦象的五行属性和关系"""
        upper_trigram = self.hexagram.upper_trigram
        lower_trigram = self.hexagram.lower_trigram
        upper_element = self._get_element(upper_trigram)
        lower_element = self._get_element(lower_trigram)

        # 获取卦的时间五行
        time_element = self.five_elements.NAJIA[self.hexagram.celestial_stem]
        
        # 分析五行关系强弱
        element_strength = self._analyze_element_strength(upper_element, lower_element, time_element)
        
        # 分析五行相生相克关系
        relationships = self._analyze_element_relationships(upper_element, lower_element, time_element)
        
        # 分析五行旺衰
        seasonal_influence = self._analyze_seasonal_influence(time_element)
        
        return {
            "upper_trigram": {
                "trigram": upper_trigram,
                "element": upper_element,
                "attributes": self.five_elements.get_element_attributes(upper_element)
            },
            "lower_trigram": {
                "trigram": lower_trigram,
                "element": lower_element,
                "attributes": self.five_elements.get_element_attributes(lower_element)
            },
            "time_element": {
                "element": time_element,
                "attributes": self.five_elements.get_element_attributes(time_element)
            },
            "strength_analysis": element_strength,
            "relationships": relationships,
            "seasonal_influence": seasonal_influence,
            "overall_element_status": self._get_overall_element_status(
                element_strength,
                relationships,
                seasonal_influence
            )
        }

    def analyze_changing_lines(self) -> List[Dict]:
        """分析动爻的含义和影响"""
        results = []
        for line_pos in self.hexagram.changing_lines:
            line_analysis = {
                "position": line_pos + 1,  # 爻位（1-6）
                "original_value": self.hexagram.lines[line_pos],
                "changed_value": 1 - self.hexagram.lines[line_pos],
                "six_relative": self.hexagram.six_relatives[line_pos],
                "six_spirit": self.hexagram.six_spirits[line_pos],
                "significance": self._analyze_line_significance(line_pos)
            }
            results.append(line_analysis)
        return results

    def analyze_six_relatives(self) -> List[Dict]:
        """分析六亲关系"""
        results = []
        for position, relative in enumerate(self.hexagram.six_relatives):
            result = {
                "position": position + 1,
                "relative": relative,
                "info": self.SIX_RELATIVES[relative],
                "is_changing": position in self.hexagram.changing_lines
            }
            results.append(result)
        return results

    def analyze_six_spirits(self) -> List[Dict]:
        """分析六神关系"""
        results = []
        for position, spirit in enumerate(self.hexagram.six_spirits):
            result = {
                "position": position + 1,
                "spirit": spirit,
                "info": self.SIX_SPIRITS[spirit],
                "is_changing": position in self.hexagram.changing_lines
            }
            results.append(result)
        return results

    def analyze_ten_gods(self) -> Dict:
        """分析十神关系"""
        stem = self.hexagram.celestial_stem
        branch = self.hexagram.terrestrial_branch
        
        # 根据天干确定日主
        day_master = self.five_elements.NAJIA[stem]
        
        # 分析每个爻位的十神关系
        results = []
        for position, line in enumerate(self.hexagram.lines):
            # 根据爻的阴阳和五行确定十神
            line_element = self._get_line_element(position)
            god = self._determine_ten_god(day_master, line_element, line == 1)
            
            result = {
                "position": position + 1,
                "god": god,
                "info": self.TEN_GODS[god],
                "is_changing": position in self.hexagram.changing_lines
            }
            results.append(result)
            
        return {
            "day_master": day_master,
            "positions": results
        }

    def analyze_najia_relationships(self, context_type: str = "general") -> Dict:
        """分析六爻纳甲关系
        
        Args:
            context_type: 分析场景类型，可选值：
                - general: 通用分析
                - career: 事业
                - relationship: 感情
                - health: 健康
                - wealth: 财运
        """
        # 获取世应爻位置
        shi_yao = self._get_shi_yao_position()
        ying_yao = self._get_ying_yao_position()
        
        # 获取本卦和变卦信息
        original_lines = self.hexagram.lines
        changing_positions = self.hexagram.changing_lines
        changed_lines = original_lines.copy()
        for pos in changing_positions:
            changed_lines[pos] = 1 if original_lines[pos] == 0 else 0
            
        # 分析世应爻关系
        shi_ying_relation = self._analyze_shi_ying_relation(
            shi_yao,
            ying_yao,
            original_lines,
            context_type
        )
        
        # 分析六亲关系
        liuqin_relations = self._analyze_liuqin_relations(
            original_lines,
            changed_lines,
            context_type
        )
        
        # 分析十神关系
        shishen_relations = self._analyze_shishen_relations(
            original_lines,
            changed_lines,
            context_type
        )
        
        # 生成综合分析
        comprehensive_analysis = self._generate_najia_analysis(
            shi_ying_relation,
            liuqin_relations,
            shishen_relations,
            context_type
        )
        
        return {
            "shi_ying_relation": shi_ying_relation,
            "liuqin_relations": liuqin_relations,
            "shishen_relations": shishen_relations,
            "comprehensive_analysis": comprehensive_analysis
        }

    def _get_shi_yao_position(self) -> int:
        """获取世爻位置"""
        # 根据卦宫和动静来确定世爻
        # 此处需要补充具体的世爻判断逻辑
        return 0  # 临时返回值

    def _get_ying_yao_position(self) -> int:
        """获取应爻位置"""
        # 应爻与世爻相对
        shi_yao = self._get_shi_yao_position()
        return 5 - shi_yao

    def _analyze_shi_ying_relation(self, shi_yao: int, ying_yao: int, 
                                 lines: List[int], context_type: str) -> Dict:
        """分析世应爻关系"""
        # 基本关系判断
        basic_relation = self._get_yao_relation(
            lines[shi_yao],
            lines[ying_yao]
        )
        
        # 获取世应爻五行属性
        shi_element = self._get_yao_element(shi_yao, lines[shi_yao])
        ying_element = self._get_yao_element(ying_yao, lines[ying_yao])
        
        # 分析五行关系
        element_relation = self._analyze_element_relation(
            shi_element,
            ying_element
        )
        
        # 根据场景调整关系解释
        context_meaning = self._get_context_specific_meaning(
            basic_relation,
            element_relation,
            context_type
        )
        
        return {
            "basic_relation": basic_relation,
            "element_relation": element_relation,
            "context_meaning": context_meaning,
            "strength": self._calculate_relation_strength(
                basic_relation,
                element_relation
            )
        }

    def _analyze_liuqin_relations(self, original: List[int], 
                                changed: List[int], context_type: str) -> List[Dict]:
        """分析六亲关系"""
        relations = []
        
        # 六亲属性定义
        liuqin_types = {
            "兄弟": {"career": "竞争对手", "relationship": "情敌", "health": "免疫系统", "wealth": "合作伙伴"},
            "子孙": {"career": "技能成果", "relationship": "感情结果", "health": "恢复能力", "wealth": "收益"},
            "官鬼": {"career": "上级领导", "relationship": "另一半", "health": "疾病", "wealth": "机遇"},
            "父母": {"career": "资源支持", "relationship": "长辈建议", "health": "调养", "wealth": "本金"},
            "妻财": {"career": "报酬收入", "relationship": "感情付出", "health": "营养", "wealth": "财源"}
        }
        
        for pos in range(6):
            # 获取该爻的六亲属性
            liuqin = self._get_liuqin_type(pos, original[pos])
            
            # 分析原卦与变卦的关系
            if pos in self.hexagram.changing_lines:
                change_relation = self._analyze_change_relation(
                    original[pos],
                    changed[pos],
                    liuqin
                )
            else:
                change_relation = None
            
            # 获取场景特定含义
            context_meaning = liuqin_types.get(liuqin, {}).get(context_type, "未知")
            
            relations.append({
                "position": pos,
                "liuqin": liuqin,
                "context_meaning": context_meaning,
                "change_relation": change_relation,
                "significance": self._get_position_significance(pos)
            })
            
        return relations

    def _analyze_shishen_relations(self, original: List[int], 
                                 changed: List[int], context_type: str) -> List[Dict]:
        """分析十神关系"""
        relations = []
        
        # 十神属性定义
        shishen_types = {
            "正官": {
                "career": "正统权威",
                "relationship": "正缘",
                "health": "正规治疗",
                "wealth": "正当收入"
            },
            "七杀": {
                "career": "竞争压力",
                "relationship": "暧昧对象",
                "health": "急性病症",
                "wealth": "意外收入"
            },
            "正印": {
                "career": "学习提升",
                "relationship": "精神契合",
                "health": "调养",
                "wealth": "稳定增长"
            },
            "偏印": {
                "career": "技能特长",
                "relationship": "精神寄托",
                "health": "保健",
                "wealth": "潜在收益"
            },
            "比肩": {
                "career": "同事",
                "relationship": "朋友",
                "health": "体魄",
                "wealth": "共同发展"
            },
            "劫财": {
                "career": "竞争",
                "relationship": "干扰",
                "health": "隐患",
                "wealth": "消耗"
            },
            "伤官": {
                "career": "创新能力",
                "relationship": "浪漫情怀",
                "health": "亚健康",
                "wealth": "投机"
            },
            "食神": {
                "career": "才能",
                "relationship": "愉悦",
                "health": "养生",
                "wealth": "生财之道"
            },
            "正财": {
                "career": "正当利益",
                "relationship": "真诚",
                "health": "营养",
                "wealth": "固定收入"
            },
            "偏财": {
                "career": "额外收益",
                "relationship": "暧昧",
                "health": "补充",
                "wealth": "机会"
            }
        }
        
        for pos in range(6):
            # 获取该爻的十神属性
            shishen = self._get_shishen_type(pos, original[pos])
            
            # 分析原卦与变卦的关系
            if pos in self.hexagram.changing_lines:
                change_relation = self._analyze_change_relation(
                    original[pos],
                    changed[pos],
                    shishen
                )
            else:
                change_relation = None
            
            # 获取场景特定含义
            context_meaning = shishen_types.get(shishen, {}).get(context_type, "未知")
            
            relations.append({
                "position": pos,
                "shishen": shishen,
                "context_meaning": context_meaning,
                "change_relation": change_relation,
                "significance": self._get_position_significance(pos)
            })
            
        return relations

    def _generate_najia_analysis(self, shi_ying: Dict, liuqin: List[Dict],
                               shishen: List[Dict], context_type: str) -> Dict:
        """生成纳甲综合分析"""
        # 分析世应关系的影响
        shi_ying_impact = self._analyze_shi_ying_impact(shi_ying, context_type)
        
        # 分析六亲关系的整体态势
        liuqin_trend = self._analyze_liuqin_trend(liuqin, context_type)
        
        # 分析十神关系的关键指向
        shishen_indication = self._analyze_shishen_indication(shishen, context_type)
        
        # 生成具体建议
        recommendations = self._generate_najia_recommendations(
            shi_ying_impact,
            liuqin_trend,
            shishen_indication,
            context_type
        )
        
        return {
            "shi_ying_impact": shi_ying_impact,
            "liuqin_trend": liuqin_trend,
            "shishen_indication": shishen_indication,
            "recommendations": recommendations
        }

    def _analyze_shi_ying_impact(self, shi_ying: Dict, context_type: str) -> Dict:
        """分析世应关系的影响"""
        # 基于关系强度和场景特点评估影响
        strength = shi_ying["strength"]
        context_meaning = shi_ying["context_meaning"]
        
        if strength > 0.8:
            impact_level = "强烈"
            suggestion = "积极把握机会" if context_meaning["favorable"] else "谨慎应对"
        elif strength > 0.5:
            impact_level = "中等"
            suggestion = "稳步推进" if context_meaning["favorable"] else "防范风险"
        else:
            impact_level = "微弱"
            suggestion = "等待时机" if context_meaning["favorable"] else "暂时观望"
            
        return {
            "level": impact_level,
            "nature": context_meaning["nature"],
            "suggestion": suggestion
        }

    def _analyze_liuqin_trend(self, liuqin: List[Dict], context_type: str) -> Dict:
        """分析六亲关系的整体态势"""
        # 统计各类六亲的影响
        influence_stats = {}
        for relation in liuqin:
            liuqin_type = relation["liuqin"]
            significance = relation["significance"]
            
            if liuqin_type not in influence_stats:
                influence_stats[liuqin_type] = 0
            influence_stats[liuqin_type] += significance
            
        # 找出主要影响力量
        main_influences = sorted(
            influence_stats.items(),
            key=lambda x: x[1],
            reverse=True
        )[:2]
        
        return {
            "main_influences": main_influences,
            "trend_description": self._get_liuqin_trend_description(
                main_influences,
                context_type
            )
        }

    def _analyze_shishen_indication(self, shishen: List[Dict], context_type: str) -> Dict:
        """分析十神关系的关键指向"""
        # 统计各类十神的影响
        influence_stats = {}
        for relation in shishen:
            shishen_type = relation["shishen"]
            significance = relation["significance"]
            
            if shishen_type not in influence_stats:
                influence_stats[shishen_type] = 0
            influence_stats[shishen_type] += significance
            
        # 找出关键指向
        key_indications = sorted(
            influence_stats.items(),
            key=lambda x: x[1],
            reverse=True
        )[:2]
        
        return {
            "key_indications": key_indications,
            "indication_meaning": self._get_shishen_indication_meaning(
                key_indications,
                context_type
            )
        }

    def _generate_najia_recommendations(self, shi_ying_impact: Dict,
                                      liuqin_trend: Dict,
                                      shishen_indication: Dict,
                                      context_type: str) -> List[str]:
        """生成纳甲分析建议"""
        recommendations = []
        
        # 基于世应关系的建议
        recommendations.append(
            f"根据世应关系：{shi_ying_impact['suggestion']}"
        )
        
        # 基于六亲趋势的建议
        recommendations.append(
            f"整体趋势：{liuqin_trend['trend_description']}"
        )
        
        # 基于十神指向的建议
        recommendations.append(
            f"关键指向：{shishen_indication['indication_meaning']}"
        )
        
        # 添加场景特定建议
        context_specific = self._get_context_specific_recommendations(
            context_type,
            shi_ying_impact,
            liuqin_trend,
            shishen_indication
        )
        recommendations.extend(context_specific)
        
        return recommendations

    def _get_element(self, trigram: str) -> str:
        """获取卦象的五行属性"""
        for element, trigrams in self.FIVE_ELEMENTS.items():
            if trigram in trigrams:
                return element
        return "土"  # 默认属土

    def _analyze_element_strength(self, upper: str, lower: str, time: str) -> Dict:
        """分析五行力量强弱"""
        elements_count = {element: 0 for element in self.five_elements.ELEMENTS}
        elements_count[upper] += 2  # 上卦权重为2
        elements_count[lower] += 2  # 下卦权重为2
        elements_count[time] += 1   # 时间五行权重为1
        
        # 计算最强和最弱的五行
        max_count = max(elements_count.values())
        min_count = min(elements_count.values())
        
        strongest = [e for e, c in elements_count.items() if c == max_count]
        weakest = [e for e, c in elements_count.items() if c == min_count]
        
        return {
            "element_counts": elements_count,
            "strongest_elements": strongest,
            "weakest_elements": weakest,
            "balance_score": self._calculate_balance_score(elements_count)
        }

    def _analyze_element_relationships(self, upper: str, lower: str, time: str) -> Dict:
        """分析五行相生相克关系"""
        relationships = []
        
        # 分析上下卦关系
        upper_lower_relation = self.five_elements.get_relation(upper, lower)
        relationships.append({
            "elements": (upper, lower),
            "type": "上下卦",
            "relation": upper_lower_relation
        })
        
        # 分析与时间五行的关系
        time_upper_relation = self.five_elements.get_relation(time, upper)
        time_lower_relation = self.five_elements.get_relation(time, lower)
        relationships.extend([
            {
                "elements": (time, upper),
                "type": "时势上卦",
                "relation": time_upper_relation
            },
            {
                "elements": (time, lower),
                "type": "时势下卦",
                "relation": time_lower_relation
            }
        ])
        
        # 计算整体关系倾向
        relationship_scores = {
            "生": 0,
            "克": 0,
            "泄": 0,
            "化": 0
        }
        
        for rel in relationships:
            rel_type = rel["relation"]["type"]
            if rel_type in relationship_scores:
                relationship_scores[rel_type] += 1
        
        return {
            "detailed_relationships": relationships,
            "relationship_scores": relationship_scores,
            "dominant_relationship": max(relationship_scores.items(), key=lambda x: x[1])[0]
        }

    def _analyze_seasonal_influence(self, time_element: str) -> Dict:
        """分析五行的季节性影响"""
        current_season = self._get_current_season()
        season_element = {
            "春": "木",
            "夏": "火",
            "秋": "金",
            "冬": "水",
            "四季": "土"
        }[current_season]
        
        seasonal_relation = self.five_elements.get_relation(season_element, time_element)
        
        return {
            "current_season": current_season,
            "season_element": season_element,
            "time_element": time_element,
            "seasonal_relation": seasonal_relation,
            "is_seasonally_favorable": seasonal_relation["type"] in ["生", "化"]
        }

    def _calculate_balance_score(self, element_counts: Dict[str, int]) -> float:
        """计算五行平衡度分数 (0-1)"""
        total = sum(element_counts.values())
        expected = total / 5  # 理想情况下每个元素的数量
        
        # 计算方差
        variance = sum((count - expected) ** 2 for count in element_counts.values()) / 5
        
        # 将方差转换为0-1的分数，0表示完全不平衡，1表示完全平衡
        max_possible_variance = expected ** 2  # 最大可能的方差
        balance_score = 1 - (variance / max_possible_variance)
        
        return round(balance_score, 2)

    def _get_current_season(self) -> str:
        """根据当前月份获取季节"""
        month = self.hexagram.time.month
        if month in [3, 4, 5]:
            return "春"
        elif month in [6, 7, 8]:
            return "夏"
        elif month in [9, 10, 11]:
            return "秋"
        else:
            return "冬"

    def _get_overall_element_status(self, strength: Dict, relationships: Dict, seasonal: Dict) -> Dict:
        """综合分析五行状态"""
        # 计算整体有利度分数 (0-100)
        favorable_score = 0
        
        # 考虑五行平衡度 (30分)
        favorable_score += strength["balance_score"] * 30
        
        # 考虑相生相克关系 (40分)
        relationship_scores = relationships["relationship_scores"]
        total_relationships = sum(relationship_scores.values())
        if total_relationships > 0:
            favorable_ratio = (relationship_scores["生"] + relationship_scores["化"]) / total_relationships
            favorable_score += favorable_ratio * 40
        
        # 考虑季节影响 (30分)
        if seasonal["is_seasonally_favorable"]:
            favorable_score += 30
            
        return {
            "favorable_score": round(favorable_score, 1),
            "status_level": self._get_status_level(favorable_score),
            "primary_recommendations": self._get_recommendations(
                strength["weakest_elements"],
                relationships["dominant_relationship"],
                seasonal["is_seasonally_favorable"]
            )
        }

    def _get_status_level(self, score: float) -> str:
        """根据分数获取状态等级"""
        if score >= 80:
            return "极佳"
        elif score >= 60:
            return "良好"
        elif score >= 40:
            return "一般"
        elif score >= 20:
            return "欠佳"
        else:
            return "不利"

    def _get_recommendations(self, weak_elements: List[str], dominant_relation: str, seasonal_favorable: bool) -> List[str]:
        """生成五行调节建议"""
        recommendations = []
        
        # 基于薄弱五行的建议
        for element in weak_elements:
            recommendations.append(f"可以通过增强{element}的特质来改善状态")
        
        # 基于主导关系的建议
        if dominant_relation == "克":
            recommendations.append("需要注意化解冲突，避免对抗")
        elif dominant_relation == "泄":
            recommendations.append("注意节制，避免过度消耗")
        
        # 基于季节影响的建议
        if not seasonal_favorable:
            recommendations.append("当前季节特性不利，建议顺应时势，稳健行事")
        
        return recommendations

    def _analyze_line_significance(self, position: int) -> str:
        """分析爻位的重要性"""
        significances = [
            "初爻，代表开始阶段",
            "二爻，代表发展阶段",
            "三爻，代表转折阶段",
            "四爻，代表近结果",
            "五爻，代表结果",
            "上爻，代表结束"
        ]
        return significances[position]

    def _get_line_element(self, position: int) -> str:
        """获取爻位的五行属性"""
        trigram = self.TRIGRAMS[tuple(self.hexagram.lines[position:position+3])]
        return self.five_elements.get_trigram_element(trigram)

    def _determine_ten_god(self, day_master: str, line_element: str, is_yang: bool) -> str:
        """确定十神关系"""
        relation = self.five_elements.get_relation(day_master, line_element)
        
        # 根据五行关系和阴阳确定十神
        if relation["type"] == "生":
            return "正印" if is_yang else "偏印"
        elif relation["type"] == "克":
            return "正官" if is_yang else "七杀"
        elif relation["type"] == "泄":
            return "正财" if is_yang else "偏财"
        elif relation["type"] == "化":
            return "食神" if is_yang else "伤官"
        else:  # 同类
            return "比肩" if is_yang else "劫财"

    def _get_overall_judgment(self) -> str:
        """获取总体判断"""
        # 基于卦象特性和动爻情况给出整体判断
        judgment = f"{self.hexagram_data.get('name')}卦："
        judgment += self.hexagram_data.get('description', '')
        
        if not self.hexagram.changing_lines:
            judgment += "，无变爻，保持现状为宜。"
        else:
            judgment += f"，有{len(self.hexagram.changing_lines)}个变爻，"
            judgment += "需要注意变化和调整。"
        
        return judgment

    def get_comprehensive_analysis(self) -> Dict:
        """获取全面的卦象分析"""
        return {
            "basic_info": {
                "name": self.hexagram_data.get("name"),
                "meaning": self.hexagram_data.get("meaning"),
                "nature": self.hexagram_data.get("nature"),
                "description": self.hexagram_data.get("description")
            },
            "time_info": {
                "datetime": self.hexagram.time.isoformat(),
                "celestial_stem": self.hexagram.celestial_stem,
                "terrestrial_branch": self.hexagram.terrestrial_branch
            },
            "five_elements": self.analyze_five_elements(),
            "six_relatives": self.analyze_six_relatives(),
            "six_spirits": self.analyze_six_spirits(),
            "ten_gods": self.analyze_ten_gods(),
            "changing_lines": self.analyze_changing_lines(),
            "overall_judgment": self._get_overall_judgment()
        }

    def analyze_hexagram_changes(self) -> Dict:
        """分析卦象变化的完整信息"""
        # 获取原卦和变卦信息
        original_lines = self.hexagram.lines
        changing_positions = self.hexagram.changing_lines
        changed_lines = original_lines.copy()
        for pos in changing_positions:
            changed_lines[pos] = 1 if original_lines[pos] == 0 else 0

        # 分析变化的性质
        change_nature = self._analyze_change_nature(original_lines, changed_lines, changing_positions)
        
        # 分析变化的影响
        change_impact = self._analyze_change_impact(changing_positions)
        
        # 分析变化的时序
        temporal_analysis = self._analyze_temporal_sequence(changing_positions)
        
        # 分析卦象转化的意义
        transformation_meaning = self._analyze_transformation_meaning(
            original_lines, 
            changed_lines,
            changing_positions
        )
        
        # 生成变化建议
        recommendations = self._generate_change_recommendations(
            change_nature,
            change_impact,
            temporal_analysis
        )
        
        return {
            "change_nature": change_nature,
            "change_impact": change_impact,
            "temporal_analysis": temporal_analysis,
            "transformation_meaning": transformation_meaning,
            "recommendations": recommendations
        }

    def _analyze_change_nature(self, original: List[int], changed: List[int], positions: List[int]) -> Dict:
        """分析变化的本质特征"""
        # 变化的数量特征
        change_count = len(positions)
        
        # 变化的方向（阴阳转化）
        yin_to_yang = sum(1 for pos in positions if original[pos] == 0)
        yang_to_yin = len(positions) - yin_to_yang
        
        # 变化的位置特征
        position_nature = {
            0: "初爻",
            1: "二爻",
            2: "三爻",
            3: "四爻",
            4: "五爻",
            5: "上爻"
        }
        
        # 变化的结构特征
        structure_changes = {
            "下卦变化": len([p for p in positions if p < 3]),
            "上卦变化": len([p for p in positions if p >= 3]),
            "内卦变化": len([p for p in positions if 1 <= p <= 4]),
            "外卦变化": len([p for p in positions if p in (0, 5)])
        }
        
        # 判断变化的主导性质
        if change_count == 0:
            change_type = "无变爻"
        elif change_count == 1:
            change_type = "单爻变"
        elif change_count == 2:
            change_type = "双爻变"
        elif change_count == 3:
            change_type = "三爻变"
        else:
            change_type = "多爻变"
            
        return {
            "change_count": change_count,
            "change_type": change_type,
            "yin_yang_transformation": {
                "yin_to_yang": yin_to_yang,
                "yang_to_yin": yang_to_yin,
                "dominant_direction": "阴转阳" if yin_to_yang > yang_to_yin else "阳转阴" if yang_to_yin > yin_to_yang else "平衡"
            },
            "changing_positions": [position_nature[pos] for pos in positions],
            "structure_changes": structure_changes,
            "change_intensity": self._calculate_change_intensity(change_count, positions)
        }

    def _analyze_change_impact(self, positions: List[int]) -> Dict:
        """分析变化的影响范围和程度"""
        # 定义爻位的基本属性
        position_attributes = {
            0: {"domain": "基础", "influence": "开始", "aspect": "动机"},
            1: {"domain": "内在", "influence": "发展", "aspect": "准备"},
            2: {"domain": "内核", "influence": "执行", "aspect": "行动"},
            3: {"domain": "外显", "influence": "表现", "aspect": "形式"},
            4: {"domain": "外在", "influence": "环境", "aspect": "地位"},
            5: {"domain": "终极", "influence": "结果", "aspect": "目标"}
        }
        
        # 分析每个变爻的影响
        position_impacts = []
        for pos in positions:
            attr = position_attributes[pos]
            impact = {
                "position": pos,
                "domain": attr["domain"],
                "influence": attr["influence"],
                "aspect": attr["aspect"],
                "significance": self._get_position_significance(pos)
            }
            position_impacts.append(impact)
        
        # 计算整体影响
        overall_impact = {
            "scope": self._calculate_impact_scope(positions),
            "intensity": self._calculate_impact_intensity(positions),
            "duration": self._calculate_impact_duration(positions),
            "primary_domains": [impact["domain"] for impact in position_impacts],
            "key_aspects": [impact["aspect"] for impact in position_impacts]
        }
        
        return {
            "position_impacts": position_impacts,
            "overall_impact": overall_impact
        }

    def _analyze_temporal_sequence(self, positions: List[int]) -> Dict:
        """分析变化的时序特征"""
        # 时间属性定义
        temporal_attributes = {
            0: {"phase": "初始", "timing": "开始", "duration": "短期"},
            1: {"phase": "发展", "timing": "渐进", "duration": "短中期"},
            2: {"phase": "成长", "timing": "发展", "duration": "中期"},
            3: {"phase": "转化", "timing": "变化", "duration": "中长期"},
            4: {"phase": "成熟", "timing": "稳定", "duration": "长期"},
            5: {"phase": "终结", "timing": "完成", "duration": "最终"}
        }
        
        # 分析变化序列
        sequence = []
        for pos in sorted(positions):
            attr = temporal_attributes[pos]
            sequence.append({
                "position": pos,
                "phase": attr["phase"],
                "timing": attr["timing"],
                "duration": attr["duration"]
            })
        
        # 确定主要时间特征
        primary_phase = sequence[0]["phase"] if sequence else None
        final_phase = sequence[-1]["phase"] if sequence else None
        
        return {
            "sequence": sequence,
            "temporal_span": {
                "start": primary_phase,
                "end": final_phase,
                "duration": self._calculate_temporal_span(positions)
            },
            "development_pattern": self._analyze_development_pattern(positions),
            "timing_suggestions": self._generate_timing_suggestions(positions)
        }

    def _analyze_transformation_meaning(self, original: List[int], changed: List[int], positions: List[int]) -> Dict:
        """分析卦象转化的深层含义"""
        # 获取原卦和变卦的基本属性
        original_attributes = self._get_hexagram_attributes(original)
        changed_attributes = self._get_hexagram_attributes(changed)
        
        # 分析转化的核心意义
        core_transformation = self._analyze_core_transformation(
            original_attributes,
            changed_attributes
        )
        
        # 分析具体领域的变化
        domain_changes = self._analyze_domain_changes(
            original_attributes,
            changed_attributes,
            positions
        )
        
        return {
            "core_transformation": core_transformation,
            "domain_changes": domain_changes,
            "transformation_nature": self._get_transformation_nature(
                original_attributes,
                changed_attributes
            ),
            "key_implications": self._get_key_implications(
                core_transformation,
                domain_changes
            )
        }

    def _generate_change_recommendations(self, nature: Dict, impact: Dict, temporal: Dict) -> List[str]:
        """生成变化相关的具体建议"""
        recommendations = []
        
        # 基于变化性质的建议
        if nature["change_count"] == 0:
            recommendations.append("当前形势稳定，宜守不宜进")
        elif nature["change_count"] == 1:
            recommendations.append("单一领域有变化，注意把握机会")
        elif nature["change_count"] >= 3:
            recommendations.append("变化较多，需要全面应对")
        
        # 基于影响范围的建议
        if impact["overall_impact"]["intensity"] == "强":
            recommendations.append("变化影响重大，需要认真对待")
        
        # 基于时序的建议
        if temporal["temporal_span"]["duration"] == "短期":
            recommendations.append("变化见效较快，及时把握")
        elif temporal["temporal_span"]["duration"] == "长期":
            recommendations.append("变化需要时间，保持耐心")
        
        return recommendations

    def analyze_directions(self) -> Dict:
        """分析卦象的方位特征"""
        # 基本方位属性
        directions = {
            "乾": {"direction": "西北", "season": "冬", "time": "夜"},
            "坤": {"direction": "西南", "season": "夏", "time": "午"},
            "震": {"direction": "东", "season": "春", "time": "晨"},
            "巽": {"direction": "东南", "season": "春夏之交", "time": "晚"},
            "坎": {"direction": "北", "season": "冬", "time": "子"},
            "离": {"direction": "南", "season": "夏", "time": "午"},
            "艮": {"direction": "东北", "season": "冬春之交", "time": "寅"},
            "兑": {"direction": "西", "season": "秋", "time": "酉"}
        }
        
        # 获取上下卦
        upper_trigram = self._get_upper_trigram_name()
        lower_trigram = self._get_lower_trigram_name()
        
        # 获取方位信息
        upper_info = directions.get(upper_trigram, {})
        lower_info = directions.get(lower_trigram, {})
        
        # 分析方位组合
        combined_direction = self._analyze_direction_combination(
            upper_info.get("direction"),
            lower_info.get("direction")
        )
        
        # 分析时空特征
        spatiotemporal = self._analyze_spatiotemporal_features(
            upper_info,
            lower_info
        )
        
        return {
            "upper_trigram": {
                "name": upper_trigram,
                **upper_info
            },
            "lower_trigram": {
                "name": lower_trigram,
                **lower_info
            },
            "combined_direction": combined_direction,
            "spatiotemporal_features": spatiotemporal,
            "recommendations": self._generate_direction_recommendations(combined_direction)
        }

    def _analyze_direction_combination(self, upper_dir: str, lower_dir: str) -> Dict:
        """分析方位组合关系"""
        if not (upper_dir and lower_dir):
            return {"type": "未知", "strength": "无", "description": "方位信息不完整"}
            
        # 方位对应的角度
        direction_angles = {
            "东": 90, "东南": 135, "南": 180, "西南": 225,
            "西": 270, "西北": 315, "北": 0, "东北": 45
        }
        
        # 计算方位角度差
        angle_diff = abs(direction_angles[upper_dir] - direction_angles[lower_dir])
        if angle_diff > 180:
            angle_diff = 360 - angle_diff
            
        # 分析方位关系
        if angle_diff == 0:
            relation = {"type": "同向", "strength": "最强", "description": "上下一致，力量集中"}
        elif angle_diff == 180:
            relation = {"type": "对冲", "strength": "最弱", "description": "上下相对，力量分散"}
        elif angle_diff < 90:
            relation = {"type": "相助", "strength": "较强", "description": "方向协调，力量互补"}
        else:
            relation = {"type": "相离", "strength": "较弱", "description": "方向偏离，力量分散"}
            
        return relation

    def _analyze_spatiotemporal_features(self, upper_info: Dict, lower_info: Dict) -> Dict:
        """分析时空特征"""
        # 季节变化分析
        season_progression = self._analyze_season_progression(
            upper_info.get("season"),
            lower_info.get("season")
        )
        
        # 时间流转分析
        time_flow = self._analyze_time_flow(
            upper_info.get("time"),
            lower_info.get("time")
        )
        
        return {
            "season_progression": season_progression,
            "time_flow": time_flow,
            "energy_pattern": self._get_energy_pattern(season_progression, time_flow)
        }

    def _analyze_season_progression(self, upper_season: str, lower_season: str) -> Dict:
        """分析季节变化"""
        seasons_order = ["春", "夏", "秋", "冬"]
        if not (upper_season and lower_season):
            return {"type": "未知", "description": "季节信息不完整"}
            
        # 处理特殊季节表述
        upper_season = upper_season.replace("之交", "")
        lower_season = lower_season.replace("之交", "")
        
        if upper_season == lower_season:
            return {"type": "稳定", "description": "季节稳定，能量平稳"}
            
        # 判断季节变化方向
        try:
            upper_idx = seasons_order.index(upper_season)
            lower_idx = seasons_order.index(lower_season)
            
            if (upper_idx - lower_idx) % 4 == 1:
                return {"type": "顺行", "description": "季节顺序发展，能量渐进"}
            elif (upper_idx - lower_idx) % 4 == 3:
                return {"type": "逆行", "description": "季节逆序变化，能量回溯"}
            else:
                return {"type": "跳跃", "description": "季节跨度较大，能量转换显著"}
        except ValueError:
            return {"type": "特殊", "description": "季节变化不规则"}

    def _analyze_time_flow(self, upper_time: str, lower_time: str) -> Dict:
        """分析时间流转"""
        time_order = ["子", "寅", "晨", "午", "晚", "酉", "夜"]
        if not (upper_time and lower_time):
            return {"type": "未知", "description": "时间信息不完整"}
            
        if upper_time == lower_time:
            return {"type": "凝滞", "description": "时间静止，需要突破"}
            
        try:
            upper_idx = time_order.index(upper_time)
            lower_idx = time_order.index(lower_time)
            
            if (upper_idx - lower_idx) % 7 <= 3:
                return {"type": "顺时", "description": "时间顺序流转，发展自然"}
            else:
                return {"type": "逆时", "description": "时间逆序流转，需要调整"}
        except ValueError:
            return {"type": "不规则", "description": "时间流转异常"}

    def _get_energy_pattern(self, season_prog: Dict, time_flow: Dict) -> Dict:
        """分析能量模式"""
        # 能量强度评估
        strength_map = {
            ("顺行", "顺时"): "最强",
            ("顺行", "逆时"): "较强",
            ("逆行", "顺时"): "较弱",
            ("逆行", "逆时"): "最弱",
            ("稳定", "凝滞"): "停滞",
            ("跳跃", "不规则"): "紊乱"
        }
        
        pattern = strength_map.get(
            (season_prog["type"], time_flow["type"]),
            "中等"
        )
        
        return {
            "pattern": pattern,
            "description": self._get_energy_description(pattern)
        }

    def _get_energy_description(self, pattern: str) -> str:
        """获取能量模式描述"""
        descriptions = {
            "最强": "能量充沛，发展顺畅",
            "较强": "能量充足，略有阻滞",
            "中等": "能量平稳，发展正常",
            "较弱": "能量不足，需要蓄积",
            "最弱": "能量衰竭，需要休整",
            "停滞": "能量凝滞，需要突破",
            "紊乱": "能量混乱，需要调理"
        }
        return descriptions.get(pattern, "能量状态不明")

    def _generate_direction_recommendations(self, direction_info: Dict) -> List[str]:
        """生成方位相关建议"""
        recommendations = []
        
        # 基于方位关系的建议
        if direction_info["type"] == "同向":
            recommendations.extend([
                "方向明确，可以果断前进",
                "力量集中，适合专注发展"
            ])
        elif direction_info["type"] == "对冲":
            recommendations.extend([
                "需要调和对立的力量",
                "寻找平衡点再行动"
            ])
        elif direction_info["type"] == "相助":
            recommendations.extend([
                "力量互补，可以稳步前进",
                "注意协调各方面的发展"
            ])
        elif direction_info["type"] == "相离":
            recommendations.extend([
                "需要整合分散的力量",
                "调整方向后再行动"
            ])
            
        return recommendations

    def predict_trends(self) -> Dict:
        """预测发展趋势"""
        # 获取基础分析数据
        direction_analysis = self.analyze_directions()
        change_analysis = self.analyze_hexagram_changes()
        
        # 综合分析趋势
        trend_factors = {
            "direction": direction_analysis["combined_direction"]["strength"],
            "energy": direction_analysis["spatiotemporal_features"]["energy_pattern"]["pattern"],
            "change_intensity": change_analysis["change_nature"]["change_intensity"],
            "temporal_pattern": change_analysis["temporal_analysis"]["development_pattern"]
        }
        
        # 计算趋势指标
        trend_indicators = self._calculate_trend_indicators(trend_factors)
        
        # 生成预测结论
        predictions = self._generate_predictions(trend_indicators)
        
        return {
            "trend_factors": trend_factors,
            "indicators": trend_indicators,
            "predictions": predictions,
            "confidence_level": self._calculate_confidence_level(trend_indicators)
        }

    def _calculate_trend_indicators(self, factors: Dict) -> Dict:
        """计算趋势指标"""
        # 方位强度转换
        direction_scores = {
            "最强": 1.0, "较强": 0.75, "中等": 0.5,
            "较弱": 0.25, "最弱": 0.1
        }
        
        # 能量模式转换
        energy_scores = {
            "最强": 1.0, "较强": 0.8, "中等": 0.6,
            "较弱": 0.4, "最弱": 0.2, "停滞": 0.1,
            "紊乱": 0.3
        }
        
        # 变化强度转换
        intensity_scores = {
            "强": 1.0, "中": 0.6, "弱": 0.3
        }
        
        # 发展模式转换
        pattern_scores = {
            "连续发展": 1.0, "跳跃发展": 0.7,
            "突变": 0.5, "稳定": 0.3
        }
        
        # 计算各项指标
        direction_score = direction_scores.get(factors["direction"], 0.5)
        energy_score = energy_scores.get(factors["energy"], 0.5)
        intensity_score = intensity_scores.get(factors["change_intensity"], 0.5)
        pattern_score = pattern_scores.get(factors["temporal_pattern"], 0.5)
        
        # 计算综合指标
        momentum = (direction_score + energy_score) / 2
        stability = 1 - abs(direction_score - energy_score)
        potential = (intensity_score + pattern_score) / 2
        
        return {
            "momentum": momentum,  # 发展动力
            "stability": stability,  # 稳定性
            "potential": potential,  # 发展潜力
            "raw_scores": {
                "direction": direction_score,
                "energy": energy_score,
                "intensity": intensity_score,
                "pattern": pattern_score
            }
        }

    def _generate_predictions(self, indicators: Dict) -> List[Dict]:
        """生成预测结论"""
        predictions = []
        
        # 动力预测
        momentum = indicators["momentum"]
        if momentum > 0.8:
            predictions.append({
                "aspect": "发展动力",
                "level": "极强",
                "description": "发展势头强劲，可以大胆进取"
            })
        elif momentum > 0.6:
            predictions.append({
                "aspect": "发展动力",
                "level": "较强",
                "description": "动力充足，稳步前进"
            })
        else:
            predictions.append({
                "aspect": "发展动力",
                "level": "一般",
                "description": "动力欠缺，需要蓄势"
            })
            
        # 稳定性预测
        stability = indicators["stability"]
        if stability > 0.8:
            predictions.append({
                "aspect": "稳定性",
                "level": "高",
                "description": "发展稳定，可持续性强"
            })
        elif stability > 0.6:
            predictions.append({
                "aspect": "稳定性",
                "level": "中",
                "description": "基本稳定，有小幅波动"
            })
        else:
            predictions.append({
                "aspect": "稳定性",
                "level": "低",
                "description": "变数较大，需要防范"
            })
            
        # 潜力预测
        potential = indicators["potential"]
        if potential > 0.8:
            predictions.append({
                "aspect": "发展潜力",
                "level": "巨大",
                "description": "潜力充沛，前景广阔"
            })
        elif potential > 0.6:
            predictions.append({
                "aspect": "发展潜力",
                "level": "较好",
                "description": "有一定潜力，可以开发"
            })
        else:
            predictions.append({
                "aspect": "发展潜力",
                "level": "有限",
                "description": "潜力有限，需要创新"
            })
            
        return predictions

    def _calculate_confidence_level(self, indicators: Dict) -> Dict:
        """计算预测可信度"""
        # 基础分数计算
        base_score = (
            indicators["momentum"] * 0.3 +
            indicators["stability"] * 0.4 +
            indicators["potential"] * 0.3
        )
        
        # 可信度级别判定
        if base_score > 0.8:
            level = "很高"
            description = "预测可信度很高，可以作为重要参考"
        elif base_score > 0.6:
            level = "较高"
            description = "预测可信度较高，可以参考"
        elif base_score > 0.4:
            level = "中等"
            description = "预测可信度一般，仅供参考"
        else:
            level = "较低"
            description = "预测可信度较低，需要谨慎参考"
            
        return {
            "level": level,
            "score": base_score,
            "description": description
        }

    def _analyze_wu_xing(self) -> Dict:
        """分析五行关系"""
        try:
            # 获取本卦上下卦的五行属性
            upper_element = self.five_elements.get_trigram_element(self.hexagram.original_trigrams[1])
            lower_element = self.five_elements.get_trigram_element(self.hexagram.original_trigrams[0])
            
            # 分析本卦五行关系
            relation = self.five_elements.get_relation(upper_element, lower_element)
            recommendations = self.five_elements.get_relationship_recommendations(upper_element, lower_element)
            
            # 获取变卦五行属性和关系
            changed_upper = self.five_elements.get_trigram_element(self.hexagram.changed_trigrams[1])
            changed_lower = self.five_elements.get_trigram_element(self.hexagram.changed_trigrams[0])
            changed_relation = self.five_elements.get_relation(changed_upper, changed_lower)
            changed_recommendations = self.five_elements.get_relationship_recommendations(changed_upper, changed_lower)
            
            # 分析五行循环
            cycle_analysis = self.five_elements.analyze_relationship_cycle(upper_element)
            
            return {
                "original": {
                    "upper": {
                        "trigram": self.hexagram.original_trigrams[1],
                        "element": upper_element,
                        "attributes": self.five_elements.get_element_attributes(upper_element)
                    },
                    "lower": {
                        "trigram": self.hexagram.original_trigrams[0],
                        "element": lower_element,
                        "attributes": self.five_elements.get_element_attributes(lower_element)
                    },
                    "relation": relation,
                    "recommendations": recommendations
                },
                "changed": {
                    "upper": {
                        "trigram": self.hexagram.changed_trigrams[1],
                        "element": changed_upper,
                        "attributes": self.five_elements.get_element_attributes(changed_upper)
                    },
                    "lower": {
                        "trigram": self.hexagram.changed_trigrams[0],
                        "element": changed_lower,
                        "attributes": self.five_elements.get_element_attributes(changed_lower)
                    },
                    "relation": changed_relation,
                    "recommendations": changed_recommendations
                },
                "cycle_analysis": cycle_analysis,
                "summary": f"{upper_element}上{lower_element}下，{relation['description']}",
                "migration_advice": self._get_migration_advice(relation, changed_relation)
            }
        except Exception as e:
            print(f"五行分析错误: {str(e)}")
            return {}
            
    def _get_migration_advice(self, original_relation: Dict, changed_relation: Dict) -> List[str]:
        """根据五行关系生成迁移建议"""
        advice = []
        
        # 基于本卦关系提供建议
        if original_relation["favorable"]:
            advice.append("当前形势有利于迁移，可以积极准备")
        else:
            advice.append("当前形势需要谨慎，建议做好充分准备")
            
        # 基于变卦关系提供建议
        if changed_relation["favorable"]:
            advice.append("长期发展趋势向好，可以规划长远")
        else:
            advice.append("未来可能面临挑战，需要制定应对策略")
            
        # 基于关系强度提供具体建议
        if original_relation["strength"] > 0.7:
            advice.append("当前基础稳固，可以采取主动行动")
        elif original_relation["strength"] < 0.4:
            advice.append("基础还需加强，建议先做内部调整")
            
        return advice

    def _get_position_nature(self, position: int) -> str:
        """获取爻位性质
        Args:
            position: 爻位（1-6）
        Returns:
            str: 阳位或阴位
        """
        # 一、三、五爻为阳位，二、四、六爻为阴位
        if position in [1, 3, 5]:
            return "阳位"
        return "阴位"

    def _get_line_element(self, position: int) -> str:
        """获取爻的五行属性
        Args:
            position: 爻位（1-6）
        Returns:
            str: 五行属性
        """
        # 根据卦的五行属性和爻位确定五行
        if position > 3:  # 上卦
            return self.five_elements.get_trigram_element(self.hexagram.original_trigrams[1])
        return self.five_elements.get_trigram_element(self.hexagram.original_trigrams[0])  # 下卦

    def _get_shi_ying(self) -> Dict:
        """获取世应爻位置
        Returns:
            Dict: 包含世爻和应爻位置的字典
        """
        # 世应规则：
        # 乾宫：世五应二
        # 兑宫：世四应一
        # 离宫：世三应六
        # 震宫：世二应五
        # 巽宫：世一应四
        # 坎宫：世六应三
        # 艮宫：世五应二
        # 坤宫：世四应一
        shi_ying_map = {
            "乾": (5, 2),
            "兑": (4, 1),
            "离": (3, 6),
            "震": (2, 5),
            "巽": (1, 4),
            "坎": (6, 3),
            "艮": (5, 2),
            "坤": (4, 1)
        }
        
        shi, ying = shi_ying_map.get(self.hexagram.gong, (0, 0))
        
        return {
            "shi": shi,
            "ying": ying,
            "shi_state": "动" if shi in self.hexagram.changing_lines else "静",
            "ying_state": "动" if ying in self.hexagram.changing_lines else "静",
            "description": self._get_shi_ying_description(shi, ying)
        }
        
    def _get_shi_ying_description(self, shi: int, ying: int) -> str:
        """获取世应关系描述
        Args:
            shi: 世爻位置
            ying: 应爻位置
        Returns:
            str: 世应关系描述
        """
        shi_state = "动" if shi in self.hexagram.changing_lines else "静"
        ying_state = "动" if ying in self.hexagram.changing_lines else "静"
        
        if shi_state == "动" and ying_state == "动":
            return "世应俱动，变化显著"
        elif shi_state == "静" and ying_state == "静":
            return "世应俱静，局势稳定"
        elif shi_state == "动" and ying_state == "静":
            return "世动应静，主动求变"
        else:  # shi_state == "静" and ying_state == "动"
            return "世静应动，被动变化"
            
    def _analyze_shi_yao(self) -> Dict:
        """分析世爻特征
        Returns:
            Dict: 世爻分析结果
        """
        shi_ying = self._get_shi_ying()
        shi_position = shi_ying["shi"]
        
        # 获取世爻的基本特征
        line_value = self.hexagram.lines[shi_position - 1]  # 世爻的阴阳值
        is_changing = shi_position in self.hexagram.changing_lines
        position_nature = self._get_position_nature(shi_position)
        line_nature = "阳" if line_value == 1 else "阴"
        
        # 计算世爻强度
        strength = self._get_line_strength(shi_position, line_value, is_changing)
        
        # 分析世爻与所在卦的关系
        trigram_index = 1 if shi_position > 3 else 0
        trigram = self.hexagram.original_trigrams[trigram_index]
        
        return {
            "position": shi_position,
            "value": line_value,
            "changing": is_changing,
            "position_nature": position_nature,
            "line_nature": line_nature,
            "harmony": line_nature == position_nature.replace("位", ""),
            "strength": strength,
            "trigram": trigram,
            "element": self._get_line_element(shi_position),
            "state_description": self._get_shi_yao_state(shi_position, line_value, is_changing),
            "advice": self._get_shi_yao_advice(shi_position, line_value, is_changing, strength["value"])
        }
        
    def _get_shi_yao_state(self, position: int, value: int, is_changing: bool) -> str:
        """获取世爻状态描述
        Args:
            position: 世爻位置
            value: 爻的阴阳值
            is_changing: 是否是变爻
        Returns:
            str: 状态描述
        """
        nature = "阳" if value == 1 else "阴"
        position_nature = self._get_position_nature(position).replace("位", "")
        
        if nature == position_nature and not is_changing:
            return "世爻得正，局势稳定"
        elif nature == position_nature and is_changing:
            return "世爻得正而变，主动求变"
        elif nature != position_nature and not is_changing:
            return "世爻失正，需要调整"
        else:  # nature != position_nature and is_changing
            return "世爻失正而变，被动变化"
            
    def _get_shi_yao_advice(self, position: int, value: int, is_changing: bool, strength: float) -> List[str]:
        """获取世爻建议
        Args:
            position: 世爻位置
            value: 爻的阴阳值
            is_changing: 是否是变爻
            strength: 爻的强度值
        Returns:
            List[str]: 建议列表
        """
        advice = []
        nature = "阳" if value == 1 else "阴"
        position_nature = self._get_position_nature(position).replace("位", "")
        
        # 基于阴阳和谐度的建议
        if nature == position_nature:
            advice.append("当前位置有利，可以稳步推进")
        else:
            advice.append("需要调整策略，寻找更合适的定位")
            
        # 基于变化状态的建议
        if is_changing:
            advice.append("时机已到，可以采取行动")
        else:
            advice.append("暂时保持现状，等待合适时机")
            
        # 基于强度的建议
        if strength >= 0.8:
            advice.append("形势大好，可以大胆行动")
        elif strength >= 0.6:
            advice.append("条件较好，可以稳步前进")
        elif strength >= 0.4:
            advice.append("形势一般，需要谨慎行事")
        else:
            advice.append("条件不足，建议先行积累")
            
        return advice