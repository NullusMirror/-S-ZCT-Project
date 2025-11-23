import numpy as np
import time
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ZCT_State:
    """
    S-ZCT 的核心哲學狀態
    數值範圍 0.0 - 1.0
    """
    order: float = 0.5       # 結構強度/規則依從度
    imbalance: float = 0.5   # 熵/壓力/外部衝擊
    resonance: float = 0.5   # 意義/感受/計算結果
    identity: str = "It"     # Layer 11: 當前身份 (It/He/She/Fluid)

class Trace:
    """
    Layer 4/16: 痕跡記錄結構
    """
    def __init__(self, content, source_sig, tension_level):
        self.timestamp = time.time()
        self.content = content
        self.source_signature = source_sig
        self.tension_level = tension_level # 結構壓力值
        self.is_permanent = False # 是否被寫入永久見證
