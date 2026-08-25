#!/usr/bin/env python3
"""
FinGuard AI — Comprehensive Meaningful LOC Measurement Tool.
Calculates exact source, test, infrastructure, script, and documentation lines of code
while strictly excluding comments, blank lines, vendor modules, and generated artifacts.
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple

LANGUAGE_MAP = {
    ".py": "Python",
    ".ts": "TypeScript",
    ".tsx": "TypeScript (React)",
    ".js": "JavaScript",
    ".jsx": "JavaScript (React)",
    ".css": "CSS",
    ".scss": "SCSS",
    ".sql": "SQL",
    ".json": "JSON",
    ".yaml": "YAML",
    ".yml": "YAML",
    ".toml": "TOML",
    ".sh": "Shell",
    ".ps1": "PowerShell",
    ".tf": "Terraform",
    ".md": "Markdown",
    ".dockerfile": "Dockerfile",
    "Dockerfile": "Dockerfile",
}

IGNORE_DIRS = {
    ".git",
    ".github",
    "node_modules",
    "venv",
    ".venv",
    "env",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "dist",
    "build",
    "coverage",
    ".next",
    "target",
    ".idea",
    ".vscode",
    "data_cache",
    "artifacts",
}

IGNORE_FILES = {
    "package-lock.json",
    "pnpm-lock.yaml",
    "yarn.lock",
    "poetry.lock",
}

def is_comment_or_blank(line: str, ext: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return True
    if ext in [".py", ".sh", ".ps1", ".yaml", ".yml", ".toml", ".tf", "Dockerfile"]:
        if stripped.startswith("#"):
            return True
    if ext in [".ts", ".tsx", ".js", ".jsx", ".css", ".scss", ".sql"]:
        if stripped.startswith("//") or stripped.startswith("/*") or stripped.startswith("*") or stripped.startswith("--"):
            return True
    return False

def categorize_path(file_path: Path) -> str:
    path_str = str(file_path).replace("\\", "/").lower()
    ext = file_path.suffix.lower()

    if "tests/" in path_str or "test_" in path_str or ".test." in path_str or ".spec." in path_str:
        if ext == ".py":
            return "Python test LOC"
        elif ext in [".ts", ".tsx", ".js", ".jsx"]:
            return "Frontend test LOC"
        return "Other test LOC"
    if "migrations/" in path_str or ext == ".sql":
        return "SQL/migration LOC"
    
    if "docs/" in path_str or ext == ".md":
        return "Documentation LOC"
    
    if any(k in path_str for k in ["infrastructure/", "docker/", "nginx/", "monitoring/", "aws/", ".tf", "dockerfile"]):
        return "Infrastructure LOC"
    
    if "scripts/" in path_str or "apps/cli" in path_str:
        return "Scripts/CLI LOC"

    if ext == ".py":
        return "Python production LOC"
    
    if ext in [".ts", ".tsx", ".js", ".jsx", ".css", ".scss"]:
        return "TypeScript/React LOC"
    
    return "Other source LOC"

def count_finguard_loc(root_dir: Path) -> Tuple[Dict[str, int], Dict[str, int], int, int, int]:
    categories = {
        "Python production LOC": 0,
        "Python test LOC": 0,
        "TypeScript/React LOC": 0,
        "Frontend test LOC": 0,
        "SQL/migration LOC": 0,
        "Infrastructure LOC": 0,
        "Scripts/CLI LOC": 0,
        "Documentation LOC": 0,
    }
    language_counts = {}
    total_meaningful = 0
    total_source = 0
    total_test = 0

    for current_root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            if file in IGNORE_FILES:
                continue

            file_path = Path(current_root) / file
            ext = file_path.suffix.lower()
            if file == "Dockerfile" or file.startswith("Dockerfile."):
                ext = "Dockerfile"

            if ext not in LANGUAGE_MAP and file != "Dockerfile":
                continue

            lang = LANGUAGE_MAP.get(ext, ext)
            cat = categorize_path(file_path)

            lines_count = 0
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        if not is_comment_or_blank(line, ext):
                            lines_count += 1
            except Exception:
                continue

            if lines_count > 0:
                categories[cat] = categories.get(cat, 0) + lines_count
                language_counts[lang] = language_counts.get(lang, 0) + lines_count
                total_meaningful += lines_count

                if "test" in cat.lower():
                    total_test += lines_count
                elif cat != "Documentation LOC":
                    total_source += lines_count

    return categories, language_counts, total_source, total_test, total_meaningful

def print_loc_report(root_dir: Path):
    categories, language_counts, total_source, total_test, total_meaningful = count_finguard_loc(root_dir)

    print("=" * 80)
    print("       FINGUARD AI — ENTERPRISE CODEBASE METRICS & AUDIT REPORT       ")
    print("=" * 80)
    print(f"Target Root: {root_dir}")
    print("-" * 80)
    print("MEANINGFUL LINES OF CODE BY DOMAIN CATEGORY:")
    for cat, count in categories.items():
        pct = (count / total_meaningful * 100.0) if total_meaningful > 0 else 0.0
        print(f"  * {cat:<28}: {count:>8,} LOC ({pct:>5.1f}%)")
    print("-" * 80)
    print("SUMMARY TOTALS:")
    print(f"  * TOTAL SOURCE LOC        : {total_source:>8,} LOC")
    print(f"  * TOTAL TEST LOC          : {total_test:>8,} LOC")
    print(f"  * TOTAL MEANINGFUL LOC    : {total_meaningful:>8,} LOC")
    print("-" * 80)
    print("LINES OF CODE BY LANGUAGE:")
    for lang, count in sorted(language_counts.items(), key=lambda x: x[1], reverse=True):
        pct = (count / total_meaningful * 100.0) if total_meaningful > 0 else 0.0
        print(f"  * {lang:<28}: {count:>8,} LOC ({pct:>5.1f}%)")
    print("=" * 80)
    
    target = 100000
    if total_meaningful >= target:
        print(f"STATUS: [PASSED] Meets and exceeds 100,000 LOC target ({total_meaningful:,} / {target:,})")
    else:
        prog = (total_meaningful / target) * 100.0
        print(f"STATUS: [IN PROGRESS] Milestone progress: {prog:.2f}% ({total_meaningful:,} / {target:,} LOC)")
    print("=" * 80)

if __name__ == "__main__":
    target_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    print_loc_report(target_path)
