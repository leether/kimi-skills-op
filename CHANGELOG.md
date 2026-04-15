# Changelog

所有显著变更都将记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，版本号遵循 [Semantic Versioning](https://semver.org/lang/zh-CN/)。

---

## [Unreleased]

## [0.1.0] - 2026-04-15

### Added
- 创建 `README.md`、`CONTRIBUTING.md`、`CHANGELOG.md` 和 `LICENSE`，建立开源仓库治理骨架。
- 新增 `skills/` 目录，收录 6 个可复用的 Kimi Flow Skills：
  - `bdi-agent` | `programmatic-tools` | `repo-privacy-gate`
  - `self-consistency-gate` | `kimi-skills-governance` | `kimi-skills-op-loop`

### Changed
- `.gitignore` 增加对本地记忆、环境变量文件和敏感密钥的排除规则。
- 项目名从 `this-computer` 正式更新为 `kimi-skills-op`。

### Removed
- 移除 `BASELINE.md` 和 `ACCEPTANCE_REPORT.md`，使仓库聚焦为通用 Skills 共享仓库。
- 移除 `system-audit` 和 `project-onboarding`，将仓库边界收紧为 **Skills 运维工具集**。
