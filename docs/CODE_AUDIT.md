# Read-only clustering audit

Audit date: **2026-11-05**. Baseline: `a141010012e6d894e73421496fe08fa5ab959e5e`.

All original tracked files, all 18 notebook cells and saved outputs, and all original PNGs were inspected. No analytical code, parameter, notebook byte, dataset, dependency, or original chart was changed. No model was run. [EVIDENCE.md](EVIDENCE.md) records the inventory, hashes, source map, and saved metrics.

**Status definitions:** Confirmed means directly observed behavior or an absent safeguard; it does not imply a measured data defect. Potential means the effect depends on missing input data. Unverified means the available artifacts cannot establish a claim. Severity reflects possible consequence for validity, interpretation, or reproducibility, not measured incidence.

## Findings by severity

| Severity | Findings | Status breakdown |
|---|---:|---|
| Critical | 0 | No critical defect established |
| High | 3 | 1 Confirmed, 1 Potential, 1 Unverified |
| Medium | 6 | 4 Confirmed, 1 Potential, 1 Unverified |
| Low | 2 | 2 Potential |

The main priorities are recovering the input/environment, validating monetary inputs and return semantics, and replacing unsupported persona claims with measured profiles. Recommendations below are **not implemented**.

## High severity

### H1. Historical results cannot be independently reproduced from tracked files

