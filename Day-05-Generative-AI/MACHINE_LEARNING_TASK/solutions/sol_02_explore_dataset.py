# ==============================================================
# Solution 2: Explore the dataset using head(), shape, isnull()
# ==============================================================

import pandas as pd

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

# First 5 rows
print("=== head() ===")
print(df.head())

# Shape of the dataset (rows, columns)
print(f"\n=== shape ===")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# Check for missing values
print(f"\n=== isnull().sum() ===")
print(df.isnull().sum())

# Data types and info
print(f"\n=== dtypes ===")
print(df.dtypes)
