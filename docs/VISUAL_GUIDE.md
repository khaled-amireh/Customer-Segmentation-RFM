# Visual analysis guide

All original PNG files remain unchanged. The notebook also contains embedded figures in cells 10, 12, and 18. The standalone script writes the same three paths, while the notebook displays figures; no figure was regenerated during this documentation work.

| Artifact | Original dimensions | Source location | What to read |
|---|---|---|---|
| [Elbow method](../images/elbow_method.png) | 855 x 469 | Notebook cell 12; script lines 44-57 | Inertia falls as K increases from 1 through 10; diminishing returns require interpretation |
| [Ward dendrogram](../images/dendrogram.png) | 1211 x 652 | Notebook cell 10; script lines 34-41 | Successive customer-group merges on standardized log-RFM; heights are linkage distances |
| [Cluster comparison](../images/cluster_comparison.png) | 1455 x 514 | Notebook cell 18; script lines 79-91 | Two separately fitted partitions projected onto original-unit Recency and Monetary |

## Elbow: a diagnostic, not an automatic selector

The vertical axis is within-cluster sum of squares in standardized log-RFM space. It is not money or prediction error. The curve falls steeply at small K and gradually flattens. The code plots the curve but has no knee detector and saves no numeric inertia table. Four is the subsequent configured K, rather than a proven optimum returned by this chart.

## Dendrogram: hierarchy, not persona taxonomy

The leaves represent customer profiles, not invoices. Large merge heights indicate more costly merges under Ward's criterion. The x-axis order is a tree layout and is not a ranking by customer value. Leaf labels are dense at the saved resolution. No explicit cut threshold is drawn; default branch colors do not designate four named customer personas.

The tree is calculated with SciPy, while final hierarchical labels are calculated separately with scikit-learn. Both use the same preprocessed features and Ward linkage. Do not read branch colors as K-Means label IDs.

## Comparison: original axes, transformed fit

Recency is in days and Monetary retains source currency units on a **logarithmic axis**. A log display axis is separate from the earlier three-feature `log1p` preprocessing used to fit the models. Frequency is absent from this view, even though it contributes to fitted distances.

Color IDs 0-3 apply within each subplot only. K-Means 0 and hierarchical 0 are not automatically the same group. Overlap in this two-dimensional view does not by itself prove overlap in the three-dimensional model space. Dot overlap prevents reliable counts, and apparent gaps cannot establish stability. See [segment observations](SEGMENTS.md) for cautious qualitative descriptions.

## Banner and presentation contract

[Customer intelligence banner](../images/customer-intelligence-banner.svg) is the only new image. It uses a 1440 x 460 viewBox, native vector shapes, system font fallbacks, accessible title/description, and the palette `#0B1220`, `#7C3AED`, `#22D3EE`, `#DB2777`, `#F8FAFC`. It has no scripts, animation, remote images, or external fonts. Its customer points and RFM bars are illustrative artwork, not analytical measurements.

The README displays original plots with descriptive alt text and captions. The architecture diagram describes execution paths, while this banner supplies visual identity. Neither is presented as newly computed experimental evidence.
