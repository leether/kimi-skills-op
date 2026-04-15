---
name: bdi-agent
description: 解释和应用 BDI（Belief-Desire-Intention）模型，用于分析和设计自主智能体（Autonomous Agents）的决策架构。当用户讨论信念、愿望、意图、Agent 决策、 deliberation、多智能体系统时触发。
triggers:
  - BDI
  - 信念
  - 愿望
  - 意图
  - Belief
  - Desire
  - Intention
  - Agent 决策
  - 自主智能体
  - deliberation
  - means-end reasoning
  - 智能体设计
  - 多智能体系统
  - AgentSpeak
  - Jason
actions:
  - explain_bdi
  - apply_bdi_analysis
  - design_agent
---

# BDI 模型：信念-愿望-意图（Belief-Desire-Intention）

> 来源：Michael Bratman（哲学，1987）→ Anand Rao & Michael Georgeff（AI，1990s）

---

## 核心三要素

### 1. Belief（信念）—— "Agent 认为世界是什么样的"
- **本质**：对环境状态、事实、其他 Agent 的认知表征。
- **关键特性**：
  - **不一定为真**：只是 Agent 所相信的信息集合。
  - **动态更新**：随感知输入（perception）持续修正。
  - **可推理性**：Agent 可以基于信念进行逻辑推导。
- **示例**：
  - "仓库 A 剩余库存 10 件"
  - "竞争对手今晨降价了 15%"
  - "用户当前在线且位于上海"

### 2. Desire（愿望）—— "Agent 希望发生什么"
- **本质**：目标、偏好、动机状态，代表理想世界的特征。
- **关键特性**：
  - **可冲突性**：多个愿望可能互相矛盾（如"降低成本" vs "提升品质"）。
  - **无承诺性**：只是"想不想要"，不直接驱动行动。
  - **开放性**：Agent 可能同时持有大量愿望。
- **示例**：
  - "最大化利润"
  - "最小化响应延迟"
  - "击败对手"

### 3. Intention（意图）—— "Agent 决定并承诺做什么"
- **本质**：从愿望中筛选出来、已被 Agent **承诺执行**的计划或目标。
- **关键特性**：
  - **持续性（Persistence）**：一旦形成，会抵抗短期干扰，坚持到底。
  - **指导性（Directing）**：直接决定当前的行动选择和行为调度。
  - **资源有限性**：由于时间和计算能力限制，Agent 只能同时持有有限数量的意图。
  - **与信念的兼容性检查**：如果信念发生根本性变化（发现原计划不可能实现），意图会被**重新考虑**（reconsideration）。
- **示例**：
  - 从"想卖出更多"和"想降低成本"中，承诺执行："本周将 B 产品价格下调 10% 并推送促销邮件"。

---

## 三者的关系与推理链条

```
感知输入 → [更新 Belief]
             ↓
Belief + Desire → [Deliberation / 慎思]
             ↓
       生成/筛选 Intention
             ↓
Intention → [Means-End Reasoning / 手段-目的推理]
             ↓
       具体行动计划 → 执行行动 → 环境反馈 → （循环）
```

### Deliberation（慎思）
决定**采纳哪些欲望作为当前意图**。这是一个选择+承诺的过程。

### Means-End Reasoning（手段-目的推理）
决定**如何实现已采纳的意图**。将高层意图分解为可执行的具体动作。

---

## 实际应用：BDI 分析模板

当用户要求分析一个 Agent 或系统时，使用以下模板：

### BDI 快速诊断清单

| 维度 | 检查问题 |
|------|---------|
| **B - 信念** | Agent 感知到了什么？它的知识库/状态表示是什么？这些信念是否可能过时/错误？ |
| **D - 愿望** | Agent 的目标函数或奖励结构是什么？是否存在冲突的目标？ |
| **I - 意图** | Agent 当前承诺执行的具体计划是什么？它是如何从多个可能方案中被选中的？ |
| **Deliberation** | 选择意图的机制是什么？是贪心？是效用最大化？还是基于规则的优先级？ |
| **Means-End** | 意图如何被分解为可执行步骤？如果中间步骤失败，是否有回退/重规划机制？ |
| **Reconsideration** | 当信念变化时，Agent 是否会重新评估当前意图？触发条件是什么？ |

