# 贡献指南

感谢你对 `kimi-skills-op` 项目的关注！

本仓库是一个基于 **BDI（Belief-Desire-Intention）框架** 和 **Kimi Skills 方法论** 的运维工具集，聚焦 **"如何设计、编写、检查、治理一个高质量的 Skills 仓库"**。我们欢迎所有建设性的贡献。

---

## 📋 提交前必读

1. **理解项目定位**：
   - 本仓库是 **Skills 运维工具集**，不是通用技能超市。
   - 核心目标是帮助 contributor 和 maintainer 产出**结构一致、隐私安全、可持续维护**的 Skill。

2. **阅读现有 Skill**：
   - 请先浏览 [`skills/`](./skills/) 目录，避免与现有 Skill 高度重复。

3. **保持脱敏原则**：
   - 所有提交到本仓库的内容**不得包含**真实的 API Keys、私钥、主机名、序列号、用户名、内部 IP 等敏感信息。
   - 请使用占位符，如 `<hostname>`、`<username>`、`<internal-ip>`、`<serial-number>`。

---

## 🎯 我们欢迎的贡献类型

| 类型 | 示例 | 建议方式 |
|------|------|---------|
| **文档改进** | 修正错误、补充说明、优化排版 | 直接提 PR |
| **优化建议** | 针对现有 Skill 提出更优方案 | 先提 Issue 讨论 |
| **Skill 分享** | 与 Skills 设计/检查/治理相关的新 Flow Skill | 直接提 PR |
| **问题反馈** | 发现文档中的矛盾、过时内容 | 提 Issue |
| **翻译** | 将核心文档翻译为其他语言 | 直接提 PR |

---

## 🚫 我们不接受的贡献

- 包含未脱敏敏感信息的提交
- 与本项目定位无关的商业推广
- 恶意代码、攻击性内容或政治敏感内容
- 仅做格式调整但无实质改进的大量 PR（如批量修改标点）

---

## 🔄 提交流程

1. **Fork 本仓库**
2. **创建功能分支**：`git checkout -b feat/your-skill-name`
3. **本地验证**：
   ```bash
   python validate-skills.py
   ```
   确保高严重度问题（🔴）为 0 项后再提交 PR。
4. **提交清晰 commit**：
   - `docs:` 文档改进
   - `fix:` 错误修正
   - `feat:` 新增 Skill 或功能
   - `chore:` 杂项维护
5. **推送到你的 Fork 并提交 PR**
6. **等待审查**：PR 会自动触发 GitHub Actions 的 `PR Gate` 检查，maintainer 会在此基础上进行 BDI 框架质量审查

---

## 📝 Commit Message 规范

```
<type>: <简短描述>

<详细说明（可选）>
```

示例：
```
feat: add skill-scaffold for rapid skill prototyping

新增一个 Flow Skill，帮助 contributor 在 5 分钟内生成
符合标准的 SKILL.md 骨架，降低创作门槛。
```

---

## ⏱️ 审查时效

- 文档类 PR：通常 3-5 天内反馈
- 需要讨论的方案类 Issue：通常 7 天内回复
- 修改后重审：通常 24-48 小时内反馈

---

## 💬 行为准则

- 尊重不同水平的贡献者
- 反馈必须建设性
- 有争议的内容通过 Issue 公开讨论
- 维护者保留对 PR 的最终合并决定权

---

如有疑问，欢迎先开一个 Issue 讨论！
