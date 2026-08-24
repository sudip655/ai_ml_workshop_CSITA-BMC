# =========================================================
# DAY 2 - PART 1: Introduction to NumPy and Pandas
# -----------------------------------------------------------
# What this file does:
#   - Shows basic NumPy array creation, reshaping, and stats
#     (mean, median, max, standard deviation) — kept as
#     commented-out blocks so you can uncomment and run one
#     example at a time to see what it does.
#   - Shows a very basic Pandas DataFrame example (a table
#     made from a Python dictionary) and tries to add a new
#     row to it.
# =========================================================

import numpy as np
import pandas as pd

# ---------------- NUMPY EXAMPLES ----------------

# Example 1: Create numbers 1 to 99 (step 5), then reshape into a 4x5 grid
print("=== Example 1: arange + reshape ===")
a = np.arange(1,100,5)
print(a)
a = np.reshape(a,(4,5))
print(a)

# Example 2: Create numbers 0-8, reshape into 3x3, check shape & dimensions
print("\n=== Example 2: reshape, shape, ndim ===")
a = np.arange(0,9)
b=a.reshape(3,3)
print(b)
print(b.shape)   # (3,3) -> 3 rows, 3 columns
print(b.ndim)    # 2 -> it's a 2D array

# Example 3: Matrix addition with 2x2 arrays
print("\n=== Example 3: Matrix addition ===")
a = np.arange(0,8,2)
a=a.reshape(2,2)

b = np.arange(8,16,2)
b=b.reshape(2,2)

print(a+b)   # adding two 2x2 matrices element by element

c = np.arange(0,9)
d=c.reshape(3,3)
print(c.shape)

# Example 4: Basic statistics with NumPy - mean, median, max, std deviation
print("\n=== Example 4: Basic statistics ===")
array1=np.array([1,2,3,4,20,10,30])
array2=np.array([4,6,7,9])

print(f"Mean={array1.mean()}")
median = np.median(array1)
max_val=np.max(array2)
sd=np.std(array1)
print(f"standard deviation={sd}")
print(f"median={median}")
print(f"max={max_val}")

# ---------------- PANDAS EXAMPLE ----------------
# Create a small table (DataFrame) from a dictionary
print("\n=== Pandas DataFrame ===")
data = {"name":["ram","hari","sita","geeta"],"Marks":[10,20,30,40],"age":[20,21,22,23]}
df =pd.DataFrame(data)

print(df)

# Adding a new row using pd.concat (correct way)
newRow = pd.DataFrame([{"name":"shyam","Marks":50,"age":30}])
df = pd.concat([df, newRow], ignore_index=True)
print("\nAfter adding new row:")
print(df)