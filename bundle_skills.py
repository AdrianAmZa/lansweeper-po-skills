#!/usr/bin/env python3
"""
PO Skills Bundle Builder
========================
Empaqueta todos los skills de un directorio en archivos .skill individuales
y genera un bundle ZIP listo para distribuir como GitHub Release o por Slack/Drive.

Uso:
    python bundle_skills.py <skills_dir> [--output <output_dir>] [--version <version>]

Ejemplo:
    python bundle_skills.py /mnt/skills/user --version 1.0.0
    python bundle_skills.py ./skills --output ./dist --version 2026-Q1
"""

import argparse
import fnmatch
import json
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import yaml

# ── Exclusion rules (same as official package_skill.py) ──────────────────────
EXCLUDE_DIRS = {"__pycache__", "node_modules", ".git"}
EXCLUDE_GLOBS = {"*.pyc"}
EXCLUDE_FILES = {".DS_Store", ".gitignore"}
ROOT_EXCLUDE_DIRS = {"evals"}


def should_exclude(rel_path: Path) -> bool:
    parts = rel_path.parts
    if any(part in EXCLUDE_DIRS for part in parts):
        return True
    if len(parts) > 1 and parts[1] in ROOT_EXCLUDE_DIRS:
        return True
    name = rel_path.name
    if name in EXCLUDE_FILES:
        return True
    return any(fnmatch.fnmatch(name, pat) for pat in EXCLUDE_GLOBS)


# ── Validation (inline, no external deps) ────────────────────────────────────
def validate_skill(skill_path: Path) -> tuple[bool, str, dict]:
    """Validate a skill folder. Returns (valid, message, metadata)."""
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return False, "SKILL.md not found", {}

    content = skill_md.read_text()
    if not content.startswith("---"):
        return False, "No YAML frontmatter found", {}

    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format", {}

    try:
        frontmatter = yaml.safe_load(match.group(1))
        if not isinstance(frontmatter, dict):
            return False, "Frontmatter must be a YAML dict", {}
    except yaml.YAMLError as e:
        return False, f"Invalid YAML: {e}", {}

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")

    if not name:
        return False, "Missing 'name' in frontmatter", {}
    if not description:
        return False, "Missing 'description' in frontmatter", {}

    return True, "Valid", {"name": name, "description": description}


# ── Package a single skill ────────────────────────────────────────────────────
def package_skill(skill_path: Path, output_dir: Path) -> Path | None:
    """Package one skill folder into a .skill (ZIP) file."""
    valid, msg, meta = validate_skill(skill_path)
    if not valid:
        print(f"  ⚠️  Skipping {skill_path.name}: {msg}")
        return None

    skill_filename = output_dir / f"{skill_path.name}.skill"
    file_count = 0

    with zipfile.ZipFile(skill_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file_path in sorted(skill_path.rglob("*")):
            if not file_path.is_file():
                continue
            arcname = file_path.relative_to(skill_path.parent)
            if should_exclude(arcname):
                continue
            zipf.write(file_path, arcname)
            file_count += 1

    print(f"  ✅ {skill_path.name}.skill ({file_count} files, {skill_filename.stat().st_size / 1024:.1f} KB)")
    return skill_filename


# ── Build the full bundle ─────────────────────────────────────────────────────
def build_bundle(skills_dir: Path, output_dir: Path, version: str):
    """Package all skills + create a combined bundle ZIP."""
    output_dir.mkdir(parents=True, exist_ok=True)
    individual_dir = output_dir / "individual"
    individual_dir.mkdir(exist_ok=True)

    # Discover skill folders (any dir containing SKILL.md)
    skill_folders = sorted(
        [d for d in skills_dir.iterdir() if d.is_dir() and (d / "SKILL.md").exists()]
    )

    if not skill_folders:
        print(f"❌ No skills found in {skills_dir}")
        sys.exit(1)

    print(f"📦 Found {len(skill_folders)} skills in {skills_dir}\n")

    # Package each skill individually
    packaged: list[Path] = []
    manifest_entries: list[dict] = []

    for folder in skill_folders:
        result = package_skill(folder, individual_dir)
        if result:
            packaged.append(result)
            _, _, meta = validate_skill(folder)
            manifest_entries.append({
                "name": meta["name"],
                "file": f"{folder.name}.skill",
                "description": meta["description"][:120] + ("..." if len(meta["description"]) > 120 else ""),
            })

    if not packaged:
        print("\n❌ No skills were packaged successfully.")
        sys.exit(1)

    # Create manifest
    manifest = {
        "bundle": "lansweeper-po-skills",
        "version": version,
        "created": datetime.now(timezone.utc).isoformat(),
        "skills_count": len(packaged),
        "skills": manifest_entries,
    }

    manifest_path = output_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False))

    # Create README for the bundle
    readme_lines = [
        f"# Lansweeper PO Skills Bundle v{version}",
        "",
        f"Generated: {manifest['created'][:10]}",
        f"Skills: {len(packaged)}",
        "",
        "## Installation",
        "",
        "Each `.skill` file can be installed individually in Claude.",
        "Drag and drop the `.skill` file into Claude's skill installer,",
        "or unzip it manually into your skills directory.",
        "",
        "## Included Skills",
        "",
        "| Skill | Description |",
        "|-------|-------------|",
    ]
    for entry in manifest_entries:
        readme_lines.append(f"| {entry['name']} | {entry['description']} |")

    readme_lines += [
        "",
        "## Architecture",
        "",
        "```",
        "Orchestration:  orchestrator-po",
        "Research:        jira-researcher, confluence-researcher, slack-researcher, figma-researcher",
        "Execution:       jira-ticket-creator, sprint-planner, stakeholder-communicator",
        "Output:          test-plan-creator, technical-writer",
        "```",
        "",
        "---",
        "Built with the PO Skills Bundle Builder.",
    ]

    readme_path = output_dir / "README.md"
    readme_path.write_text("\n".join(readme_lines))

    # Create the combined bundle ZIP
    bundle_name = f"lansweeper-po-skills-v{version}.zip"
    bundle_path = output_dir / bundle_name

    with zipfile.ZipFile(bundle_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        # Add individual .skill files
        for skill_file in sorted(individual_dir.iterdir()):
            zipf.write(skill_file, f"skills/{skill_file.name}")

        # Add manifest and README
        zipf.write(manifest_path, "manifest.json")
        zipf.write(readme_path, "README.md")

    bundle_size = bundle_path.stat().st_size / 1024

    print(f"\n{'='*50}")
    print(f"📦 Bundle ready: {bundle_name} ({bundle_size:.1f} KB)")
    print(f"   {len(packaged)} skills packaged")
    print(f"   Individual .skill files in: {individual_dir}")
    print(f"   Manifest: {manifest_path}")
    print(f"   README: {readme_path}")
    print(f"{'='*50}")

    return bundle_path


# ── CLI ───────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Package PO skills into a distributable bundle")
    parser.add_argument("skills_dir", help="Directory containing skill folders")
    parser.add_argument("--output", "-o", default="./dist", help="Output directory (default: ./dist)")
    parser.add_argument("--version", "-v", default=datetime.now().strftime("%Y.%m.%d"), help="Bundle version (default: YYYY.MM.DD)")
    args = parser.parse_args()

    build_bundle(
        skills_dir=Path(args.skills_dir),
        output_dir=Path(args.output),
        version=args.version,
    )


if __name__ == "__main__":
    main()
