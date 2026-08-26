#  Customer Segmentation using K-Means and Hierarchical Clustering

An end-to-end unsupervised machine learning pipeline comparing **K-Means Clustering** and **Agglomerative Hierarchical Clustering** on online retail transactions (~1M records) using **RFM (Recency, Frequency, Monetary)** feature analysis.

---

##  Executive Summary & Problem Overview

Targeted marketing requires understanding unique customer behaviors rather than treating all shoppers identically. Transactional data consists of individual purchases, which cannot be fed directly into clustering algorithms without aggregation. 

This project engineers **Recency, Frequency, and Monetary (RFM)** features at the customer level, normalizes features via Log Transformation and `StandardScaler`, and compares centroid-based (K-Means) versus connectivity-based (Hierarchical) algorithms to build actionable business personas.

---

##  Dataset Information

* **Source:** [Online Retail II Dataset on Kaggle](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci)
* **Scale:** ~1,000,000 raw invoice transactions.
* **Engineered Units:** Unique customer-level RFM profiles:
  * **Recency (R):** Days since last completed transaction.
  * **Frequency (F):** Count of distinct completed purchases.
  * **Monetary (M):** Total monetary revenue generated per customer.

---

##  Data Preprocessing & Feature Engineering

1. **Cleaning:** Dropped rows missing `Customer ID` and removed negative/cancelled quantities (`Quantity > 0`).
2. **Aggregation:** Calculated total spend per line item (`Quantity * Price`) and aggregated metrics grouped by `Customer ID`.
3. **Log Transformation:** Applied `np.log1p()` to handle heavy right-skewness across monetary and frequency distributions.
4. **Feature Scaling:** Applied `StandardScaler` to normalize feature vectors before distance-based evaluation.

---

##  Optimal Cluster Selection ($K=4$)

### 1. Hierarchical Dendrogram Analysis
Using `ward` linkage and Euclidean distances, the tree cut visually confirms 4 distinct natural groupings.

![Hierarchical Dendrogram](images/dendrogram.png)

### 2. K-Means Elbow Method
The Within-Cluster Sum of Squares (WCSS) plot displays a distinct elbow point at $K=4$.

![Elbow Method](images/elbow_method.png)

---

##  Model Evaluation & Comparison

Both models were evaluated on scaled features using quantitative internal cluster validation metrics:

| Clustering Algorithm | Silhouette Score ↑ | Davies-Bouldin Index ↓ | Evaluation |
| :--- | :---: | :---: | :--- |
| **K-Means Clustering** | **0.3663** | **0.9355** | Slightly higher separation and cluster cohesion. |
| **Hierarchical Clustering** | **0.3314** | **0.9317** | Comparable performance with slightly better DB index. |

---

##  Visual Cluster Comparison

Side-by-side scatter plots illustrating customer distribution across Recency vs. Monetary space:

![Cluster Comparison](images/cluster_comparison.png)

---

##  Business Persona Mapping & Strategy

1. **VIP / High Spenders (High Monetary, High Recency):**
   * *Strategy:* Exclusive VIP rewards, early access to new collections, and dedicated account support.
2. **Loyal Regulars (Moderate Monetary, Frequent Purchases):**
   * *Strategy:* Cross-selling recommendations and loyalty points program to maximize Customer Lifetime Value (CLV).
3. **Recent / New Buyers (Low Monetary, High Recency):**
   * *Strategy:* Welcome discount codes, onboarding email sequences, and popular product suggestions.
4. **At-Risk / Lost Customers (Low-to-Moderate Monetary, Low Recency):**
   * *Strategy:* Targeted win-back email campaigns and re-engagement promotional incentives.

---
## Author

**Khaled Amireh**