- **Severity:** High. **Status:** Confirmed.
- **Exact source:** [script line 12](../customer_segmentation_rfm_clustering.py#L12); notebook cell 4 / `06d2641c`; notebook `metadata.language_info.version`; complete baseline inventory in [EVIDENCE.md](EVIDENCE.md#original-file-manifest).
- **Evidence:** `pd.read_csv('online_retail_II.csv')` requires an absent local input. No CSV hash, full data-shape output, dependency manifest, or package-version record exists. Notebook metadata records Python 3.11.9 only.
- **Impact:** Saved scores can be transcribed and their call sites checked, but the exact input population, snapshot timestamp, and full-precision results cannot be independently established. Upstream scale is not proof of the local input count.
- **Minimal recommended correction:** Recover and record the historical CSV checksum, export lineage, row counts, snapshot date, and exact environment. If unavailable, retain the explicit historical-evidence qualification.
- **New experiments required:** No for documenting provenance if historical records exist; yes for an independent reproduction once the input/environment are recovered. A newly assembled input would be a new experiment.

### H2. Named personas, numeric thresholds, and final-persona selection lack saved support

- **Severity:** High. **Status:** Unverified.
- **Exact source:** Original README at baseline, lines 172 and 188-202 (`git show a141010:README.md`); [script lines 66-67](../customer_segmentation_rfm_clustering.py#L66) and [79-91](../customer_segmentation_rfm_clustering.py#L79); notebook cells 14 and 18.
- **Evidence:** The former README provides four named personas, day/order/spend thresholds, and a claim that K-Means supplied final personas. Code attaches numeric labels and draws a two-feature plot. No cluster counts, mean/median RFM table, persona mapping, or downstream selection is saved. The chart does not show Frequency. No tenure or first-purchase feature identifies new customers. Original spend thresholds use dollars although the referenced source describes GBP.
- **Impact:** Readers could treat proposed treatments and illustrative thresholds as empirical segment profiles, or identify new/lost customers without supporting features. A numeric ID is not a business label and is not comparable across estimators.
- **Minimal recommended correction:** Describe only the visible relative tendencies; remove unsupported thresholds and label marketing ideas as hypotheses. Future analytical work should save all-feature summaries, group counts, unit metadata, and an explicit evidence-based mapping. This documentation applies the claim correction without changing models.
- **New experiments required:** Yes for verified profiles, customer-tenure distinctions, or actionable thresholds; controlled campaign experiments are needed for treatment-effect claims.

### H3. Monetary inputs are not validated before log transformation and distance fitting

- **Severity:** High. **Status:** Potential.
- **Exact source:** [script lines 15-16](../customer_segmentation_rfm_clustering.py#L15), [21-30](../customer_segmentation_rfm_clustering.py#L21); notebook cells 6 and 8.
- **Evidence:** Only Quantity is constrained positive. Price is neither checked for missingness, finiteness, nor positivity before multiplication and sum. No aggregate-domain or finite-matrix validation precedes `np.log1p` and scaling. The missing dataset prevents counting any problematic rows.
- **Impact:** Missing values can be skipped in sums; zero or negative prices can understate retained spend. An aggregate at -1 yields negative infinity under `log1p`; below -1 yields an invalid real value. Nonfinite model input can fail fitting. Less severe retained errors can shift distances and labels.
- **Minimal recommended correction:** In a future analytical revision, profile nonfinite/missing/nonpositive prices and aggregate spend; define a business rule for exclusions or exceptional records, then assert finite valid transformed inputs. Do not silently discard legitimate adjustments.
- **New experiments required:** Yes. Quantify affected records and compare customer features, memberships, and metrics under a documented policy.

## Medium severity

### M1. Cancellation coverage is inferred from quantity rather than verified from invoices

- **Severity:** Medium. **Status:** Confirmed.
- **Exact source:** [script line 15](../customer_segmentation_rfm_clustering.py#L15); notebook cell 6 / `30df5163`.
- **Evidence:** The predicate is `Quantity > 0`; no `Invoice` prefix check exists. The [upstream variable description](https://archive.ics.uci.edu/dataset/502/online+retail+ii) identifies `c`-prefixed invoices as cancellations. Ordinary negative-quantity cancellation rows are excluded, but equivalence of both rules is not tested.
- **Impact:** Any cancellation-coded row with positive quantity would survive. Its existence and effect are unknown; this is a confirmed coverage gap, not proof that cancellations actually survived in the historical input.
- **Minimal recommended correction:** Cross-tabulate case-normalized cancellation prefixes against quantity signs. Define and document an explicit cancellation policy after inspecting exceptions.
- **New experiments required:** Yes to establish affected counts; rerun only if a changed policy alters retained data.

### M2. Duplicate invoice-line influence is not assessed

- **Severity:** Medium. **Status:** Potential.
- **Exact source:** [script lines 12-25](../customer_segmentation_rfm_clustering.py#L12); notebook cells 4 and 6.
- **Evidence:** No duplicate count, duplicate-key policy, or deduplication operation appears. The dataset is unavailable, so duplicate incidence is unknown. `Frequency=('Invoice', 'nunique')` avoids inflating invoice count for a repeated line, while summed Monetary would include its repeated value.
- **Impact:** Accidental duplicate lines could inflate Monetary while leaving Frequency unchanged, shifting feature geometry. Repeated product lines may also be legitimate, so blind removal is not justified.
- **Minimal recommended correction:** Measure exact and business-key duplicates, review examples, and adopt a justified policy before changing data.
- **New experiments required:** Yes for incidence assessment and, if duplicates are removed, a sensitivity comparison.

### M3. Retained positive purchases are not return-adjusted net revenue

- **Severity:** Medium. **Status:** Confirmed.
- **Exact source:** [script lines 15-24](../customer_segmentation_rfm_clustering.py#L15); notebook cell 6.
- **Evidence:** Nonpositive quantities are discarded before RFM aggregation. Positive original purchase lines are not matched to later cancellations or returns. Monetary sums retained line values, and invoice Frequency counts retained purchases regardless of a later reversal.
- **Impact:** A refunded or fully returned purchase can still contribute to gross spend and invoice activity. If the business intends net customer value, the aggregate may overstate it. The magnitude is unknown without input data; the code can still be consistent with a deliberately gross-purchase objective.
- **Minimal recommended correction:** Explicitly name the measure retained gross spend. For a net-value objective, reconcile sales and reversals using a documented transaction policy and compare the resulting features.
- **New experiments required:** No for correcting the description; yes for return reconciliation and its effect on clustering.

### M4. K-Means initialization effort depends on the unrecorded library version

- **Severity:** Medium. **Status:** Confirmed.
- **Exact source:** [script line 46](../customer_segmentation_rfm_clustering.py#L46) and [line 60](../customer_segmentation_rfm_clustering.py#L60); notebook cells 12 and 14.
- **Evidence:** Both K-Means constructors set `random_state=42` and `init='k-means++'` but omit `n_init`. [Official versioned documentation](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.KMeans.html) records a default change to `auto` in 1.4; with k-means++ that means one start. Historical package versions are absent.
- **Impact:** The same seed does not guarantee equivalent initialization effort or identical results across environments. Both the elbow and final fit can change. No particular historical default can be inferred from the output alone.
- **Minimal recommended correction:** Recover the original version and restart setting. In a future code revision, specify the intended `n_init` explicitly for both constructors and record versions.
- **New experiments required:** Yes to assess restart and seed sensitivity; environment recovery alone may document historical behavior.

### M5. Four clusters are hard-coded without comparative selection evidence

- **Severity:** Medium. **Status:** Confirmed.
- **Exact source:** [script lines 44-48](../customer_segmentation_rfm_clustering.py#L44), [60-64](../customer_segmentation_rfm_clustering.py#L60); notebook cells 10, 12, and 14; original README baseline line 154.
- **Evidence:** The elbow plots inertia for k=1...10; final models explicitly request four groups. The dendrogram contains no chosen cut threshold. No silhouette-by-K table or alternative-K profile assessment is saved. The old README describes the two diagnostics as independent confirmation, although Ward and K-Means both favor compact variance-based groups on the same matrix.
- **Impact:** Readers may overstate four as a uniquely supported natural structure. Different K values can produce different segment interpretations while still appearing plausible.
- **Minimal recommended correction:** Describe four as the implemented exploratory choice. Later compare multiple K values using metrics, group sizes, profiles, and practical use constraints.
- **New experiments required:** Yes to justify a selected K beyond the existing visual heuristic; no for qualifying the claim.

### M6. Cluster stability and resistance to extremes are not established

- **Severity:** Medium. **Status:** Unverified.
- **Exact source:** [script lines 28-30](../customer_segmentation_rfm_clustering.py#L28), [60-73](../customer_segmentation_rfm_clustering.py#L60); notebook cells 8, 14, and 16.
- **Evidence:** A single K-Means seed and a single hierarchical fit are evaluated on their fitted population. No resampling, temporal comparison, seed sweep, or outlier sensitivity analysis is present. Log transformation reduces magnitude differences but [StandardScaler remains outlier-sensitive](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html).
- **Impact:** Saved internal scores cannot establish membership stability or whether extreme customers drive boundaries. This is missing validation, not evidence of instability. Large visible spend values in a chart are not proof of defective records.
- **Minimal recommended correction:** Avoid robustness/stability claims. For future experiments, compare seeds/restarts, resamples and observation windows, and justified outlier policies; match cluster identities before comparing labels.
- **New experiments required:** Yes for all stability and sensitivity conclusions.

## Low severity

### L1. Timestamp and invoice-identifier quality rules are implicit

- **Severity:** Low. **Status:** Potential.
- **Exact source:** [script lines 17-24](../customer_segmentation_rfm_clustering.py#L17); notebook cell 6.
- **Evidence:** Date conversion has no explicit format or quality report. The snapshot is `max(InvoiceDate) + one day`, and Recency uses `.days`. `nunique` excludes missing invoice IDs by default; only customer-ID missingness is filtered. No counts of missing invoice IDs or date exceptions are saved.
- **Impact:** Ambiguous/malformed dates or missing invoice IDs could affect Recency or Frequency if present. Fractional days are deliberately truncated, which is not a calendar-date calculation. The reference-date expression itself is consistent and is not an off-by-one defect.
- **Minimal recommended correction:** Record the exact snapshot, parse policy, and rejected-date/missing-invoice counts; define whether elapsed days or calendar days are intended.
- **New experiments required:** Yes to inspect the absent data; documentation alone can clarify intended time semantics.

### L2. Full-population diagnostics can become expensive as customer count grows

- **Severity:** Low. **Status:** Potential.
- **Exact source:** [script line 35](../customer_segmentation_rfm_clustering.py#L35), [63-64](../customer_segmentation_rfm_clustering.py#L63), [70-71](../customer_segmentation_rfm_clustering.py#L70); notebook cells 10, 14, and 16.
- **Evidence:** SciPy Ward linkage, a separate agglomerative fit, and unsampled silhouette are all run on customer vectors. [SciPy documents quadratic linkage memory](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html). The exact number of customers and runtime/memory measurements are absent.
- **Impact:** Future larger customer populations may exhaust resources or make diagnostics impractical. This is not a claim that the historical run failed or that clustering operated on one million raw lines.
- **Minimal recommended correction:** Record customer count and resource use; consider clearly labeled diagnostic sampling or scalable alternatives if necessary. Preserve the distinction between sampled and full scores.
- **New experiments required:** Yes for resource measurements or altered diagnostics at a new scale.

## Checks without a demonstrated implementation defect

| Requested check | Observed result |
|---|---|
| RFM aggregation | Correct customer groupby, latest timestamp, distinct invoices, and summed retained line values; unit/return caveats above |
| Recency reference date | A shared latest-retained timestamp plus one day; exact timestamp unavailable |
| Frequency | Invoice `nunique`, not row or item count |
| Transformations | `log1p` applies to R, F, and M before labels exist |
| Scaling consistency | One fitted scaler; both estimators and all metric calls use the same `X_scaled` |
| Silhouette correctness | Each model's labels paired with its fitted matrix; default Euclidean; no observed label leakage |
| Davies-Bouldin correctness | Corresponding labels and same matrix; no observed argument mismatch |
| Ward methodology | Consistent Ward/Euclidean setup; diagnostic SciPy tree and scikit-learn label fit are separate |
| Saved metrics | Cell 16 prints K-Means 0.3663 / 0.9355 and hierarchical 0.3314 / 0.9317 |

Evaluation is in-sample internal assessment, not supervised predictive accuracy. No critical bug, proven unstable partition, measured duplicate count, or quantified cleaning impact can be established from the available evidence. [EVALUATION.md](EVALUATION.md) and [SEGMENTS.md](SEGMENTS.md) distinguish verified outputs from proposed follow-up work.
