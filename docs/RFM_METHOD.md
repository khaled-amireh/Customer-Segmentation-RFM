# RFM methodology reference

This reference describes the existing implementation, with no changes to its computation. Source: [script lines 15-31](../customer_segmentation_rfm_clustering.py#L15), notebook cells 6 and 8; see the [cell map](EVIDENCE.md#source-map).

## Definitions

Let `D` be rows with a nonmissing customer identifier and positive Quantity. For customer `c`, let `D_c` contain their retained rows. The common snapshot `S` is the largest retained `InvoiceDate` plus one day.

| Feature | Exact calculation | Units / detail |
|---|---|---|
| Recency | `(S - max(InvoiceDate in D_c)).days` | Integer elapsed days; fractional days discarded |
| Frequency | `nunique(Invoice in D_c)` | Distinct invoice identifiers; missing invoice values excluded by pandas default |
| Monetary | `sum(Quantity * Price in D_c)` | Input currency; sum skips missing values by pandas default |

The snapshot is shared across customers; it is not each customer's last date plus one day. It is relative to the retained dataset, not today's date. The latest observed customer has Recency 1. The exact timestamp is not printed in saved outputs.

Frequency counts **invoices**, not product rows or units. Repeated lines within an invoice do not increase Frequency, but they do contribute again to Monetary. Multiple purchases on the same day can count separately when their invoice IDs differ.

Monetary is spend over the retained positive-quantity rows. Because negative quantities are discarded without matching returns against sales, it is not return-adjusted net revenue. Missing prices can silently disappear in a grouped sum; no validation is present. These are interpretation boundaries, not measured counts of bad records.

## Geometry used for clustering

For each of the three original RFM columns, the code applies `log(1 + value)`, then standardizes that transformed column using the observed customer population. Clustering therefore uses distances between standardized log-RFM vectors, not raw GBP or raw day differences. It does not compute quartile scores, concatenate RFM digits, or use manually weighted features.

The matrix is created **before** cluster columns are attached to `rfm`. Labels are not input features in the saved execution order. `X_scaled_df` is an indexed display copy; both estimators consume the NumPy array `X_scaled`.

## Interpretation rules

- Interpret profiles in original units after clustering; standardized coordinates are not spend or purchase counts.
- Low Recency means a recent observed transaction, but does not identify a first-time buyer. No first-purchase or customer-tenure feature is computed.
- High Frequency and Monetary may partly reflect a longer opportunity to purchase within the observation window. The implementation does not normalize by tenure.
- A customer's aggregate contains no product preference, margin, channel, or campaign-response variable.
- Numeric cluster IDs have no inherent ordering or shared meaning across estimators.

## Evidence boundary

Cell 6 saves five raw customer rows and cell 8 saves five transformed rows. These support verification of the displayed feature definitions and execution sequence. They do not establish the customer population size, cluster distributions, or a reliable persona mapping. Full reproduction requires the [missing input and environment](DATASET.md).
