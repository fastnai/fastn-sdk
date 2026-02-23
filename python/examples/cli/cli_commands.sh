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
#   fastn login
#   fastn connector sync
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
# → Prompts to select a project
# → Saves tokens to .fastn/config.json

# fastn logout
# → Clears auth tokens from .fastn/config.json

# ============================================================================
# CONNECTORS — fastn connector <subcommand>
# ============================================================================

echo ""
echo "=== fastn connector sync ==="
# fastn connector sync
# Output:
#   Syncing connector registry...
#   ✓ Registry synced: 45 connectors available.
#   ✓ Refreshed stubs for 2 installed connector(s).

echo ""
echo "=== fastn connector ls ==="
fastn connector ls
# Output:
#   Available connectors (45):
#
#   My Project (3):
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
echo "=== fastn connector ls --installed ==="
fastn connector ls --installed
# Output:
#   Installed connectors (2):
#   ✅ slack
#   ✅ github

echo ""
echo "=== fastn connector ls slack ==="
fastn connector ls slack
# Output:
#   Slack (25 tools):
#
#     send_message              Send a message to a channel
#     list_channels             List all channels
#     ...

echo ""
echo "=== fastn connector ls slack -v ==="
fastn connector ls slack -v
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
# echo "=== fastn connector ls --active ==="
# fastn connector ls --active
# Output:
#   Active connectors (12 tools across 4 connectors):
#
#   ✅ Slack (5 tools)
#   ✅ GitHub (4 tools)
#     Notion (0 tools — not connected)

# ============================================================================
# ADD / REMOVE STUBS
# ============================================================================

# echo ""
# echo "=== fastn connector add ==="
# fastn connector add slack
# Output:
#   Adding slack...
#     Fetching tools for slack...
#     ✓ slack added (25 tools).
#   ✓ Type stubs generated.

# fastn connector add slack github jira    # Add multiple at once

# echo ""
# echo "=== fastn connector remove ==="
# fastn connector remove slack
# Output: ✓ Removed slack.

# ============================================================================
# TOOL EXECUTION (fastn connector run)
# ============================================================================

echo ""
echo "=== fastn connector run slack ==="
fastn connector run slack
# Output:
#   Slack — available tools:
#
#     send_message              Send a message to a channel
#     list_channels             List all channels
#     ...
#
#   Run: fastn connector run slack <tool> [--key value ...]

# echo ""
# echo "=== fastn connector run (inline params) ==="
# fastn connector run slack send_message --channel general --text "Hello from CLI!"
# Output:
#   Running slack.send_message...
#   {
#     "ok": true,
#     "ts": "1234567890.001234"
#   }

# echo ""
# echo "=== fastn connector run (interactive) ==="
# fastn connector run slack send_message
# → Prompts for each parameter:
#   channel (Channel name) [string]: general
#   text (Message text) [string]: Hello!

# echo ""
# echo "=== fastn connector run (with tenant) ==="
# fastn connector run slack send_message --tenant acme --channel general --text "Hi"
# fastn connector run slack send_message acme-tenant-id --channel general --text "Hi"

# echo ""
# echo "=== fastn connector run (with connection) ==="
# fastn connector run slack send_message --connection-id conn_123 --channel general --text "Hi"

# echo ""
# echo "=== fastn connector run (JSON params) ==="
# fastn connector run slack send_message --channel general --text "Hello" --blocks '[{"type":"section"}]'

# ============================================================================
# SCHEMA INSPECTION
# ============================================================================

echo ""
echo "=== fastn connector schema ==="
fastn connector schema slack send_message
# Output (JSON):
#   {
#     "name": "send_message",
#     "description": "Send a message to a channel",
#     "actionId": "act_slack_send_message",
#     "inputSchema": { ... },
#     "outputSchema": { ... }
#   }

echo ""
echo "=== fastn connector schema (all tools) ==="
fastn connector schema slack
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
# fastn -v connector run slack send_message --channel general --text "Hi"
# Output includes:
#   [API] POST https://live.fastn.ai/api/ucl/executeTool
#   [API] Headers: { ... }
#   [API] Payload: { ... }
#   [API] Response 200: { ... }

echo ""
echo "Done! See fastn --help for more."
