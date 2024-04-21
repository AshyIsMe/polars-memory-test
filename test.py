import numpy as np
import os.path
import polars as pl
import sys

print(f"{sys.version = }")
print(f"{pl.__version__ = }")

if not os.path.exists("df.parquet"):
    df = pl.DataFrame({"a": np.arange(1e8), "b": np.arange(1e8), "c": np.arange(1e8)})
    print(f"{df.estimated_size()/1e9 = } GB")
    df.write_parquet("df.parquet")
    del df

print(pl.scan_parquet("df.parquet", low_memory=True, parallel="none").max().collect())
