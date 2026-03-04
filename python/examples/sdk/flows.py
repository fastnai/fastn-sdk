"""Flow execution examples — list, run, check status, and inspect flows.

Covers:
  1. List flows           — enumerate flows in the workspace
  2. Run a flow           — trigger with optional input data
  3. Check run status     — poll a run for completion
  4. Discover schema      — inspect the input schema
  5. Filter by status     — list only active flows

Update the credentials below and run:
    python examples/sdk/flows.py
"""

from __future__ import annotations

import json

from fastn import FastnClient

# --- Configuration (update these) ----------------------------------------
API_KEY = "your-api-key"
PROJECT_ID = "your-project-id"
# --------------------------------------------------------------------------


def _header(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


# ===================================================================
# 1. List flows
# ===================================================================

def list_flows() -> None:
    """Enumerate all flows in the workspace."""
    _header("1. LIST FLOWS")

    with FastnClient(api_key=API_KEY, project_id=PROJECT_ID) as fastn:
        flows = fastn.flows.list()
        for f in flows:
            print(f"  {f['name']:<30} status={f['status']}  v{f.get('version', '?')}")

        if not flows:
            print("  (no flows found)")


# ===================================================================
# 2. Run a flow
# ===================================================================

def run_flow() -> None:
    """Trigger a flow with optional input data."""
    _header("2. RUN A FLOW")

    with FastnClient(api_key=API_KEY, project_id=PROJECT_ID) as fastn:
        flows = fastn.flows.list()
        if not flows:
            print("  (no flows found)")
            return

        flow_name = flows[0]["name"]
        print(f"Running: {flow_name}")
        result = fastn.flows.run(flow_name, input_data={"message": "Hello from SDK"})
        print(f"  Result: {json.dumps(result, default=str)[:300]}")


# ===================================================================
# 3. Check run status
# ===================================================================

def check_run_status() -> None:
    """Run a flow and poll its completion status."""
    _header("3. CHECK RUN STATUS")

    with FastnClient(api_key=API_KEY, project_id=PROJECT_ID) as fastn:
        flows = fastn.flows.list()
        if not flows:
            print("  (no flows found)")
            return

        flow_name = flows[0]["name"]
        result = fastn.flows.run(flow_name, input_data={"message": "Hello from SDK"})
        run_id = result.get("run_id") if isinstance(result, dict) else None

        if run_id:
            print(f"Run ID: {run_id}")
            status = fastn.flows.get_run(run_id=run_id)
            print(f"  Status: {status.get('status')}")
            print(f"  Result: {json.dumps(status.get('result', {}), default=str)[:200]}")
        else:
            print("  (no run_id returned)")


# ===================================================================
# 4. Discover schema
# ===================================================================

def discover_schema() -> None:
    """Inspect a flow's input schema."""
    _header("4. DISCOVER SCHEMA")

    with FastnClient(api_key=API_KEY, project_id=PROJECT_ID) as fastn:
        flows = fastn.flows.list()
        if not flows:
            print("  (no flows found)")
            return

        flow_name = flows[0]["name"]
        print(f"Schema for: {flow_name}")
        schema_info = fastn.flows.schema(flow_name)
        print(f"  Fields: {schema_info['fields']}")
        print(f"  Schema: {json.dumps(schema_info['schema'], indent=4)}")


# ===================================================================
# 5. Filter by status
# ===================================================================

def filter_by_status() -> None:
    """List only active flows."""
    _header("5. FILTER BY STATUS")

    with FastnClient(api_key=API_KEY, project_id=PROJECT_ID) as fastn:
        active = fastn.flows.list(status="active")
        for f in active:
            print(f"  {f['name']}")

        if not active:
            print("  (no active flows)")


# ===================================================================
# Main
# ===================================================================

if __name__ == "__main__":
    # Uncomment the examples you want to run:
    list_flows()
    # run_flow()
    # check_run_status()
    # discover_schema()
    # filter_by_status()
