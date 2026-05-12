#!/bin/bash
# Bootstrap mykb on a new machine.
# Run once after cloning: bash setup.sh

set -e

echo "=== mykb setup ==="

# Python deps
echo "[1/3] Installing Python packages..."
pip install yfinance pandas numpy --quiet
echo "      yfinance, pandas, numpy installed"

# Node / npx check
echo "[2/3] Checking Node.js..."
if ! command -v npx &>/dev/null; then
  echo "      ERROR: npx not found. Install Node.js first: https://nodejs.org"
  exit 1
fi
echo "      npx found: $(npx --version)"

# Claude Code MCP — puppeteer is already in .mcp.json (project-scoped, auto-loaded)
# financial-datasets is HTTP-based, no install needed
echo "[3/3] MCP servers..."
echo "      puppeteer: loaded from .mcp.json automatically (npx, no install needed)"
echo "      financial-datasets: HTTP-based, no install needed"
echo "      Google MCPs (Gmail/Calendar/Drive): authenticate via /mcp in Claude Code"

echo ""
echo "=== Done. Start Claude Code with: claude ==="
echo ""
echo "Notes:"
echo "  - Memory lives in ~/.claude/projects/.../memory/ (not synced — rebuild on new host)"
echo "  - API keys must be set in env vars on each machine"
