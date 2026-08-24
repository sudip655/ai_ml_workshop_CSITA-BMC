# ==============================================================
# Solution 7 & 8: Train Logistic Regression + Make Predictions
# ==============================================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

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

df = pd.DataFrame(data)

X = df[["Age", "Income", "SpendingScore"]]
y = df["Purchased"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
print("Logistic Regression model trained successfully!")

# Make predictions on test data
y_pred = model.predict(X_test)

print(f"\nActual values:    {list(y_test.values)}")
print(f"Predicted values: {list(y_pred)}")
