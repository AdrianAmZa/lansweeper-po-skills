#!/usr/bin/env bash
# ============================================================================
# release.sh — Commit, push, build bundle, and create GitHub Release
# Usage: ./release.sh <version>
# Example: ./release.sh 1.0.0
# ============================================================================
set -euo pipefail

VERSION="${1:?Usage: ./release.sh <version>}"
TAG="v${VERSION}"
REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
DIST_DIR="${REPO_DIR}/dist"

echo "═══════════════════════════════════════════════"
echo "  Lansweeper PO Skills — Release ${TAG}"
echo "═══════════════════════════════════════════════"
echo ""

# ── Pre-flight checks ──────────────────────────────
command -v gh >/dev/null 2>&1 || { echo "❌ GitHub CLI (gh) not found. Install: brew install gh"; exit 1; }
command -v git >/dev/null 2>&1 || { echo "❌ git not found."; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo "❌ python3 not found."; exit 1; }
python3 -c "import yaml" 2>/dev/null || { echo "❌ PyYAML not found. Install: pip install pyyaml"; exit 1; }

# Check we're in a git repo
cd "${REPO_DIR}"
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || { echo "❌ Not a git repo. Run 'git init' first."; exit 1; }

# Check gh is authenticated
gh auth status >/dev/null 2>&1 || { echo "❌ GitHub CLI not authenticated. Run: gh auth login"; exit 1; }

# ── Step 1: Git commit & push ──────────────────────
echo "📝 Step 1/3 — Commit & push"
git add -A
if git diff --cached --quiet; then
    echo "   No changes to commit, skipping."
else
    git commit -m "release: ${TAG} — PO Skills Bundle"
    echo "   ✅ Committed"
fi
git push origin main
echo "   ✅ Pushed to origin/main"
echo ""

# ── Step 2: Build bundle ──────────────────────────
echo "📦 Step 2/3 — Build bundle"
rm -rf "${DIST_DIR}"
python3 "${REPO_DIR}/bundle_skills.py" "${REPO_DIR}/skills" --output "${DIST_DIR}" --version "${VERSION}"
echo ""

# ── Step 3: Create GitHub Release ─────────────────
echo "🚀 Step 3/3 — Create GitHub Release"

# Collect all .skill files
SKILL_FILES=()
for f in "${DIST_DIR}/individual/"*.skill; do
    [ -f "$f" ] && SKILL_FILES+=("$f")
done

gh release create "${TAG}" \
    "${DIST_DIR}/lansweeper-po-skills-v${VERSION}.zip" \
    "${SKILL_FILES[@]}" \
    --title "${TAG} — PO Skills Bundle (WoW 2026)" \
    --notes-file "${REPO_DIR}/RELEASE_NOTES.md"

echo ""
echo "═══════════════════════════════════════════════"
echo "  ✅ Release ${TAG} published!"
echo "  🔗 https://github.com/AdrianAmZa/lansweeper-po-skills/releases/tag/${TAG}"
echo "═══════════════════════════════════════════════"
