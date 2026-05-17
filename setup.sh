#!/bin/bash
# Bootstrap mykb on a new machine.
# Run once after cloning: bash setup.sh

set -e

echo "=== mykb setup ==="

# Python deps
echo "[1/4] Installing Python packages..."
pip install yfinance pandas numpy --quiet
echo "      yfinance, pandas, numpy installed"

# Node / npx check
echo "[2/4] Checking Node.js..."
if ! command -v npx &>/dev/null; then
  echo "      ERROR: npx not found. Install Node.js first: https://nodejs.org"
  exit 1
fi
echo "      npx found: $(npx --version)"

# MCP servers auto-loaded from .mcp.json
echo "[3/4] MCP servers (auto-load from .mcp.json):"
echo "      playwright         — stdio via npx (project-scoped, auto-runs on Claude Code open)"
echo "      financial-datasets — HTTP MCP (requires /mcp OAuth on first use per machine)"

# Plugin installs (Claude Code marketplace, manual steps)
echo "[4/4] Manual steps inside Claude Code:"
echo ""
echo "  After launching Claude Code (claude), run:"
echo "    /plugin marketplace add kepano/obsidian-skills"
echo "    /plugin install obsidian@obsidian-skills"
echo "    /reload-plugins"
echo ""
echo "  Authenticate financial-datasets (one-time OAuth per machine):"
echo "    /mcp     # then click auth flow for financial-datasets"
echo ""
echo "=== Done. Start Claude Code with: claude ==="
echo ""
echo "Notes:"
echo "  - Auto-memory (~/.claude/projects/.../memory/) is intentionally NOT synced."
echo "    Rebuild from vault context (daily/ + notes/) on new machine."
echo "  - API keys / env vars (if any) must be set per machine."
echo "  - Source of truth: my2ndbrain/daily/ for session history; CLAUDE.md for project conventions."
echo "  - CLAUDE.md and scripts/lib_finance.py currently live at /Users/<you>/prj-2026/"
echo "    (outside my2ndbrain) — they must be recreated or symlinked from elsewhere on new machine."
