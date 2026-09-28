"""Vickrey-Clarke-Groves (VCG) Combinatorial Auction Mechanism.
100% Python Standard Library.
"""

class VCGAuction:
    """Computes social welfare-maximizing bundle allocation and Clarke pivot payments."""
    @staticmethod
    def run_auction(items, bidders_bids):
        bidder_ids = list(bidders_bids.keys())
        best_welfare = -1.0
        best_allocation = None
        
        def search_alloc(idx, remaining_items, current_alloc, current_welfare):
            nonlocal best_welfare, best_allocation
            if idx == len(bidder_ids):
                if current_welfare > best_welfare:
                    best_welfare = current_welfare
                    best_allocation = dict(current_alloc)
                return
                
            bidder = bidder_ids[idx]
            bids = bidders_bids[bidder]
            
            search_alloc(idx + 1, remaining_items, current_alloc, current_welfare)
            for bundle, val in bids.items():
                bundle_set = set(bundle)
                if bundle_set.issubset(remaining_items):
                    current_alloc[bidder] = bundle
                    search_alloc(idx + 1, remaining_items - bundle_set, current_alloc, current_welfare + val)
                    del current_alloc[bidder]

        search_alloc(0, set(items), {}, 0.0)
        
        payments = {}
        for bidder in bidder_ids:
            w_others_actual = sum(
                bidders_bids[b].get(best_allocation.get(b, ()), 0.0)
                for b in bidder_ids if b != bidder
            )
            
            best_cf_welfare = 0.0
            def search_cf(idx, remaining_items, cur_welfare):
                nonlocal best_cf_welfare
                if idx == len(bidder_ids):
                    if cur_welfare > best_cf_welfare:
                        best_cf_welfare = cur_welfare
                    return
                b = bidder_ids[idx]
                if b == bidder:
                    search_cf(idx + 1, remaining_items, cur_welfare)
                    return
                bids = bidders_bids[b]
                search_cf(idx + 1, remaining_items, cur_welfare)
                for bundle, val in bids.items():
                    b_set = set(bundle)
                    if b_set.issubset(remaining_items):
                        search_cf(idx + 1, remaining_items - b_set, cur_welfare + val)

            search_cf(0, set(items), 0.0)
            payments[bidder] = round(best_cf_welfare - w_others_actual, 4)
            
        return {
            "allocation": {k: list(v) for k, v in best_allocation.items()},
            "payments": payments,
            "social_welfare": round(best_welfare, 4)
        }
