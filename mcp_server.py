"""MCP stdio server for VCG Auction Mechanism."""
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import VCGAuction

def handle_rpc(request):
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "run_vcg_auction",
                        "description": "Execute VCG combinatorial auction with truthful Clarke pivot pricing",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "items": {"type": "array", "items": {"type": "string"}},
                                "bids": {
                                    "type": "object",
                                    "description": "Mapping from bidder_name to list of {bundle: [item1, item2], value: number}"
                                }
                            },
                            "required": ["items", "bids"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "run_vcg_auction":
            items = args.get("items", [])
            raw_bids = args.get("bids", {})
            bidders_bids = {}
            for bidder, bundle_list in raw_bids.items():
                bidders_bids[bidder] = {}
                for b in bundle_list:
                    bidders_bids[bidder][tuple(sorted(b["bundle"]))] = float(b["value"])
            res = VCGAuction.run_auction(items, bidders_bids)
            return {"jsonrpc": "2.0", "id": req_id, "result": res}
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method {name} not found"}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid request"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_rpc(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