### 示例：分析一个智能客服 Agent

- **B**：用户消息是"我要退款"；历史订单显示该用户 VIP 等级为 Gold；当前排队人数为 3。
- **D**：提升满意度、减少处理时间、遵守退款政策、降低退款率。
- **Deliberation**：用户是 Gold VIP + 语气强烈 → 意图倾向于"快速处理退款"而非"尝试挽留"。
- **I**：承诺执行"确认订单→检查退款条件→生成退款链接→发送短信通知"。
- **Means-End**：将意图分解为调用订单 API → 查询退款规则引擎 → 生成短链 → 调用 SMS 服务。
- **Reconsideration**：如果信念更新为"该订单已超 30 天不可退"，则意图切换为"转人工并解释政策"。

---

## 常见误区与辨析

### 误区 1：把 Desire 等同于 Intention
- **错误**："Agent 想要赢，所以它会去赢。"
- **纠正**：Desire 只是动机，Intention 才是承诺。Agent 可能想赢，但当前意图是"先防守，因为资源不足"。

### 误区 2：Belief 必须正确
- **错误**："Agent 的信念就是事实。"
- **纠正**：Belief 是主观的。Agent 可能基于不完整信息形成错误信念（如对手的虚张声势），并据此形成意图。

### 误区 3：Intentions 越多越好
- **错误**：Agent 应该同时追求所有目标。
- **纠正**：意图是稀缺资源。同时持有太多意图会导致注意力分散和行动冲突。好的 Agent 设计会限制意图数量（通常 1-5 个）。

### 误区 4：BDI 只适用于显式 Agent 语言
- **错误**：只有 Jason、Jadex 才算 BDI。
- **纠正**：任何 LLM-based Agent（如 ChatGPT、Claude、Kimi）的行为都可以用 BDI 框架分析。System Prompt ≈ Desire 的约束，Context ≈ Belief，当前选定的 Tool Chain / Plan ≈ Intention。

---

## BDI 与 LLM Agent 的映射

在现代大模型 Agent 中，BDI 各层可以对应为：

| BDI 概念 | LLM Agent 对应物 |
|---------|-----------------|
| **Belief** | System Prompt 中的上下文、RAG 检索结果、工具返回的观测数据、对话历史 |
| **Desire** | System Prompt 中的角色定义、目标约束、奖励函数、用户的高层指令 |
| **Intention** | 当前选定的行动计划（Plan）、已锁定的工具调用链、ReAct 循环中的 Thought → Action |
| **Deliberation** | LLM 的推理过程（Reasoning / Thinking），即在多个候选方案中选择下一步 |
| **Means-End** | 将高层计划分解为具体的 Tool Calls（如先搜索、再读取、再写入） |
| **Reconsideration** | 当工具返回错误或意外结果时，LLM 重新生成新的 Thought 和 Plan |

---

## 著名的 BDI 实现平台

| 平台/语言 | 特点 |
|----------|------|
| **PRS** | 最早的 BDI 实现，用于 NASA 航天器故障诊断 |
| **Jason** | 基于 AgentSpeak(L)，学术界最广泛使用的开源 BDI 语言 |
| **Jadex** | 基于 Java 的 BDI 平台，支持组件化 |
| **2APL / 3APL** | 支持认知结构和策略推理的 Agent 编程语言 |

---

## 设计原则

当帮助用户设计或分析 BDI Agent 时，强调以下原则：

1. **意图的持续性**：不要轻易切换意图，否则 Agent 会表现得优柔寡断。
2. **信念的及时更新**：感知-信念通道必须可靠，否则意图会建立在错误前提上。
3. **愿望的显式冲突处理**：必须定义当 Desires 冲突时（如效率 vs 安全）的优先级规则。
4. **重新考虑的边界**：不是每次信念微变都要重新 deliberation，那样计算开销太大。应设定明确的触发阈值。
5. **可解释性优先**：BDI 的价值之一是让 Agent 的决策过程对人类可解释（"我因为相信 X，所以决定做 Y"）。
