"""
MCP Server for Vickrey-Clarke-Groves (VCG) Auction Mechanism Skill
"""

import json
import sys
from client import VCGAuction

def handle_call(name: str, args: dict) -> dict:
    if name == "run_vcg_auction":
        items = args.get("items", ["item1"])
        bids = args.get("bids", {"agent1": 100.0, "agent2": 80.0})
        units = args.get("units", 1)
        auction = VCGAuction(items)
        if units == 1:
            return auction.run_single_item_auction(bids)
        else:
            return auction.run_multi_unit_auction(bids, units)
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_call(req.get("method"), req.get("params", {}))
        sys.stdout.write(json.dumps(res) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
