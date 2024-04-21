import numpy as np
import os.path
import polars as pl
import sys

print(f"{sys.version = }")
print(f"{pl.__version__ = }")

if not os.path.exists("df.csv"):
    df = pl.DataFrame({"a": np.arange(1e8), "b": np.arange(1e8), "c": np.arange(1e8)})
    print(f"{df.estimated_size()/1e9 = } GB")
    df.write_csv("df.csv")
    del df

with pl.Config() as cfg:
    cfg.set_streaming_chunk_size(1000)

    print(pl.scan_csv("df.csv", low_memory=True).max().collect(streaming=True))
