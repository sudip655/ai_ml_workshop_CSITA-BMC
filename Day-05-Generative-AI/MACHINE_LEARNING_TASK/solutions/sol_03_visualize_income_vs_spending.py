# ==============================================================
# Solution 3: Visualize Income vs Spending Score
#              (separating Purchased vs Not Purchased)
# ==============================================================

import pandas as pd
import matplotlib.pyplot as plt

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

# Separate customers by purchase status
purchased = df[df["Purchased"] == 1]
not_purchased = df[df["Purchased"] == 0]

plt.figure(figsize=(10, 6))
plt.scatter(
    not_purchased["Income"], not_purchased["SpendingScore"],
    color="red", label="Not Purchased", marker="x", s=100
)
plt.scatter(
    purchased["Income"], purchased["SpendingScore"],
    color="green", label="Purchased", marker="o", s=100
)
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.title("Income vs Spending Score (by Purchase Status)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("income_vs_spending.png", dpi=150)
print("Plot saved as 'income_vs_spending.png'")
plt.show()
