# Dataset provenance and input contract

## Upstream source and local uncertainty

[Online Retail II at UCI](https://archive.ics.uci.edu/dataset/502/online+retail+ii) describes 1,067,371 records from a UK online retailer, covering 1 December 2009 to 9 December 2011. The distributed file is an Excel workbook; the project expects a CSV. These are invoice-line records, not one million unique receipts or customers.

The original README references the [Kaggle mirror](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci). Neither the CSV nor an input checksum is committed. The exact export, sheet selection, concatenation, row count, and local date range are **unverified**. The upstream count must not be presented as a measured input count for this run.

UCI credits Daqing Chen, lists DOI [10.24432/C5CG6D](https://doi.org/10.24432/C5CG6D), and applies [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). This dataset license is separate from the repository's [MIT license](../LICENSE). Upstream field descriptions identify sterling as the price unit and an invoice beginning with `c` as a cancellation.

## Contract enforced by the existing code

Source: [script lines 12-25](../customer_segmentation_rfm_clustering.py#L12), notebook cells 4 and 6. The filename is case-sensitive on case-sensitive systems: `online_retail_II.csv`, located in the **current working directory**. There is no download or schema-normalization step.

| CSV header, exact spelling | How it is used | Required interpretation |
|---|---|---|
| `Customer ID` | Drop missing values; grouping key | Stable customer identifier |
| `Invoice` | `nunique` within each customer | Invoice identifier, including any cancellation prefix |
| `InvoiceDate` | `pd.to_datetime`; maximum timestamp | Consistently parseable purchase timestamp |
| `Quantity` | Positive filter; line value calculation | Numeric units |
| `Price` | Line value calculation | Numeric unit price in a consistent currency |

Other source columns are not used by the implementation. Headers such as `CustomerID`, `InvoiceNo`, and `UnitPrice` do not satisfy this code's exact contract. A renamed workbook is not a CSV.

## Preparing an input for a future experiment

1. Obtain the intended source export independently, retaining its attribution and license.
2. Record its download URL, retrieval date, SHA-256, row count, date range, and whether both source sheets are represented.
3. Verify the five headers above, identifier preservation, numeric types, and unambiguous dates. Record any conversion separately; no conversion was performed during this documentation work.
4. Place the resulting file at the working-directory path expected by the original code in a disposable checkout. Do not overwrite the preserved notebook, outputs, or images in this working tree.

An input assembled today may support a new experiment but cannot be claimed to recreate the saved scores without establishing equivalence to the missing historical CSV.
