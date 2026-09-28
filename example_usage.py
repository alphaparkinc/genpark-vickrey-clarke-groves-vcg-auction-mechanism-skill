"""Example demonstrating VCG combinatorial auction execution."""
from client import VCGAuction

def main():
    items = ["Alpha", "Beta"]
    bids = {
        "Agent1": {("Alpha", "Beta"): 150.0},
        "Agent2": {("Alpha",): 80.0},
        "Agent3": {("Beta",): 90.0}
    }
    res = VCGAuction.run_auction(items, bids)
    print("VCG Auction Outcome:")
    print("  Allocation:", res["allocation"])
    print("  Payments:", res["payments"])
    print("  Social Welfare:", res["social_welfare"])

if __name__ == "__main__":
    main()
