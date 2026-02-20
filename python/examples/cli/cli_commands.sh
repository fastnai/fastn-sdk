#!/usr/bin/env bash
# ============================================================================
# Fastn CLI — Complete Command Reference (runnable examples)
# ============================================================================
#
# This script demonstrates every fastn CLI command with examples.
# Commands that modify state are commented out — uncomment to run.
#
# Prerequisites:
#   pip install fastn
#   fastn init          # or: fastn login
#   fastn sync
# ============================================================================

set -euo pipefail

echo "=== fastn version ==="
fastn version
# Output:
#   Fastn SDK v0.2.0
#   Registry version: 1.0.0
#   Last synced: 2026-02-19T00:00:00+00:00

echo ""
echo "=== fastn --version ==="
fastn --version
# Output: fastn, version 0.2.0

echo ""
echo "=== fastn --help ==="
fastn --help
# Shows all available commands

# ============================================================================
# AUTHENTICATION
# ============================================================================

echo ""
echo "=== fastn whoami ==="
fastn whoami
# Output:
#   Logged in as: Your Name
#   Email: you@example.com
#   User ID: user_abc123

# fastn login
# → Opens browser for OAuth device login
# → Prompts to select a workspace
# → Saves tokens to .fastn/config.json

# fastn logout
# → Clears auth tokens from .fastn/config.json

# fastn init
# → Interactive setup wizard
# → Option 1: Browser login (recommended)
# → Option 2: Manual API key entry
# → Saves config + adds to .gitignore

# ============================================================================
# REGISTRY MANAGEMENT
# ============================================================================

echo ""
echo "=== fastn sync ==="
# fastn sync
# Output:
#   Syncing tool registry...
#   ✓ Registry synced: 45 tools available.
#   ✓ Refreshed stubs for 2 installed tool(s).

echo ""
echo "=== fastn list ==="
fastn list
# Output:
#   Available tools (45):
#
#   My Workspace (3):
#     ✅ flows
#       test
#
#   My Organization (5):
#       slack
#       github
#
#   Marketplace (37):
#       ...

echo ""
echo "=== fastn list --installed ==="
fastn list --installed
# Output:
#   Installed tools (2):
#   ✅ slack
#   ✅ github

echo ""
echo "=== fastn list slack ==="
fastn list slack
# Output:
#   Slack (25 tools):
#
#     send_message              Send a message to a channel
#     list_channels             List all channels
#     ...

echo ""
echo "=== fastn list slack -v ==="
fastn list slack -v
# Output (verbose — shows schemas):
#   send_message
#     Usage: fastn.slack.send_message()
#     Send a message to a channel
#     Input:
#       channel: string (required) — Channel name
#       text: string (required) — Message text
#     Output:
#       ok: boolean

# echo ""
# echo "=== fastn list --active ==="
# fastn list --active
# Output:
#   Active tools (12 actions across 4 connectors):
#
#   ✅ Slack (5 actions)
#   ✅ GitHub (4 actions)
#     Notion (0 tools — not connected)

# ============================================================================
# ADD / REMOVE STUBS
# ============================================================================

# echo ""
# echo "=== fastn add ==="
# fastn add slack
# Output:
#   Adding slack...
#     Fetching tools for slack...
#     ✓ slack added (25 tools).
#   ✓ Type stubs generated.

# fastn add slack github jira    # Add multiple at once

# echo ""
# echo "=== fastn remove ==="
# fastn remove slack
# Output: ✓ Removed slack.

# ============================================================================
# TOOL EXECUTION (fastn run)
# ============================================================================

echo ""
echo "=== fastn run slack ==="
fastn run slack
# Output:
#   Slack — available actions:
#
#     send_message              Send a message to a channel
#     list_channels             List all channels
#     ...
#
#   Run: fastn run slack <action> [--key value ...]

# echo ""
# echo "=== fastn run (inline params) ==="
# fastn run slack send_message --channel general --text "Hello from CLI!"
# Output:
#   Running slack.send_message...
#   {
#     "ok": true,
#     "ts": "1234567890.001234"
#   }

# echo ""
# echo "=== fastn run (interactive) ==="
# fastn run slack send_message
# → Prompts for each parameter:
#   channel (Channel name) [string]: general
#   text (Message text) [string]: Hello!

# echo ""
# echo "=== fastn run (with tenant) ==="
# fastn run slack send_message --tenant acme --channel general --text "Hi"
# fastn run slack send_message acme-tenant-id --channel general --text "Hi"

# echo ""
# echo "=== fastn run (with connection) ==="
# fastn run slack send_message --connection-id conn_123 --channel general --text "Hi"

# echo ""
# echo "=== fastn run (JSON params) ==="
# fastn run slack send_message --channel general --text "Hello" --blocks '[{"type":"section"}]'

# ============================================================================
# SCHEMA INSPECTION
# ============================================================================

echo ""
echo "=== fastn schema ==="
fastn schema slack send_message
# Output (JSON):
#   {
#     "name": "send_message",
#     "description": "Send a message to a channel",
#     "actionId": "act_slack_send_message",
#     "inputSchema": { ... },
#     "outputSchema": { ... }
#   }

echo ""
echo "=== fastn schema (all tools) ==="
fastn schema slack
# Output: JSON array of all tool schemas

# ============================================================================
# AI AGENT (fastn agent)
# ============================================================================

# echo ""
# echo "=== fastn agent ==="
# fastn agent "Send hello to #general on Slack"
# Output:
#   ╭──────────────────────────────────────────────────
#   │  Send hello to #general on Slack
#   ╰──────────────────────────────────────────────────
#
#   Discovering tools...
#   ✓ 3 tools: slack.send_message, slack.list_channels, slack.get_channel_info
#   ✓ LLM: openai (gpt-4o)
#
#   LLM → 1 tool: slack.send_message
#
#     ▸ slack.send_message({channel: general, text: hello})
#       ✓ {"ok": true}
#
#   [summary table]

# echo ""
# echo "=== fastn agent (scoped to connector) ==="
# fastn agent --connector slack "List all channels"

# echo ""
# echo "=== fastn agent (skip confirmations) ==="
# fastn agent -y "Send hello to #general on Slack"

# echo ""
# echo "=== fastn agent (with eval) ==="
# fastn agent --eval "Send hello to #general on Slack"
# Output ends with: ✅ PASS or ❌ FAIL

# echo ""
# echo "=== fastn agent (with tenant) ==="
# fastn agent --tenant acme "Send hello to #general"

# echo ""
# echo "=== fastn agent (options) ==="
# fastn agent --max-turns 5 --max-tools 10 --max-errors 3 "Complex multi-step task"

# ============================================================================
# VERBOSE MODE
# ============================================================================

# echo ""
# echo "=== verbose mode ==="
# fastn -v run slack send_message --channel general --text "Hi"
# Output includes:
#   [API] POST https://live.fastn.ai/api/ucl/executeTool
#   [API] Headers: { ... }
#   [API] Payload: { ... }
#   [API] Response 200: { ... }

echo ""
echo "Done! See fastn --help for more."
