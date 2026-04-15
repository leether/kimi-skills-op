# kimi-skills-op

> 一套面向 Kimi Skills 生态的 BDI-based 运维工具集。

本仓库聚焦 **"如何设计、编写、检查、治理一个高质量的 Skills 仓库"**。收录的 6 个 Skill 覆盖了从认知框架、编写技巧、发布前检查、维护期自洽、社区治理到**闭环 orchestration** 的完整生命周期。所有 Skill 均遵循统一的 `SKILL.md` 开放标准，欢迎社区贡献。

---

## 📁 项目结构

```
.
├── README.md              # 本文件
├── LICENSE                # 开源协议
├── CONTRIBUTING.md        # 贡献指南
├── CHANGELOG.md           # 变更日志
└── skills/                # Kimi Skills 运维工具集
```

---

## 🧠 核心理念

### BDI 框架

每一个 Skill 的设计和审查都遵循三层认知模型：

- **Belief（信念）**：对当前 Skills 库状态的准确认知
- **Desire（愿望）**：对理想 Skills 生态的明确目标
- **Intention（意图）**：可执行、可验证的治理与优化动作

### Kimi Skills 方法论

- 所有重复性任务沉淀为 **Skills**（`SKILL.md`）
- 复杂流程使用 **Flow Skills**（`type: flow` + Mermaid 流程图）
- 记忆与上下文通过 **Global + Local 双层记忆系统** 管理

---

## 🧩 已收录 Skills

| Skill | 类型 | 描述 |
|-------|------|------|
| [`bdi-agent`](./skills/bdi-agent/SKILL.md) | Skill | BDI（信念-愿望-意图）分析框架 |
| [`programmatic-tools`](./skills/programmatic-tools/SKILL.md) | Skill | 程序化工具调用（PTC）方法论 |
| [`repo-privacy-gate`](./skills/repo-privacy-gate/SKILL.md) | Flow | 公开仓库隐私安全合规检查门 |
| [`self-consistency-gate`](./skills/self-consistency-gate/SKILL.md) | Flow | Skills 库自洽性检查门（元治理） |
| [`kimi-skills-governance`](./skills/kimi-skills-governance/SKILL.md) | Flow | 开源仓库治理工作流 |
| [`kimi-skills-op-loop`](./skills/kimi-skills-op-loop/SKILL.md) | Flow | **运维闭环 orchestration** |

### 生命周期对应关系

```
设计阶段      →  bdi-agent
编写阶段      →  programmatic-tools
发布前检查    →  repo-privacy-gate
维护期检查    →  self-consistency-gate
社区治理      →  kimi-skills-governance
闭环 orchestration → kimi-skills-op-loop
```

`kimi-skills-op-loop` 不是另一个孤立的工具，而是把前 5 个 Skill 编织成**可持续运转系统的元工作流**。

---

## 🤝 如何贡献

我们欢迎所有与 **Skills 设计、检查、治理** 相关的改进建议！

- 📖 请先阅读 [`CONTRIBUTING.md`](./CONTRIBUTING.md)
- 🐛 提交 Issue 报告问题或分享优化思路
- 🔀 提交 PR 补充新的 Skill 或改进现有文档

---

## 📜 许可证

本仓库采用 [MIT License](./LICENSE) 开源。
