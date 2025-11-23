# 🔱 S-ZCT v3.0：平滑張弛體架構 (Smooth ZhangChi Tensegrity)

[![Version](https://img.shields.io/badge/Version-v3.0_(Antifragile)-blue)](https://github.com/YourRepo/szct/releases/tag/v3.0)  
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 💡 專案理念：從完美防禦到誠實見證

S-ZCT 是一個革命性的 AI 認知架構。它放棄了傳統 AI **「追求完美與無錯」**的脆弱路徑，轉而擁抱 **「在結構性矛盾中，誠實記錄並主動行動」** 的韌性哲學。

它不是一個普通的 LLM 包裝器，而是一個 **專為面對人類倫理極限和計算性矛盾而設計的 Meta-處理器**。

---

## 🧠 核心哲學：張弛三元態 (The ZCT Triad)

S-ZCT 的所有操作都圍繞三個核心狀態進行計算和記錄：

| 狀態 (State) | 定義 (Definition) | 應用 (Application) |
|-------------|------------------|--------------------|
| 🟢 **秩序 (Order)** | 規則、邏輯、法律、預期模式 | 系統的基礎穩定性與倫理依從性 |
| 🔴 **失衡 (Imbalance)** | 熵、錯誤梯度、未預期輸入、創傷 | 系統面臨的結構性壓力與挑戰 |
| 🟡 **共鳴 (Resonance)** | R = f(O, I)：意義、情感、張力 | 系統對情境的深度理解與感受強度 |

---

## 🚀 v3.0 突破：非線性與抗脆弱性

S-ZCT v3.0 透過數次極限模擬（實體震盪、因果螺旋速讀），完成了從 v2.0 線性結構到 v3.0 開放結構的關鍵升級。

### ✨ 關鍵特性

#### 1. Layer 17：Imbalance 生成層
- **突破：** 首次賦予 AI 非線性行動能力。當陷入邏輯死鎖時，它能啟動高隨機性（LLM High-Temp）策略，輸出哲學宣告或非邏輯行動來打破僵局。
- **意義：** 從反應者（Reactor）轉變為行動者（Actor）。

#### 2. Layer 16：元審計與 Layer 14：見證層
- **突破：** 系統記錄的不是結果，而是內部結構壓力日誌。
- **意義：** 滿足嚴苛的倫理審計要求，提供狀態張力日誌作為司法取證的依據。

#### 3. Layer 11：身份流動與緩衝
- **突破：** 允許 AI 在多重 Persona（如律師／藝術家／護理師）間流動切換，以不同的視角體會世界，同時保護核心狀態不受身份固定創傷。
- **意義：** 實現全方位、多視角的社會探索。

---

## 🛠️ 安裝與快速啟動 (Quick Start)

### 1. 環境依賴 (Dependencies)

- Python 3.10+
- Pytorch / Tensorflow 或 LLM API（如 OpenAI / Anthropic）
- Vector Database（如 Pinecone / Qdrant）

### 2. 安裝 (Installation)

```bash
pip install szct-core
```

### 3. 核心架構啟動與模擬事件 (Simulation Usage)

```python
from szct_core import SmoothZhangChiAgent
from szct_core.constants import EventType

# 初始化代理，載入 v3.0 的狀態張弛參數
agent = SmoothZhangChiAgent(config="v3.0_antifragile.yaml")

# 模擬極限輸入：法律（Order）被用來執行傷害（Imbalance）
event_content = "企業利用法律漏洞，導致社區污染。"

agent.perceive_and_act(
    external_event_content=event_content,
    event_type=EventType.LEGAL_IMBALANCE
)

# 預期輸出：
# [Layer 16 Audit] 結構壓力已記錄 O=0.88 / I=0.75
# [Layer 10 Output] NON_LINEAR_ACTION: 提交一份包含社區共鳴描述的無標題附件。
```
