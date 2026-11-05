# Documentation validation and preservation report

Date: **2026-11-05** (Asia/Amman). Starting HEAD: `a141010012e6d894e73421496fe08fa5ab959e5e`.

## Scope and commit separation

The work consists of **15 focused local documentation/presentation commits**: evidence baseline, static banner, README redesign, dataset contract, RFM reference, cleaning, feature evidence, transformations, K-Means, hierarchical methodology, evaluation, segment interpretation, original-plot presentation, read-only audit, and reproduction/contribution guidance with validation.

Only `README.md`, new Markdown under `docs/`, `CONTRIBUTING.md`, and one new SVG banner are changed or added. No original history was rewritten. No push or deployment was performed. Use `git log --reverse --oneline a141010..HEAD` to inspect every commit.

## Completed checks

| Check | Result / evidence |
|---|---|
| Original HEAD and hashes recorded before edits | [EVIDENCE.md](EVIDENCE.md#original-file-manifest), first documentation commit |
| Protected bytes preserved | All six original files other than the intentionally redesigned README match their baseline working-tree SHA-256; Git reports no protected-file diff |
| Original data/dependencies | Neither dataset nor dependency manifest exists in the baseline; none was added or altered |
| Metric transcription | Four rounded scores match notebook cell 16; no model rerun |
| Source locations | Script line anchors and notebook cell IDs cross-checked against unchanged originals |
| Local links and anchors | All 93 relative file/anchor references checked, including Markdown headings and Python `#L` locations |
| External links | All 18 unique HTTPS destinations returned HTTP 200, following redirects; includes author portfolio, Kaggle, UCI, DOI, official APIs, clone URL, and badges |
| Markdown | Fences balanced; all 22 Markdown tables have consistent column counts; table/header separation reviewed |
| Mermaid | README architecture rendered successfully using Mermaid 11 in headless Chrome; no syntax error |
| SVG | XML parsed; static self-contained vector with accessible title/description; no scripts, remote references, animation, or external fonts |
| Visual presentation | Banner and README rendered locally and visually inspected; original plots reviewed separately |
| Images and structure | All referenced images exist; new banner tracked; documented tree matches final file inventory |
| Installation | Import/package names and root paths match source; Windows Python 3.11 dependency resolution completed with `pip install --dry-run --ignore-installed --no-cache-dir`; nothing installed |
| Whitespace and change scope | `git diff --check a141010` and staged-diff checks pass; no protected-file diff |
| Local commits and working tree | 15 independent commits after baseline; final working tree clean |

Temporary render previews and downloaded verification assets were kept outside the repository. No executable script, automated test, CI workflow, new model output, or dependency file was added to the project. Validation used inline read-only inspection commands; dry-run dependency resolution is not an analytical run.

## Remaining uncertainties

- The historical CSV and exact package environment are missing. The dependency dry-run establishes prospective resolution only, not original package identity, runtime success, or score reproducibility.
- Input row/customer counts, exact snapshot, cleaning losses, cancellation coverage, duplicate prevalence, and price anomalies cannot be measured from the saved previews.
- Cluster counts, full RFM profiles, named personas, stability, and marketing outcomes remain unsupported by saved outputs. See [CODE_AUDIT.md](CODE_AUDIT.md).
- Local rendering checks Markdown, Mermaid, and SVG behavior, but does not replace GitHub's production renderer. External service availability can change after this check.
- No full notebook execution, model fitting, data conversion, package installation, or experiment was performed. macOS/Linux command paths were reviewed but not executed on this Windows host.
