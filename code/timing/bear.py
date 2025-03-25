# code/timing/bear.py
import time
start = time.perf_counter()

import polars as pl
transactions = pl.read_csv("../data/larger.csv")
results = transactions.group_by("category").agg(pl.len())
stop = time.perf_counter()

print("Transactions:")
print(transactions.head(3))

print("\n\nGroupings:")
print(results)

print(f"\n\nProcessing took: {stop-start:0.4f} seconds")
