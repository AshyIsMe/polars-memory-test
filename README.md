# lazy polars larger than memory testing



```
aaron@spitfire:~/codebases/polars-memory-test$ python test.py
sys.version = '3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]'
pl.__version__ = '0.20.21'
df.estimated_size()/1e9 = 2.4 GB
shape: (1, 3)
┌─────────────┬─────────────┬─────────────┐
│ a           ┆ b           ┆ c           │
│ ---         ┆ ---         ┆ ---         │
│ f64         ┆ f64         ┆ f64         │
╞═════════════╪═════════════╪═════════════╡
│ 9.9999999e7 ┆ 9.9999999e7 ┆ 9.9999999e7 │
└─────────────┴─────────────┴─────────────┘

aaron@spitfire:~/codebases/polars-memory-test$ firejail --quiet --rlimit-as=2g python test.py
sys.version = '3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]'
pl.__version__ = '0.20.21'
memory allocation of 2099736 bytes failed

aaron@spitfire:~/codebases/polars-memory-test$ firejail --quiet --rlimit-as=4g python test.py
sys.version = '3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]'
pl.__version__ = '0.20.21'
memory allocation of 2099736 bytes failed

aaron@spitfire:~/codebases/polars-memory-test$ firejail --quiet --rlimit-as=8g python test.py
sys.version = '3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]'
pl.__version__ = '0.20.21'
shape: (1, 3)
┌─────────────┬─────────────┬─────────────┐
│ a           ┆ b           ┆ c           │
│ ---         ┆ ---         ┆ ---         │
│ f64         ┆ f64         ┆ f64         │
╞═════════════╪═════════════╪═════════════╡
│ 9.9999999e7 ┆ 9.9999999e7 ┆ 9.9999999e7 │
└─────────────┴─────────────┴─────────────┘
```


