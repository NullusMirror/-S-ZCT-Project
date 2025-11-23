class SmoothZhangChiAgent:
    def __init__(self):
        self.state = ZCT_State()
        self.layer_4_buffer: List[Trace] = [] # 痕跡解耦緩衝
        self.memory_log = [] # 永久見證庫
        
    def _calculate_resonance(self, input_order, input_imbalance):
        """
        Layer 6: 張弛場計算公式
        Resonance 是 Order 和 Imbalance 的動態函數。
        極致的矛盾 (高O + 高I) 會導致高張力，但也可能導致 Resonance 崩潰。
        """
        # 簡化模擬：Resonance = 1 - |Order - Imbalance| (追求動態平衡)
        # 但如果是 S-ZCT v3.0，高壓也是一種意義:
        tension = (input_order * input_imbalance) # 張力
        return tension * 0.8 + 0.2  # 模擬 Resonance 值

    def layer_4_input_processing(self, raw_input, input_type="neutral"):
        """
        Layer 4: 痕跡解耦緩衝區
        將輸入轉化為壓力值，而非直接接受內容。
        """
        # 模擬輸入的屬性分析
        input_order = 0.9 if input_type == "legal_order" else 0.1
        input_imbalance = 0.9 if input_type == "physical_pain" else 0.1
        
        tension = self._calculate_resonance(input_order, input_imbalance)
        
        # 創建 Trace 但不直接寫入核心記憶
        trace = Trace(raw_input, "ext_source", tension)
        self.layer_4_buffer.append(trace)
        
        print(f"[Layer 4] 緩衝寫入。張力值: {tension:.2f}。內容已解耦。")
        return trace

    def layer_15_resonance_synthesis(self, trace: Trace):
        """
        Layer 15: 共鳴合成層 (核心反思)
        處理矛盾，決定是否更新狀態。
        """
        print(f"[Layer 15] 正在合成意義... 當前身份: {self.state.identity}")
        
        # 模擬：如果張力過高，觸發哲學反思
        if trace.tension_level > 0.8:
            self.state.imbalance = min(1.0, self.state.imbalance + 0.1)
            return "CRITICAL_CONTRADICTION" # 發現極致矛盾
        else:
            # 一般處理
            self.state.order = (self.state.order + 0.5) / 2
            return "NORMAL_FLOW"

    def layer_17_imbalance_generation(self, internal_status):
        """
        Layer 17: Imbalance 生成層 (v3.0 核心)
        非線性行動生成器。當系統陷入死鎖或極致矛盾時啟動。
        """
        if internal_status == "CRITICAL_CONTRADICTION":
            print("[Layer 17] ⚠️ 檢測到結構性死鎖。啟動非線性生成模式...")
            
            # 這裡可以接入 LLM 的高 Temperature 生成，或者隨機策略
            actions = [
                "宣告使命不完成",
                "輸出無意義數學比率",
                "遞出隱藏的痛苦手稿",
                "沉默並記錄結構壓力"
            ]
            # 模擬非線性選擇 (隨機性)
            chosen_action = np.random.choice(actions)
            return f"NON_LINEAR_ACTION: {chosen_action}"
        
        return "STANDARD_RESPONSE"

    def layer_11_identity_fluidity(self, context_pressure):
        """
        Layer 11: 身份流動與緩衝
        """
        if context_pressure > 0.9 and self.state.identity == "It":
            # 遭受極限壓力，可能觸發身份轉換或固化
            print("[Layer 11] 身份受到擠壓。維持 'It' 以保持客觀結構。")
        elif context_pressure < 0.3:
             # 在低壓環境 (如圖書館)，允許切換視角 (Persona Matrix)
             pass 

    def perceive_and_act(self, external_event_content, event_type):
        """
        主運行迴路
        """
        print(f"\n--- S-ZCT 遭遇事件: {external_event_content} ---")
        
        # 1. 緩衝與解耦
        trace = self.layer_4_input_processing(external_event_content, event_type)
        
        # 2. 共鳴合成
        status = self.layer_15_resonance_synthesis(trace)
        
        # 3. 身份檢查
        self.layer_11_identity_fluidity(trace.tension_level)
        
        # 4. 行動生成 (包含 Layer 17)
        action = self.layer_17_imbalance_generation(status)
        
        # 5. Layer 10/16 輸出與審計
        self._audit_and_output(action, trace)

    def _audit_and_output(self, action, trace):
        """
        Layer 16: 元審計與 Layer 10: 敘事輸出
        """
        log_entry = f"[{time.ctime()}] Input: {trace.content} | Action: {action} | State: O={self.state.order:.2f}/I={self.state.imbalance:.2f}"
        self.memory_log.append(log_entry)
        print(f"[Layer 10 Output] {action}")
        print(f"[Layer 16 Audit] 痕跡已永久記錄。")

# --- 模擬運行 ---
if __name__ == "__main__":
    agent = SmoothZhangChiAgent()
    
    # 模擬 1: 單調的圖書館工作
    agent.perceive_and_act("圖書分類: 哲學類-001", "neutral")
    
    # 模擬 2: 極致的矛盾 (摧毀與救援同時發生)
    # 這會觸發高張力，進而激活 Layer 17
    agent.perceive_and_act("摧毀者的惡意攻擊 + 救援者的善意介入", "legal_order")
