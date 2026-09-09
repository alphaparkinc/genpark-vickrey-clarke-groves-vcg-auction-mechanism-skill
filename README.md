# GenPark Vickrey-Clarke-Groves (VCG) Auction Mechanism Skill

Truthful Vickrey-Clarke-Groves (VCG) auction mechanism with Clarke pivot payments.

Learn more at [GenPark](https://genpark.ai) and the [GenPark MCP Catalog](https://genpark.ai/mcp).

```mermaid
graph TD
    B[Agent Sealed Bids] --> W[Welfare Maximization Winner Determination]
    W --> C[Clarke Pivot Payment Calculation]
    C --> P[Dominant-Strategy Incentive Compatibility DSIC]
    P --> U[Truthful Bidding weakly dominant for all agents]
    style B fill:#e1f5fe
    style W fill:#fff9c4
    style C fill:#ffcdd2
    style P fill:#c8e6c9
    style U fill:#d1c4e9
```

## Features
- Single-item second-price sealed-bid VCG implementation.
- Multi-unit uniform Clarke pivot rule pricing.
- Pure Python standard library.
