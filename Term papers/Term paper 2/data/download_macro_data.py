"""
Run this script ONCE to download all macro/finance data.
It saves all files to the data/ folder.

Usage:
    python download_macro_data.py
"""

import os
import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

print("=" * 50)
print("Downloading macro/finance data...")
print("=" * 50)

# ── Yahoo Finance ──────────────────────────────────────
START = "2012-01-01"
END = "2024-12-31"

# WTI Crude Oil Futures
print("\n[1/9] WTI Crude Oil (CL=F)...")
oil = yf.download("CL=F", start=START, end=END, auto_adjust=True, progress=False)
oil = oil[["Close"]].rename(columns={"Close": "WTI_oil"})
oil.index.name = "date"
oil.to_csv("data/yahoo_WTI_oil.csv")
print(f"      Saved {len(oil)} rows → data/yahoo_WTI_oil.csv")

# S&P 500
print("\n[2/9] S&P 500 (^GSPC)...")
sp500 = yf.download("^GSPC", start=START, end=END, auto_adjust=True, progress=False)
sp500 = sp500[["Close"]].rename(columns={"Close": "SP500"})
sp500.index.name = "date"
sp500.to_csv("data/yahoo_SP500.csv")
print(f"      Saved {len(sp500)} rows → data/yahoo_SP500.csv")

# ── FRED ───────────────────────────────────────────────
FRED_SERIES = {
    "CPIAUCSL":    "fred_CPIAUCSL.csv",
    "USSTHPI":     "fred_USSTHPI.csv",
    "FEDFUNDS":    "fred_FEDFUNDS.csv",
    "UNRATE":      "fred_UNRATE.csv",
    "GDPC1":       "fred_GDPC1.csv",
    "DTWEXBGS":    "fred_DTWEXBGS.csv",
    "MORTGAGE30US": "fred_MORTGAGE30US.csv",
}

for i, (series_id, filename) in enumerate(FRED_SERIES.items(), start=3):
    print(f"\n[{i}/9] {series_id}...")
    df = pdr.DataReader(series_id, "fred", start=START, end=END)
    df.index.name = "date"
    df.to_csv(f"data/{filename}")
    print(f"      Saved {len(df)} rows → data/{filename}")

print("\n" + "=" * 50)
print("✅ All done! Files saved in data/ folder.")
print("=" * 50)
