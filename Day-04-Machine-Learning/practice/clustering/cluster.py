# =========================================================
# DAY 4 - PROJECT 2: Clustering - Customer Segmentation (KMeans)
# -----------------------------------------------------------
# What this file does (unsupervised learning):
#   - Loads "dataset.csv" (columns: CustomerID, AnnualIncome,
#     SpendingScore) from THIS SAME FOLDER (project-2-clustering).
#   - Groups customers into 3 clusters based on their Annual
#     Income and Spending Score, using KMeans.
#     (Unsupervised = there is no "correct answer" given up
#      front; the algorithm finds the groups/patterns itself.)
#   - Shows a scatter plot: each color = one customer group,
#     red X marks = the center of each group.
# =========================================================

import pandas as pd
from sklearn.cluster import KMeans

import os
dataset_path = "dataset.csv"
if not os.path.exists(dataset_path):
    dataset_path = "Day-04-Machine-Learning/Clustering/dataset.csv"
df = pd.read_csv(dataset_path)

# Features used for grouping customers
x = df[["AnnualIncome", "SpendingScore"]]

# n_clusters=3 -> we're telling KMeans to find exactly 3 groups
# n_init=10 -> run the algorithm 10 times with different starting points
#              and keep the best result (more stable/reliable clusters)
model = KMeans(n_clusters=3, random_state=42, n_init=10)
model.fit(x)

# Add the predicted cluster number (0, 1, or 2) back into the table
df["Cluster"] = model.labels_

print(df.head())
print("cluster centers:")
print(model.cluster_centers_)   # the (income, spending) center point of each group

import matplotlib.pyplot as plt

# Plot each customer as a dot, colored by which cluster it belongs to
plt.scatter(df["AnnualIncome"], df["SpendingScore"], c=df["Cluster"], cmap="viridis")
# Plot the cluster centers as big red X marks
plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], c="red", marker="x", s=200)
plt.title("Customer Segments"); plt.xlabel("Annual Income"); plt.ylabel("Spending Score")
plt.show()   # opens a window showing the chart
