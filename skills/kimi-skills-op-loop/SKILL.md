---
name: kimi-skills-op-loop
description: 基于 BDI 的 Kimi Skills 运维闭环工作流。指导如何使用 `kimi-skills-op` 工具集实现自我设计、自我检查、自我治理的可持续循环。当用户说"闭环设计"、"运维闭环"、"skills闭环"、"自我维护"、"可持续循环"、"op loop"时触发。
type: flow
triggers:
  - 闭环设计
  - 运维闭环
  - skills闭环
  - 自我维护
  - 可持续循环
  - op loop
  - 运维循环
  - 循环设计
  - 自洽循环
  - 治理闭环
---

# Kimi Skills 运维闭环（Ops Loop）

> 核心理念：**一个健康的 Skills 仓库不是静态的收藏夹，而是一个能够自我设计、自我检查、自我治理的活系统。**

本工作流定义了 `kimi-skills-op` 工具集的**闭环运行方式**。5 个 Skill 不是孤立的工具，而是一个有机循环的 5 个节点。每一次仓库迭代都应沿着这个环流动，最终回到起点，等待下一次触发。

---

## BDI 框架映射

### Belief（信念）—— 我对当前循环状态的认知

- **循环是否完整**：5 个节点是否全部可用？最近一次完整循环是什么时候？
- **循环阻塞点**：哪个节点最容易失败？（通常是 self-consistency-gate 发现冲突，或 repo-privacy-gate 发现残留）
- **循环频率**：多久执行一次 self-consistency-gate？每次发布前是否都执行 repo-privacy-gate？
- **循环输入源**：Issue、新想法、自检查结果、还是治理审查中的反馈？

### Desire（愿望）—— 我希望闭环达到什么状态

- **D1 全自动化**：理想状态下，从"发现需求"到"发布更新"尽可能由 Skill 驱动，减少人工遗忘。
- **D2 零冲突释放**：每次推送到 GitHub 之前，self-consistency-gate 和 repo-privacy-gate 必须全部绿灯。
- **D3 自增强**：闭环每运行一圈，仓库质量应该比上一圈更高（文档更完整、冲突更少、结构更统一）。
- **D4 可追溯**：每一次循环的触发原因、执行动作、验证结果都有记录（Changelog / Git history）。

### Intention（意图）—— 我承诺执行的闭环动作

1. **任何变更都从 BDI 分析开始**（`bdi-agent`）
2. **任何批量检查都用脚本化实现**（`programmatic-tools`）
3. **每次提交前都经过自洽性扫描**（`self-consistency-gate`）
4. **每次推送前都经过隐私安全门**（`repo-privacy-gate`）
5. **每次合并都遵循治理规范**（`kimi-skills-governance`）

---

## 闭环流程图

```mermaid
flowchart TD
    A([BEGIN: 触发源]) --> B{触发类型?}
    B -->|新需求 / 新 Skill 想法| C1[bdi-agent<br/>BDI 分析]
    B -->|批量检查 / 数据扫描| C2[programmatic-tools<br/>脚本化实现]
    B -->|准备发布 / 推送前| C3[repo-privacy-gate<br/>隐私安全门]
    B -->|日常维护 / 新增 Skill 后| C4[self-consistency-gate<br/>自洽性检查]
    B -->|PR 审查 / 版本发布| C5[kimi-skills-governance<br/>社区治理]

    C1 --> D[本地实现与验证]
    C2 --> D
    D --> C4
    C4 --> E{是否通过?}
    E -->|否| F[修复冲突/结构问题]
    F --> C4
    E -->|是| C3
    C3 --> G{是否通过?}
    G -->|否| H[脱敏 / 清理残留]
    H --> C3
    G -->|是| I[提交 Commit]
    I --> C5
    C5 --> J{是否需要迭代?}
    J -->|是| K[记录反馈 / 生成新 Issue]
    K --> A
    J -->|否| L[更新 CHANGELOG<br/>打 Tag / Release]
    L --> M([END])
    M -.->|新触发源出现.-> A
```

---

## 节点说明

### A: 触发源（Trigger Sources）

闭环不是凭空启动的，它由以下 4 类事件触发：

| 触发源 | 示例 | 首选入口 |
|--------|------|---------|
| **外部需求** | 用户说"帮我做一个新 Skill" | `bdi-agent` → `programmatic-tools` |
| **内部检查** | 新增 Skill 后想验证一致性 | `self-consistency-gate` |
| **发布前焦虑** | "我要 push 了，会不会泄露什么？" | `repo-privacy-gate` |
| **社区事件** | 收到 PR / Issue | `kimi-skills-governance` |

