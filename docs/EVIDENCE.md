# Repository evidence and preservation baseline

Inspection date: 2026-11-05 (Asia/Amman). Starting HEAD: `a141010012e6d894e73421496fe08fa5ab959e5e`.
The working tree was clean before documentation work. All seven tracked files were inspected, including every notebook cell, saved text output, and all three original PNGs. No model or notebook was executed.

## Original file manifest

SHA-256 values were computed from working-tree bytes before any edits. Every file below except `README.md` is protected against modification. The README hash records its original state for historical comparison.

| Original tracked file | Bytes | SHA-256 |
|---|---:|---|
| `LICENSE` | 1091 | `72a967ad8f5674562cd5bcc81b8665f2791382f23a671d5e7ce595954f636d69` |
| `README.md` | 12681 | `139ada479c036c6caad7968cb192a3697323fd0ea333259b2a35366c1d3fd5b4` |
| `customer_segmentation_rfm_clustering.ipynb` | 573811 | `e89a85d52989578649f5ff6d0c0221bb8ef5f02250e6712bb42a464517b4ac28` |
| `customer_segmentation_rfm_clustering.py` | 3369 | `3e804f4bdf2d40c47449494255c628b498e644b6d8e5d0e3858f642d6336ec9d` |
| `images/cluster_comparison.png` | 544399 | `5a2a439ddb3412b6e5eaeb7755503e9c6de51950d52095c6b5c0c12e025fa821` |
| `images/dendrogram.png` | 84732 | `b7f506042f4589346e93662349807e5291e07273bb3f2487a6bff627e910986a` |
| `images/elbow_method.png` | 58181 | `008705469bc0891dc14999c116cf2e78084a31a61f11bf2304cc858c2b886bac` |

## Source map

Notebook locations use **one-based cell numbers**, counting both Markdown and code cells. IDs provide stable references without rewriting the notebook. Script line numbers refer to the unchanged original file.

| Stage | Notebook cell / ID | Script lines | Saved evidence |
|---|---|---|---|
| Imports | 2 / `ee32aee1` | 1-9 | Libraries imported |
| Input | 4 / `06d2641c` | 12 | Reads `online_retail_II.csv` from working directory |
| Cleaning and RFM | 6 / `30df5163` | 15-25 | First five RFM rows |
| Log and scaling | 8 / `8b019f2e` | 28-31 | First five scaled rows |
| Ward dendrogram | 10 / `1cd93f14` | 34-41 | Embedded PNG and original image file |
| K-Means elbow | 12 / `431f3ca4` | 44-57 | Embedded PNG; k=1 through 10 |
| Four-cluster fits | 14 / `1cb94a0c` | 60-67 | Two label columns assigned to RFM |
| Evaluation | 16 / `dd5ef864` | 70-76 | Printed metrics below |
| Comparison plot | 18 / `8c772c63` | 79-91 | Recency versus Monetary, log y-axis |

The notebook displays plots with `plt.show()`; the script writes the three existing PNG paths. Both implement the same RFM preprocessing and model parameters. Notebook metadata records Python **3.11.9**, with no package-version record.

## Claim verification

| Claim | Verdict | Evidence / boundary |
|---|---|---|
| K-Means silhouette 0.3663; Davies-Bouldin 0.9355 | Verified as saved output | Cell 16, execution count 8 |
| Hierarchical silhouette 0.3314; Davies-Bouldin 0.9317 | Verified as saved output | Same output; no fresh computation |
| Four clusters per algorithm | Verified configuration and plotted labels | Cell 14; legends contain IDs 0-3 |
| About one million input records | Upstream scale only | [UCI dataset record](https://archive.ics.uci.edu/dataset/502/online+retail+ii); no local dataset, shape output, or input hash |
| Four business personas and numeric thresholds | Unsupported by saved profiles | No cluster counts, centroids, RFM summaries, or persona mapping saved |
| Stable clusters or campaign uplift | Unverified | No seed sweep, temporal validation, or campaign experiment |

## Inventory boundaries

At the baseline, the repository contained exactly the seven files in the manifest. There was no dataset, `data/`, `notebooks/`, `requirements.txt`, lockfile, model export, or customer-label export. The old README's structure and installation instructions did not match this inventory.

The first five RFM rows are previews, not a population summary. PNGs support qualitative visual inspection, not exact cluster sizes or reconstructed labels. Saved output is historical evidence; without the original input and environment, it cannot establish independent reproducibility.

For final preservation and documentation checks, see [VALIDATION.md](VALIDATION.md), added at the end of the documentation work.
