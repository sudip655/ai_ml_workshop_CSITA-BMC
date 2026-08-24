# Day 04: Machine Learning

This folder introduces Machine Learning concepts, specifically Supervised Learning (Linear Regression) and Unsupervised Learning (K-Means Clustering).

## 📁 Directory Structure
*   `Regression/`: Supervised learning project predicting exam scores.
    *   `regression-model.py`: Fits a scikit-learn `LinearRegression` model using Study Hours and Attendance to predict a Score.
    *   `dataset.csv`: Dataset containing student columns: `StudyHours`, `Attendance`, and `Score`.
    *   `generate_dataset.py`: The Python helper script used to generate the dataset.
*   `Clustering/`: Unsupervised learning project grouping customers.
    *   `cluster.py`: Groups customer records using scikit-learn `KMeans` based on Annual Income and Spending Score.
    *   `dataset.csv`: Customer dataset containing `CustomerID`, `AnnualIncome`, and `SpendingScore`.

## 🚀 Getting Started

### Supervised Learning (Regression)
1. Run the regression script:
   ```bash
   python Regression/regression-model.py
   ```

### Unsupervised Learning (Clustering)
1. Run the clustering script:
   ```bash
   python Clustering/cluster.py
   ```