> 💡 **关键洞察**：`self-consistency-gate` 和 `kimi-skills-governance` 的输出（发现的问题、审查反馈）本身就是**新的触发源**，会重新输入到闭环的起点。这就是"闭环"的本质。

---

### C1: bdi-agent（设计层）

**职责**：为任何新 Skill 建立清晰的认知框架。

**执行 checklist**：
- [ ] 这个新 Skill 的 **Belief** 是什么？（它解决什么问题？现状如何？）
- [ ] 这个新 Skill 的 **Desire** 是什么？（理想结果是什么？质量标准？）
- [ ] 这个新 Skill 的 **Intention** 是什么？（具体可执行的步骤？）
- [ ] 如果是 Flow Skill，是否已经想好 Mermaid 流程图的主干？
- [ ] 触发词是否至少覆盖 3 个自然语言表达？

**输出**：一份 BDI 设计草图，作为后续实现的输入。

---

### C2: programmatic-tools（实现层）

**职责**：在需要批量处理、扫描、统计时，优先用脚本代替多步工具调用。

**典型场景**：
- 批量解析所有 `SKILL.md` 的 frontmatter
- 统计触发词分布、生成热力图
- 自动化格式化检查（行数、编码、空行）
- 生成 README 中的 Skills 索引表

**执行 checklist**：
- [ ] 这个任务是否涉及"读多个文件 → 提取 → 计算 → 输出"？
- [ ] 是否可以用 Python 脚本一次性完成？
- [ ] 脚本是否只读取不修改生产文件（或修改前已确认）？
- [ ] 脚本失败两次后是否有回退到手动检查的方案？

---

### D: 本地实现与验证

**职责**：在调用大门技能之前，先在本地跑通新 Skill 或修复。

**最小验证集**：
1. `SKILL.md` 能被正常解析（YAML frontmatter 无语法错误）
2. 触发词数量 ≥ 3
3. 如果是 Flow，Mermaid 代码块包含 `BEGIN` 和 `END`
4. 文件大小 ≤ 1000 行
5. 复制到 `~/.kimi/skills/` 后，通过口头触发词能被 Agent 识别（人工模拟）

---

### C4: self-consistency-gate（维护层）

**职责**：确保整个 Skills 库在结构和语义上协调一致。

**触发时机**：
- 每次新增或修改 Skill 后
- 每周例行维护（可选）
- 发布版本前（强制）

**通过标准**：
- 🔴 严重问题：0 项
- 🟡 中等问题：≤ 2 项（且必须映射中心相关的短词重叠）
- 🟢 轻微问题：任意

**未通过时的循环动作**：修复问题 → 重新运行 `self-consistency-gate` → 直到通过。

---

### C3: repo-privacy-gate（安全层）

**职责**：在代码离开本地、进入公开互联网之前，执行最后一道隐私安检。

**触发时机**：
- 每次 `git push` 到 GitHub 之前（强制）
- 每次从 `main` 向 `share` 同步内容之前（强制）

**通过标准**：
- 🔴 高危泄露（密钥/私钥/未脱敏系统路径）：0 项
- 🟡 中危泄露（PII/主机名/内网 IP）：0 项
- 🟢 低危：任意

**关键红线**：`.git` 历史中的残留比工作目录中的残留更危险。如果发现历史中有未脱敏内容，必须重写历史（`git switch --orphan` 或 `git filter-branch`）。

---

### C5: kimi-skills-governance（治理层）

**职责**：管理社区贡献、维护文档、发布版本。

**触发时机**：
- 收到外部 PR 时
- 累积足够改进后准备发版时
- Issue 分类和回应时

**通过标准**：
- PR 符合 `CONTRIBUTING.md` 规范
- 已通过 `self-consistency-gate` 和 `repo-privacy-gate`
- README / CHANGELOG 已同步更新

**循环输出**：
- 审查反馈可能成为新 Issue（返回 A）
- 版本发布为下一轮迭代设定新起点（END → 等待 A）

---

## 循环执行频率建议

| 节点 | 执行频率 | 说明 |
|------|---------|------|
| `bdi-agent` | 按需 | 每次新 Skill / 重大重构前 |
| `programmatic-tools` | 按需 | 遇到批量任务时 |
| `self-consistency-gate` | **每次修改后 + 发版前** | 日常维护的核心节拍器 |
| `repo-privacy-gate` | **每次 push 前** | 不可妥协的安全底线 |
| `kimi-skills-governance` | 收到 PR 时 / 有发版需求时 | 社区交互的节拍器 |

---

## 一句话闭环原则

> **设计时用 BDI，实现时用脚本，提交前查自洽，推送前查隐私，合并时守治理。**
>
> 每一个出口的绿灯，都是下一个入口的触发条件。
