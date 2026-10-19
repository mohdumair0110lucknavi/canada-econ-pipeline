# import requests 
# import pandas as pd

# url = "https://www.bankofcanada.ca/valet/observations/FXUSDCAD/json?recent=30"
# response = requests.get(url, timeout=10)
# data = response.json()

# rows = []
# for obs in data["observations"]:
#     date = obs["d"]
#     rate = float(obs["FXUSDCAD"]["v"])
#     rows.append({"date": date, "usd_cad": rate})

# df = pd.DataFrame(rows)
# print(df.head())

# df.to_csv("data/bronze/FXUSDCAD.csv", index=False)
# print("Saved", len(df), "rows")
# Week 1 stuff
import requests
import pandas as pd

def fetch_boc_series(code, recent):
    url = f"https://www.bankofcanada.ca/valet/observations/{code}/json?recent={recent}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    rows = []
    for obs in data["observations"]:
        rows.append({"date": obs["d"], "value": float(obs[code]["v"])})

    df = pd.DataFrame(rows)
    df.to_csv(f"data/bronze/{code}.csv", index=False)
    print(f"Saved {len(df)} rows for {code}")
    return df

fetch_boc_series("FXUSDCAD", 30)
fetch_boc_series("V39079", 30)