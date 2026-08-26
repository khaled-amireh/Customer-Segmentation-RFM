import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.cluster.hierarchy as sch

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score, davies_bouldin_score

# 1. Load Dataset
df = pd.read_csv('online_retail_II.csv')

# 2. Data Cleaning & Feature Engineering (RFM Matrix)
df_clean = df.dropna(subset=['Customer ID']).query('Quantity > 0').copy()
df_clean['TotalPrice'] = df_clean['Quantity'] * df_clean['Price']
df_clean['InvoiceDate'] = pd.to_datetime(df_clean['InvoiceDate'])

snapshot_date = df_clean['InvoiceDate'].max() + pd.Timedelta(days=1)

rfm = df_clean.groupby('Customer ID').agg(
    Recency=('InvoiceDate', lambda x: (snapshot_date - x.max()).days),
    Frequency=('Invoice', 'nunique'),
    Monetary=('TotalPrice', 'sum')
)

# 3. Log Transformation & Feature Scaling
rfm_log = np.log1p(rfm)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(rfm_log)
X_scaled_df = pd.DataFrame(X_scaled, index=rfm.index, columns=rfm.columns)

# 4. Save Plot 1: Hierarchical Clustering Dendrogram
plt.figure(figsize=(12, 6))
dendrogram = sch.dendrogram(sch.linkage(X_scaled, method='ward'))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distances')
plt.tight_layout()
plt.savefig('images/dendrogram.png', dpi=300)
plt.close()

# 5. Save Plot 2: K-Means Elbow Method
wcss = []
for k in range(1, 11):
    kmeans_eval = KMeans(n_clusters=k, init='k-means++', random_state=42)
    kmeans_eval.fit(X_scaled)
    wcss.append(kmeans_eval.inertia_)

plt.figure(figsize=(8, 4))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.title('Elbow Method (K-Means)')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS')
plt.tight_layout()
plt.savefig('images/elbow_method.png', dpi=300)
plt.close()

# 6. Model Training (K-Means & Agglomerative Hierarchical)
kmeans = KMeans(n_clusters=4, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X_scaled)

hierarchical = AgglomerativeClustering(n_clusters=4, metric='euclidean', linkage='ward')
y_hierarchical = hierarchical.fit_predict(X_scaled)

rfm['Cluster_KMeans'] = y_kmeans
rfm['Cluster_Hierarchical'] = y_hierarchical

# 7. Model Evaluation Metrics
sil_kmeans = silhouette_score(X_scaled, y_kmeans)
sil_hierarchical = silhouette_score(X_scaled, y_hierarchical)
db_kmeans = davies_bouldin_score(X_scaled, y_kmeans)
db_hierarchical = davies_bouldin_score(X_scaled, y_hierarchical)

print(f"K-Means -> Silhouette Score: {sil_kmeans:.4f} | Davies-Bouldin Index: {db_kmeans:.4f}")
print(f"Hierarchical -> Silhouette Score: {sil_hierarchical:.4f} | Davies-Bouldin Index: {db_hierarchical:.4f}")

# 8. Save Plot 3: Side-by-Side Cluster Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

sns.scatterplot(data=rfm, x='Recency', y='Monetary', hue='Cluster_KMeans', palette='Set1', ax=ax1)
ax1.set_yscale('log')
ax1.set_title('K-Means Clustering')

sns.scatterplot(data=rfm, x='Recency', y='Monetary', hue='Cluster_Hierarchical', palette='Set1', ax=ax2)
ax2.set_yscale('log')
ax2.set_title('Hierarchical Clustering')

plt.tight_layout()
plt.savefig('images/cluster_comparison.png', dpi=300)
plt.close()
