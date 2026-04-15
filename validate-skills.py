#!/usr/bin/env python3
"""
Kimi Skills OP - Validation Gate
Combines self-consistency-gate + repo-privacy-gate logic for CI and local use.
"""
import glob
import os
import re
import sys
import yaml
from collections import defaultdict

SKILLS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "skills")

def fail(msg):
    print(f"❌ {msg}")
    return 1

def pass_msg(msg):
    print(f"✅ {msg}")
    return 0

def warn(msg):
    print(f"⚠️  {msg}")
    return 0

def main():
    exit_code = 0
    paths = sorted(glob.glob(os.path.join(SKILLS_DIR, "*/SKILL.md")))

    if not paths:
        print("No skills found.")
        return 1

    print(f"Found {len(paths)} skill(s) to validate.\n")

    skills = {}
    trigger_map = defaultdict(list)
    name_set = {}
    issues = {"high": [], "medium": [], "low": []}
    router_skills = set()

    # ─────────────────────────────────────────────────────────────
    # 1. Parse and validate structure
    # ─────────────────────────────────────────────────────────────
    for path in paths:
        dir_name = os.path.basename(os.path.dirname(path))
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        lines = text.splitlines()
        line_count = len(lines)

        fm = {}
        if text.startswith("---"):
            parts = text.split("---", 2)
            if len(parts) >= 3:
                try:
                    fm = yaml.safe_load(parts[1]) or {}
                except Exception as e:
                    fm = {"_error": str(e)}

        name = fm.get("name", "")
        stype = fm.get("type", "skill")
        triggers = fm.get("triggers", [])
        description = fm.get("description", "")

        is_router = any(kw in description for kw in ["映射", "路由", "快捷口令", "快捷入口"])
        if is_router:
            router_skills.add(name)

        skills[name] = {
            "dir": dir_name,
            "name": name,
            "type": stype,
            "triggers": triggers,
            "description": description,
            "line_count": line_count,
            "path": path,
            "has_mermaid": "```mermaid" in text and ("flowchart" in text or "graph " in text),
            "has_begin_end": "BEGIN" in text and "END" in text,
            "is_router": is_router,
        }

        # Directory name check
        if dir_name != name:
            issues["medium"].append(f"[{name}] directory name '{dir_name}' does not match 'name'")
        else:
            pass_msg(f"[{name}] directory name matches skill name")

        # Name uniqueness
        if name in name_set:
            issues["high"].append(f"[{name}] duplicate name: already exists at {name_set[name]}")
        else:
            name_set[name] = path

        # Frontmatter fields
        for field in ("name", "description", "triggers"):
            if field not in fm:
                issues["high"].append(f"[{name}] missing frontmatter field: '{field}'")
            else:
                pass_msg(f"[{name}] frontmatter field '{field}' present")

        # Triggers count
        if len(triggers) < 3:
            issues["medium"].append(f"[{name}] only {len(triggers)} triggers (minimum 3)")
        else:
            pass_msg(f"[{name}] has {len(triggers)} triggers")

        for t in triggers:
            trigger_map[t].append(name)

        # Flow checks
        if stype == "flow":
            if not skills[name]["has_mermaid"]:
                issues["high"].append(f"[{name}] type=flow but missing Mermaid diagram")
            else:
                pass_msg(f"[{name}] Mermaid diagram present")
            if skills[name]["has_mermaid"] and not skills[name]["has_begin_end"]:
                issues["medium"].append(f"[{name}] Flow Skill missing BEGIN/END nodes")
            elif skills[name]["has_mermaid"]:
                pass_msg(f"[{name}] BEGIN/END nodes present")

        # Line count
        if line_count > 1000:
            issues["medium"].append(f"[{name}] {line_count} lines (max 1000)")
        else:
            pass_msg(f"[{name}] {line_count} lines (within limit)")

        # Description length
        if len(description) < 20:
            issues["low"].append(f"[{name}] description too short: {len(description)} chars")

    # ─────────────────────────────────────────────────────────────
    # 2. Trigger conflicts (self-consistency-gate)
    # ─────────────────────────────────────────────────────────────
    for t, names in trigger_map.items():
        if len(names) <= 1:
            continue
        routers = [n for n in names if n in router_skills]
        non_routers = [n for n in names if n not in router_skills]

        if len(non_routers) > 1:
            issues["high"].append(f"trigger conflict '{t}' used by {len(names)} skills: {', '.join(names)}")
        elif routers and len(non_routers) == 1:
            if len(t) <= 4:
                issues["medium"].append(f"trigger overlap '{t}' (router {', '.join(routers)} vs {', '.join(non_routers)})")
            else:
                issues["high"].append(f"trigger conflict '{t}' is a long phrase shared with router: {', '.join(names)}")
        elif len(routers) > 1:
            issues["medium"].append(f"trigger '{t}' used by multiple routers: {', '.join(routers)}")

    if not any("trigger conflict" in i or "trigger overlap" in i for i in issues["high"] + issues["medium"]):
        pass_msg("no trigger conflicts detected")

    # ─────────────────────────────────────────────────────────────
    # 3. Privacy gate scan (repo-privacy-gate)
    # ─────────────────────────────────────────────────────────────
    REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
    PATTERNS = {
        "username_lize": re.compile(r'\blize\b', re.I),
        "hostname_mymac": re.compile(r'\bmymac\b', re.I),
        "serial_like": re.compile(r'\b[A-Z0-9]{11,13}\b'),
        "email_like": re.compile(r'[\w.-]+@[\w.-]+\.\w+'),
        "ip_private": re.compile(r'\b(10\.\d{1,3}\.\d{1,3}\.\d{1,3}|172\.(1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3})\b'),
        "abs_home_mac": re.compile(r'/Users/[^\s/<>"\'\n]+'),
        "ssh_key": re.compile(r'-----BEGIN (RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----'),
    }

    leaks = []
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in {".git", "__pycache__", ".github"}]
        for f in files:
            path = os.path.join(root, f)
            # Skip git worktree pointer file and this script itself
            if os.path.basename(path) in {".git", "validate-skills.py"}:
                continue
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                    for lineno, line in enumerate(fh, 1):
                        for pname, pat in PATTERNS.items():
                            for m in pat.finditer(line):
                                snippet = m.group(0)
                                if pname == "abs_home_mac" and snippet == "/Users/<username>":
                                    continue
                                if pname == "serial_like" and not re.search(r'\d', snippet):
                                    continue
                                rel = os.path.relpath(path, REPO_ROOT)
                                leaks.append(f"{rel}:{lineno} ({pname}: {snippet})")
            except Exception:
                pass

    if leaks:
        for leak in leaks:
            issues["high"].append(f"[Privacy] {leak}")
    else:
        pass_msg("no PII/path leaks detected")

    # ─────────────────────────────────────────────────────────────
    # 4. Report summary
    # ─────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("Validation Summary")
    print("=" * 60)

    high_count = len(issues["high"])
    medium_count = len(issues["medium"])
    low_count = len(issues["low"])

    print(f"\nHigh severity issues: {high_count}")
    for i in issues["high"]:
        print(f"  ❌ {i}")
        exit_code = 1

    print(f"\nMedium severity issues: {medium_count}")
    for i in issues["medium"]:
        print(f"  ⚠️  {i}")

    print(f"\nLow severity issues: {low_count}")
    for i in issues["low"]:
        print(f"  ℹ️  {i}")

    print("\n" + "=" * 60)
    if exit_code == 0:
        print("RESULT: PASSED — all critical checks passed")
    else:
        print("RESULT: FAILED — fix high-severity issues before merging")
    print("=" * 60)

    return exit_code

if __name__ == "__main__":
    sys.exit(main())
