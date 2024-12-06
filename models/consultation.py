from typing import Dict, Optional
from datetime import datetime
from .hexagram import Hexagram

class Consultation:
    def __init__(self):
        self.id: str  # 唯一标识符
        self.category: str  # 咨询类别
        self.question: str  # 咨询问题
        self.hexagram: Hexagram  # 本卦
        self.changed_hexagram: Optional[Hexagram]  # 变卦
        self.analysis: Dict  # AI分析结果
        self.created_at: datetime  # 创建时间
        self.updated_at: datetime  # 更新时间
        
    def to_dict(self) -> Dict:
        """将咨询记录转换为字典格式"""
        return {
            "id": self.id,
            "category": self.category,
            "question": self.question,
            "hexagram": self.hexagram.__dict__,
            "changed_hexagram": self.changed_hexagram.__dict__ if self.changed_hexagram else None,
            "analysis": self.analysis,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Consultation':
        """从字典创建咨询记录实例"""
        consultation = cls()
        consultation.id = data["id"]
        consultation.category = data["category"]
        consultation.question = data["question"]
        
        hexagram = Hexagram()
        for key, value in data["hexagram"].items():
            setattr(hexagram, key, value)
        consultation.hexagram = hexagram
        
        if data.get("changed_hexagram"):
            changed_hexagram = Hexagram()
            for key, value in data["changed_hexagram"].items():
                setattr(changed_hexagram, key, value)
            consultation.changed_hexagram = changed_hexagram
        
        consultation.analysis = data["analysis"]
        consultation.created_at = datetime.fromisoformat(data["created_at"])
        consultation.updated_at = datetime.fromisoformat(data["updated_at"])
        
        return consultation