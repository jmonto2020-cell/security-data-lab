import pandas as pd

# load logs
df = pd.read_csv("sample_logs.csv")

# filter failed logins
failed = df[df["status"] == "fail"]

# count suspicious IPs
ip_counts = failed["ip"].value_counts()

print("Suspicious activity (failed logins):")
print(ip_counts)
