import requests 
import pandas as pd

url = "https://www.bankofcanada.ca/valet/observations/FXUSDCAD/json?recent=30"
response = requests.get(url, timeout=10)
data = response.json()

rows = []
for obs in data["observations"]:
    date = obs["d"]
    rate = float(obs["FXUSDCAD"]["v"])
    rows.append({"date": date, "usd_cad": rate})

df = pd.DataFrame(rows)
print(df.head())

df.to_csv("data/bronze/FXUSDCAD.csv", index=False)
print("Saved", len(df), "rows")
