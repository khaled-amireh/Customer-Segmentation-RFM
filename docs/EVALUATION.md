# Cluster selection and evaluation evidence

## Saved comparison

The authoritative saved metric output is notebook cell **16**, ID `dd5ef864`, execution count 8. [Script lines 70-76](../customer_segmentation_rfm_clustering.py#L70) implement the same calls. Values are displayed to four decimal places:

| Estimator | Configured groups | Silhouette | Davies-Bouldin |
|---|---:|---:|---:|
| K-Means | 4 | 0.3663 | 0.9355 |
| Ward agglomerative | 4 | 0.3314 | 0.9317 |

These numbers were transcribed from saved output, not recomputed. The full-precision values, input hash, package versions, fitted labels, and customer count are not saved.

## Correctness of the metric calls

Both estimators fit the same `X_scaled` array. Each score receives that array and its estimator's own `fit_predict` labels. Cluster columns are attached to `rfm` after scaling, and the scoring calls do not use the expanded `rfm` table. There is no observed label-feature leakage or mismatch between raw and transformed spaces in the saved execution sequence.

[Silhouette](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html) compares each point's within-cluster distance with its nearest alternative cluster's distance; higher is better. The code uses default Euclidean distance, without `sample_size`, so it evaluates the supplied population. A global mean can conceal poor separation in individual groups.

[Davies-Bouldin](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.davies_bouldin_score.html) compares within-group dispersion with between-center separation; lower is better. K-Means leads silhouette by 0.0349; hierarchical leads Davies-Bouldin by 0.0038, using the rounded values. These are descriptive gaps without uncertainty estimates or a significance test. Neither score measures marketing response or validates persona names.

## What supports four clusters?

The elbow diagnostic fits k=1 through 10 on the transformed customer matrix and plots inertia. The dendrogram uses Ward linkage on that matrix. Both final estimators explicitly set `n_clusters=4`; neither diagnostic feeds a selected value into training.

The elbow has diminishing returns, but there is no saved numeric inertia table or automatic knee calculation. The dendrogram contains several substantial merge gaps, no chosen distance threshold, and no explicit four-cluster cut. Its default branch colors do not select the configured K. Both Ward and K-Means favor compact groups through variance-related objectives, so visual agreement would not be independent validation.

Four clusters are therefore a documented implementation choice. The evidence does not establish that four is uniquely optimal, stable, or commercially actionable.

## Future experiments needed to strengthen the claim

| Question | Minimum useful evidence | Current status |
|---|---|---|
| Which K is useful? | Candidate-K metrics, cluster sizes, and readable raw-unit profiles | Not saved |
| Is K-Means initialization reliable? | Explicit `n_init`, seed sweep, score and assignment variability | Only seed 42 specified |
| Does the segmentation persist? | Resampling or temporal comparisons with matched cluster identities | Not performed in available code |
| Are groups usable? | Customer counts, RFM quantiles, and commercial constraints | No full profiles saved |
| Do treatments help? | Controlled campaign outcomes and costs | No campaign evidence |

No experiments above were run as part of documentation work. They require a separately authorized analytical change and a recoverable input/environment. See the [read-only audit](CODE_AUDIT.md) for prioritized recommendations.
