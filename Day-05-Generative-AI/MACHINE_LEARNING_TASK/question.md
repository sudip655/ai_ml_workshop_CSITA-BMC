# Machine Learning Question

You are given the following customer dataset. Build a Machine Learning model to predict whether a customer will purchase a product.

## Complete all the following tasks in one solution:

1. Create the DataFrame from the given dataset.
2. Explore the dataset using `head()`, `shape`, and `isnull()`.
3. Visualize Income vs Spending Score, separating customers who purchased and did not purchase.
4. Select `Age`, `Income`, and `SpendingScore` as the features.
5. Select `Purchased` as the target.
6. Split the data into training and testing data.
7. Train a Logistic Regression model.
8. Make predictions on the test data.
9. Calculate the accuracy of the model.
10. Visualize Actual vs Predicted values.
11. Predict whether a new customer will purchase the product.

## Dataset

```python
data = {
    "Age": [
        22, 25, 30, 35, 40,
        45, 50, 23, 28, 33,
        38, 42, 48, 52, 27,
        31, 36, 41, 46, 55
    ],
    "Income": [
        25000, 30000, 35000, 45000, 50000,
        60000, 70000, 28000, 32000, 40000,
        48000, 55000, 65000, 75000, 33000,
        38000, 47000, 58000, 68000, 80000
    ],
    "SpendingScore": [
        75, 80, 65, 60, 55,
        50, 40, 85, 70, 65,
        55, 50, 45, 35, 75,
        70, 60, 50, 45, 30
    ],
    "Purchased": [
        1, 1, 1, 1, 0,
        0, 0, 1, 1, 1,
        0, 0, 0, 0, 1,
        1, 1, 0, 0, 0
    ]
}
```
