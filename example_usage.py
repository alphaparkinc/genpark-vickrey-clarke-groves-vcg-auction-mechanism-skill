"""
Demonstration of Vickrey-Clarke-Groves (VCG) Auction Mechanism Skill
"""

from client import VCGAuction

def main():
    print("=== Vickrey-Clarke-Groves (VCG) Truthful Mechanism Demonstration ===")
    auction = VCGAuction(items=["gpu_cluster_compute_slot"])

    # Bids submitted by autonomous trading agents
    bids = {
        "Agent_Alpha": 150.0,
        "Agent_Beta": 115.0,
        "Agent_Gamma": 90.0,
        "Agent_Delta": 45.0
    }

    print("Submitted Agent Bids:")
    for a, b in bids.items():
        print(f"  {a}: ${b:.2f}")

    print("\nExecuting Single-Item VCG Mechanism...")
    res = auction.run_single_item_auction(bids)
    print(f"  Winner:          {res['winner']}")
    print(f"  Winning Bid:     ${res['winning_bid']:.2f}")
    print(f"  VCG Payment:     ${res['payment']:.2f} (Second-Price Clarke Pivot)")
    print(f"  Winner Surplus:  ${res['agent_utility']:.2f}")

    assert res["winner"] == "Agent_Alpha"
    assert res["payment"] == 115.0
    assert res["agent_utility"] == 35.0

    print("\nExecuting Multi-Unit VCG Mechanism (2 Available Units)...")
    multi_res = auction.run_multi_unit_auction(bids, units_available=2)
    print(f"  Allocated: {multi_res['units_allocated']}/{multi_res['units_available']} units")
    assert len(multi_res["allocations"]) == 2
    assert "Agent_Alpha" in multi_res["allocations"]
    assert "Agent_Beta" in multi_res["allocations"]
    # Clearing price is the 3rd bid ($90.0)
    assert multi_res["allocations"]["Agent_Alpha"]["payment"] == 90.0
    assert multi_res["allocations"]["Agent_Beta"]["payment"] == 90.0

    print("\nVCG Auction Mechanism Verification PASS!")

if __name__ == "__main__":
    main()
