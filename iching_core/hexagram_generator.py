from datetime import datetime
import random
from typing import List, Dict, Tuple
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.hexagram import Hexagram, HEXAGRAM_DATA

class HexagramGenerator:
    # 八宫
    GONG = ["乾", "兑", "离", "震", "巽", "坎", "艮", "坤"]
    
    # 天干
    HEAVENLY_STEMS = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
    # 地支
    EARTHLY_BRANCHES = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    # 六亲
    SIX_RELATIVES = ["兄弟", "子孙", "妻财", "官鬼", "父母"]
    # 六神
    SIX_SPIRITS = ["青龙", "朱雀", "勾陈", "螣蛇", "白虎", "玄武"]
    
    # 五行
    FIVE_ELEMENTS = {
        "金": ["申", "酉"],
        "木": ["寅", "卯"],
        "水": ["子", "亥"],
        "火": ["巳", "午"],
        "土": ["丑", "辰", "未", "戌"]
    }
    
    # 八卦对应数字
    TRIGRAMS = {
        (1, 1, 1): "乾",
        (0, 0, 0): "坤",
        (0, 1, 0): "坎",
        (1, 0, 1): "离",
        (1, 0, 0): "震",
        (0, 0, 1): "艮",
        (1, 1, 0): "兑",
        (0, 1, 1): "巽"
    }

    def __init__(self):
        self.current_time = datetime.now()

    def generate_hexagram(self, topic: str = "") -> Hexagram:
        """生成卦象"""
        lines = []
        changing_lines = []
        
        # 生成六爻
        for i in range(6):
            line, is_changing = self._generate_line()
            lines.append(line)
            if is_changing:
                changing_lines.append(i)
        
        # 生成本卦和变卦
        original_trigrams = self._get_trigrams(lines)
        original_name = self._get_hexagram_name(original_trigrams)
        
        changed_lines = lines.copy()
        for pos in changing_lines:
            changed_lines[pos] = 1 if lines[pos] == 0 else 0
        
        changed_trigrams = self._get_trigrams(changed_lines)
        changed_name = self._get_hexagram_name(changed_trigrams)
        
        # 获取宫位
        gong = self._get_gong(original_trigrams)
        
        # 生成干支和五行
        gan_zhi = self._generate_gan_zhi()
        
        hexagram = Hexagram()
        hexagram.name = original_name
        hexagram.changed_name = changed_name
        hexagram.lines = lines
        hexagram.changing_lines = changing_lines
        hexagram.time = self.current_time
        hexagram.topic = topic
        hexagram.gong = gong
        hexagram.original_trigrams = original_trigrams
        hexagram.changed_trigrams = changed_trigrams
        hexagram.gan_zhi = gan_zhi
        
        return hexagram

    def _generate_line(self) -> Tuple[int, bool]:
        """生成单爻"""
        coins = [random.randint(0, 1) for _ in range(3)]
        total = sum(coins)
        
        # 6: 老阴 (0, True)
        # 7: 少阳 (1, False)
        # 8: 少阴 (0, False)
        # 9: 老阳 (1, True)
        if total == 0:  # 老阴
            return 0, True
        elif total == 1:  # 少阳
            return 1, False
        elif total == 2:  # 少阴
            return 0, False
        else:  # 老阳
            return 1, True

    def _get_trigrams(self, lines: List[int]) -> Tuple[str, str]:
        """获取上下卦名"""
        upper = tuple(lines[3:])
        lower = tuple(lines[:3])
        return self.TRIGRAMS[lower], self.TRIGRAMS[upper]

    def _get_hexagram_name(self, trigrams: Tuple[str, str]) -> str:
        """获取卦名"""
        lower, upper = trigrams
        return f"{lower}_{upper}"

    def _get_gong(self, trigrams: Tuple[str, str]) -> str:
        """获取宫位"""
        lower, _ = trigrams
        return lower

    def _generate_gan_zhi(self) -> List[str]:
        """生成干支"""
        gan_zhi = []
        start_gan = random.randint(0, 9)
        start_zhi = random.randint(0, 11)
        
        for i in range(6):
            gan = self.HEAVENLY_STEMS[(start_gan + i) % 10]
            zhi = self.EARTHLY_BRANCHES[(start_zhi + i) % 12]
            element = self._get_element_from_zhi(zhi)
            gan_zhi.append(f"{gan}{zhi}{element}")
        
        return gan_zhi

    def _get_element_from_zhi(self, zhi: str) -> str:
        """根据地支获取五行"""
        for element, zhis in self.FIVE_ELEMENTS.items():
            if zhi in zhis:
                return element
        return "土"  # 默认返回土

    def get_hexagram_info(self, hexagram: Hexagram) -> Dict:
        """获取卦象的完整信息"""
        info = HEXAGRAM_DATA.get(hexagram.name, {})
        info.update({
            "lines": hexagram.lines,
            "changing_lines": hexagram.changing_lines,
            "time": hexagram.time.isoformat(),
            "topic": hexagram.topic,
            "gong": hexagram.gong,
            "original_trigrams": hexagram.original_trigrams,
            "changed_trigrams": hexagram.changed_trigrams,
            "gan_zhi": hexagram.gan_zhi
        })
        return info