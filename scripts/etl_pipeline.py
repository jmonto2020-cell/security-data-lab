import pandas as pd

df = pd.read_csv("sample_logs.csv")

# clean data
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["status"] = df["status"].str.lower()

df = df.dropna()

df.to_csv("clean_logs.csv", index=False)

print("ETL completed")
