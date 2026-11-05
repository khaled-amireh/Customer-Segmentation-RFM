# Inspecting and reproducing the project

## Inspect saved evidence first

The root [notebook](../customer_segmentation_rfm_clustering.ipynb) contains saved RFM previews, three figures, and the four printed evaluation values. Viewing it does not require executing cells. The [script](../customer_segmentation_rfm_clustering.py) implements the same feature/model stages but writes figures to `images/`.

Historical exact reproduction is currently blocked by the missing `online_retail_II.csv`, its hash/conversion history, and original package versions. Python 3.11.9 appears in notebook metadata; no broader tested version range is established. The instructions below prepare a compatible new environment, not a reconstructed lockfile or a promise of identical scores.

## Use a disposable checkout for execution

The script overwrites `images/dendrogram.png`, `images/elbow_method.png`, and `images/cluster_comparison.png`. Executing and saving the notebook changes its stored outputs/metadata. Perform either operation in a separate disposable clone, keeping the preserved checkout intact.

```bash
git clone https://github.com/khaled-amireh/Customer-Segmentation-RFM.git Customer-Segmentation-RFM-experiment
cd Customer-Segmentation-RFM-experiment
python --version
python -m venv .venv
```

Use a Python 3.11 interpreter to align with the saved metadata. Supply an independently obtained CSV at this checkout's root using the exact filename `online_retail_II.csv`. Verify the five headers and provenance requirements in [DATASET.md](DATASET.md#contract-enforced-by-the-existing-code) before running.

## Install imported libraries and the notebook interface

No `requirements.txt` or dependency lockfile is tracked. These package names correspond to the source imports; `notebook` supplies the interactive interface. The lower scikit-learn bound reflects the `metric` API introduced in 1.2, not a known historical environment. Other dependencies remain unpinned, so record the environment you actually resolve.

Windows PowerShell, without requiring shell activation:

```powershell
.\.venv\Scripts\python.exe -m pip install numpy pandas matplotlib seaborn scipy "scikit-learn>=1.2" notebook
.\.venv\Scripts\python.exe -m pip freeze
.\.venv\Scripts\python.exe -m notebook customer_segmentation_rfm_clustering.ipynb
```

macOS/Linux:

```bash
.venv/bin/python -m pip install numpy pandas matplotlib seaborn scipy "scikit-learn>=1.2" notebook
.venv/bin/python -m pip freeze
.venv/bin/python -m notebook customer_segmentation_rfm_clustering.ipynb
```

Start the notebook from the repository root and execute in order in the disposable checkout. Re-running individual cells out of order can reuse mutated variables: after training, `rfm` includes label columns, so blindly rerunning the scaling cell would include those columns. Restart the kernel and run from the top for a new experiment.

For the standalone path, from the same root and only in the disposable checkout:

```powershell
.\.venv\Scripts\python.exe customer_segmentation_rfm_clustering.py
```

```bash
.venv/bin/python customer_segmentation_rfm_clustering.py
```

## Compare and report responsibly

Record Python/package versions, input SHA-256, row/customer counts, retained-date range, exact snapshot, K and effective K-Means `n_init`. The script prints silhouette and Davies-Bouldin for each estimator. Compare to [saved evidence](EVALUATION.md) but investigate discrepancies rather than overwriting historical results or implying equivalence.

Common failures include a wrong working directory or filename, unexpected CSV headers, malformed dates, invalid monetary/log values, an old scikit-learn API, and insufficient memory for full customer linkage. See [CODE_AUDIT.md](CODE_AUDIT.md). None was experimentally triggered during documentation work. A successful dependency resolution does not establish successful model execution or identical outputs.
