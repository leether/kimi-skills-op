# this-computer

> 一个基于 BDI（Belief-Desire-Intention）框架和 Kimi Skills 方法论的系统优化与知识沉淀项目。

本项目记录了一套 macOS 开发环境的系统级优化实践，以及多个可复用的 Kimi Flow Skills。所有优化过程、验收标准和知识资产均以结构化方式沉淀，方便复现、迭代和社区贡献。

---

## 📁 项目结构

```
.
├── README.md              # 本文件
├── LICENSE                # 开源协议
├── CONTRIBUTING.md        # 贡献指南
├── CHANGELOG.md           # 变更日志
└── skills/                # 可复用的 Kimi Flow Skills
```

---

## 🧠 核心理念

### BDI 框架

每一个系统优化决策和 Skill 设计都遵循三层认知模型：

- **Belief（信念）**：对当前系统状态的准确认知
- **Desire（愿望）**：对理想系统状态的明确目标
- **Intention（意图）**：可执行、可验证的具体行动计划

### Kimi Skills 方法论

- 所有重复性任务沉淀为 **Skills**（`SKILL.md`）
- 复杂流程使用 **Flow Skills**（`type: flow` + Mermaid 流程图）
- 记忆与上下文通过 **Global + Local 双层记忆系统** 管理

---

## 🛠️ 优化成果概览

| 维度 | 优化内容 | 状态 |
|------|---------|------|
| 系统清理 | 释放 ~4GB 空间，删除僵尸 LaunchAgents | ✅ 已完成 |
| Shell 增强 | Starship + zsh-autosuggestions + 现代别名 | ✅ 已完成 |
| Node 管理 | 统一为 fnm，清理旧 nvm | ✅ 已完成 |
| Python 环境 | 移除冗余 env，恢复系统 `python3` | ✅ 已完成 |
| Docker 迁移 | 卸载旧 Docker Desktop，安装 Colima + docker v29 CLI | 🟡 待首次启动验证 |
| 安全加固 | API Keys 迁移至 `~/.zshenv`，删除未使用应用 | ✅ 已完成 |
| 记忆系统 | 全局记忆中枢 + 项目级本地记忆 | ✅ 已完成 |

---

## 🧩 已收录 Skills

| Skill | 类型 | 描述 |
|-------|------|------|
| [`bdi-agent`](./skills/bdi-agent/SKILL.md) | Skill | BDI（信念-愿望-意图）分析框架 |
| [`programmatic-tools`](./skills/programmatic-tools/SKILL.md) | Skill | 程序化工具调用（PTC）方法论 |
| [`project-onboarding`](./skills/project-onboarding/SKILL.md) | Flow | 新项目初始化工作流 |
| [`system-audit`](./skills/system-audit/SKILL.md) | Flow | macOS 系统审计与清理工作流 |
| [`repo-privacy-gate`](./skills/repo-privacy-gate/SKILL.md) | Flow | 公开仓库隐私安全合规检查门 |
| [`self-consistency-gate`](./skills/self-consistency-gate/SKILL.md) | Flow | Skills 库自洽性检查门（元治理） |
| [`kimi-skills-governance`](./skills/kimi-skills-governance/SKILL.md) | Flow | 开源仓库治理工作流 |

---

## 🤝 如何贡献

我们欢迎所有基于 BDI 框架的改进建议和 Skill 分享！

- 📖 请先阅读 [`CONTRIBUTING.md`](./CONTRIBUTING.md)
- 🐛 提交 Issue 报告问题或分享优化思路
- 🔀 提交 PR 补充新的 Skill 或改进现有文档

---

## 📜 许可证

本项目采用 [MIT License](./LICENSE) 开源。

---

> **温馨提示**：本项目中的系统路径和身份信息已做脱敏处理。在参考和复现时，请根据自己的实际环境替换相关变量。
