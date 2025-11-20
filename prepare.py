import glob
import pandas as pd
import os

DATA_DIR = "data"

paths = sorted(glob.glob(os.path.join(DATA_DIR, "Indian Kanoon Data Case *.csv")))

dfs = [pd.read_csv(p) for p in paths]
df = pd.concat(dfs, ignore_index=True)

if "case_id" not in df.columns:
    df["case_id"] = df.index.astype(str)

df.to_csv(os.path.join(DATA_DIR, "legal_cases.csv"), index=False)
print("Saved combined dataset with", len(df), "cases.")
