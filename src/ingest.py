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

STATCAN_URL = "https://www150.statcan.gc.ca/t1/wds/rest/getDataFromVectorsAndLatestNPeriods"


def fetch_statcan_series(vector_id, name, latest_n):
    body = [{"vectorId": vector_id, "latestN": latest_n}]
    response = requests.post(STATCAN_URL, json=body, timeout=10)
    response.raise_for_status()
    data = response.json()

    points = data[0]["object"]["vectorDataPoint"]

    rows = []
    for point in points:
        rows.append({"date": point["refPer"], "value": point["value"]})

    df = pd.DataFrame(rows)
    df.to_csv(f"data/bronze/{name}.csv", index=False)
    print(f"Saved {len(df)} rows for {name}")
    return df

fetch_statcan_series(41690973, "cpi", 24)
fetch_statcan_series(2062815, "unemployment_rate", 24)

fetch_boc_series("FXUSDCAD", 30)
fetch_boc_series("V39079", 30)