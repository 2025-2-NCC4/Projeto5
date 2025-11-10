import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
DATA_DIR = os.getenv("DATA_DIR", "../frontend/data")

def list_data_files():
    if not os.path.isdir(DATA_DIR):
        return []
    files = []
    for fn in os.listdir(DATA_DIR):
        p = os.path.join(DATA_DIR, fn)
        if os.path.isfile(p) and any(fn.lower().endswith(ext) for ext in [".csv", ".xlsx", ".xls", ".parquet", ".json"]):
            files.append(fn)
    return files

def load_table(filename: str):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.isfile(path):
        raise FileNotFoundError(f"File not found: {path}")
    if filename.lower().endswith(".csv"):
        return pd.read_csv(path)
    if filename.lower().endswith(".json"):
        return pd.read_json(path)
    if filename.lower().endswith((".xlsx", ".xls")):
        return pd.read_excel(path)
    if filename.lower().endswith(".parquet"):
        return pd.read_parquet(path)
    raise ValueError("Unsupported file type")
