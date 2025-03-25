# code/timing/lazy.py
import time
start = time.perf_counter()

import polars as pl
transactions = pl.scan_csv("../data/larger.csv")
q1 = transactions.head()
q2 = (
    transactions
    .group_by("category").agg(pl.len())
)
result1 = q1.collect()
result2 = q2.collect()
stop = time.perf_counter()

print("Transactions:")
print(result1)

print("\n\nGroupings:")
print(result2)

print(f"\n\nProcessing took: {stop-start:0.4f} seconds")
