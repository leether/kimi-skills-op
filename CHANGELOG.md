# Changelog

所有显著变更都将记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，版本号遵循 [Semantic Versioning](https://semver.org/lang/zh-CN/)。

---

## [Unreleased]

### Added
- 创建 `README.md`，说明项目定位、核心理念和优化成果概览。
- 创建 `CONTRIBUTING.md`，定义贡献类型、提交规范和行为准则。
- 创建 `CHANGELOG.md`，建立变更日志规范。
- 新增 `skills/` 目录，收录 7 个可复用的 Kimi Flow Skills：
  - `bdi-agent` | `programmatic-tools` | `project-onboarding` | `system-audit`
  - `repo-privacy-gate` | `self-consistency-gate` | `kimi-skills-governance`

### Changed
- `.gitignore` 增加对本地记忆、环境变量文件和敏感密钥的排除规则。
- 项目名从 `this-computer` 正式更新为 `bdi-flow-skills`，README、CONTRIBUTING、LICENSE 已同步更新。

### Removed
- 移除 `BASELINE.md` 和 `ACCEPTANCE_REPORT.md`，使 `share` 分支聚焦为通用 Skills 共享仓库。
- 移除 `system-audit` 和 `project-onboarding`，将仓库边界收紧为 **Skills 运维工具集**。

---

## [0.1.0] - 2026-04-15

### Added
- 初始提交：包含系统基线文档 `BASELINE.md` 和验收测试报告 `ACCEPTANCE_REPORT.md`。
- 记录了 macOS 系统优化、Shell 增强、Node/Python/Docker 环境整理、安全加固和记忆系统建设的完整过程。
