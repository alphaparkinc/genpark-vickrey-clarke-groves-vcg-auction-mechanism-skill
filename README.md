# Vickrey-Clarke-Groves (VCG) Auction Skill

Truthful, dominant-strategy incentive-compatible (DSIC) mechanism for allocating arbitrary discrete resource bundles.

```mermaid
flowchart TD
    Bids["Agent Bundle Valuations v_i(S)"] --> Alloc["Max Social Welfare Allocation x*"]
    Alloc --> Counterfactual["Counterfactual Allocation without Agent i"]
    Counterfactual --> Harm["Externality Imposed on Others by Winner i"]
    Harm --> Payment["Clarke Pivot Payment p_i"]
```

## Features
- **100% Python Standard Library**: Exhaustive combinatorial search engine.
- **Truthful Mechanism**: Truth-telling is a weakly dominant strategy for all bidders.
- **Clarke Pivot Rule**: Guarantees individual rationality and non-negative payments.
