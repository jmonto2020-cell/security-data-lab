import pandas as pd

df = pd.read_csv("sample_logs.csv")

failed = df[df["status"] == "fail"]

ip_counts = failed["ip"].value_counts()

print("Failed login attempts per IP:")
print(ip_counts)
