# Customer segments: observations and hypotheses

## What is actually available

Notebook cell 14 fits two four-cluster models and attaches IDs to the raw RFM table. Cell 18 and the [original comparison PNG](../images/cluster_comparison.png) show each model's partition on Recency and Monetary, with a logarithmic Monetary axis. No group-size table, centroids, raw-unit RFM summary, saved labels, or named persona mapping is available.

The table below records qualitative observations from that PNG. It does not reconstruct data from pixel positions. Frequency is absent from this projection, so no claim about loyalty or repeat ordering follows from the image alone.

| Algorithm / ID | Visible tendency in the original two-feature projection | Evidence limit |
|---|---|---|
| K-Means 0, red | Concentrated toward recent purchases and lower-to-middle spend | Recent does not establish new-customer status |
| K-Means 1, blue | Lower spend across a broad recency range | Includes different recency levels; not a single inactivity threshold |
| K-Means 2, green | Higher spend, predominantly toward recent purchases | Frequency and margin unknown |
| K-Means 3, purple | Middle-to-higher spend across a broader recency range | Not a measured loyal-customer profile |
| Hierarchical 0, red | Higher spend, more concentrated toward recent purchases | Does not correspond to K-Means ID 0 |
| Hierarchical 1, blue | Lower-to-middle spend, more toward the recent side | Requires full profiles for naming |
| Hierarchical 2, green | Lower spend, including many less-recent observations | No validated churn label |
| Hierarchical 3, purple | Middle-spend band across a broad recency range | No measured campaign response |

All descriptions are relative visual tendencies with overlap, not numeric boundaries. **Every cluster's exact count, share, and mean/median RFM remain unknown from saved evidence.** Colors and numeric IDs are estimator-specific. Matching partitions requires membership data and an explicit mapping, not matching label numbers.

## Responsible business interpretation

The former README named Champions/VIP, Loyal Regulars, Recent/New Buyers, and At-Risk/Lost, with thresholds such as 30 days, 15 orders, and $10,000. There is no saved analysis deriving those cutoffs, and the source prices are described in GBP. Those thresholds are not retained as findings.

| Possible hypothesis | Evidence needed before adopting it | Proposed experiment |
|---|---|---|
| High-value active customers | Low Recency plus high Frequency and Monetary; margins and service costs | Evaluate a loyalty treatment with a control group |
| Repeat regulars | High invoice Frequency and sensible timing relative to tenure | Compare cross-sell relevance and incremental margin |
| Newly acquired customers | First-purchase date or tenure, in addition to RFM | Assess onboarding effectiveness |
| Lapsing customers | Historical cadence, elapsed time, and a validated inactivity rule | Test reactivation with costs and suppression rules |

These are possible uses, not the four learned cluster names, deployed actions, or measured outcomes. Low-frequency recent purchasing is not proof of acquisition; high Recency is not proof of permanent churn.

## Minimum profile evidence for a future analytical revision

Save counts and proportions per group, mean/median and spread for all three raw-unit RFM features, invoice and spend shares, and cluster-center information with feature-space labels. Examine tails and customers near boundaries before choosing names. Include tenure if distinguishing new from returning customers. Compare alternative K values and seeds before treating a partition as stable.

This documentation adds no analytical output. See [evaluation](EVALUATION.md) for the saved metrics and [RFM methodology](RFM_METHOD.md) for feature semantics.
