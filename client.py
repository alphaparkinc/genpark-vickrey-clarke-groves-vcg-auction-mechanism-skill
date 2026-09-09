"""
Vickrey-Clarke-Groves (VCG) Auction Mechanism Skill Client
Pure Python Standard Library implementation of VCG truthful mechanism design.
Calculates socially optimal resource allocation and Clarke pivot rule payments,
guaranteeing that truthful valuation bidding is a weakly dominant strategy (DSIC).
"""

from typing import Dict, List, Tuple, Any, Optional


class VCGAuction:
    def __init__(self, items: List[str]):
        self.items = list(items)

    def run_single_item_auction(self, bids: Dict[str, float]) -> Dict[str, Any]:
        """Execute single-item second-price VCG auction."""
        sorted_bids = sorted(bids.items(), key=lambda x: x[1], reverse=True)
        if not sorted_bids:
            return {"winner": None, "winning_bid": 0.0, "payment": 0.0, "social_welfare": 0.0}

        winner, winning_bid = sorted_bids[0]
        second_price = sorted_bids[1][1] if len(sorted_bids) > 1 else 0.0

        return {
            "winner": winner,
            "winning_bid": winning_bid,
            "payment": second_price,  # Clarke pivot payment (opportunity cost imposed on others)
            "social_welfare": winning_bid,
            "agent_utility": winning_bid - second_price,
            "truthful_dominant_strategy": True
        }

    def run_multi_unit_auction(self, bids: Dict[str, float], units_available: int) -> Dict[str, Any]:
        """Execute multi-unit VCG auction where each bidder demands 1 unit."""
        sorted_bids = sorted(bids.items(), key=lambda x: x[1], reverse=True)
        k = min(units_available, len(sorted_bids))
        winners = sorted_bids[:k]
        clearing_price = sorted_bids[k][1] if len(sorted_bids) > k else 0.0

        allocations = {}
        for bidder, b in winners:
            allocations[bidder] = {
                "units_won": 1,
                "bid": b,
                "payment": clearing_price,
                "surplus": b - clearing_price
            }

        return {
            "units_available": units_available,
            "units_allocated": k,
            "allocations": allocations,
            "total_revenue": clearing_price * k,
            "total_social_welfare": sum(b for _, b in winners)
        }
