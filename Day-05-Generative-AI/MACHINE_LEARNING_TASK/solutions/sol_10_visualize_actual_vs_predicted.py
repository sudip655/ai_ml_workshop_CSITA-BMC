# ==============================================================
# Solution 10: Visualize Actual vs Predicted Values
# ==============================================================

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Bar chart: Actual vs Predicted
x_axis = np.arange(len(y_test))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x_axis - width / 2, y_test.values, width, label="Actual", color="#2ecc71")
bars2 = ax.bar(x_axis + width / 2, y_pred, width, label="Predicted", color="#e74c3c")

ax.set_xlabel("Test Sample Index")
ax.set_ylabel("Purchased (0 = No, 1 = Yes)")
ax.set_title("Actual vs Predicted Purchase Status")
ax.set_xticks(x_axis)
ax.set_xticklabels([f"Sample {i+1}" for i in range(len(y_test))])
ax.legend()
ax.set_yticks([0, 1])
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("actual_vs_predicted.png", dpi=150)
print("Plot saved as 'actual_vs_predicted.png'")
plt.show()
