import pandas as pd

# EXTRACT
df = pd.read_csv("sample_logs.csv")

# TRANSFORM
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["status"] = df["status"].str.lower()

# simple cleaning
df = df.dropna()

# LOAD (simulated output)
df.to_csv("clean_logs.csv", index=False)

print("ETL pipeline completed")
