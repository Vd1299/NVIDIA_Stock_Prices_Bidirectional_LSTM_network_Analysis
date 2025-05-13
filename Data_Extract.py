import os
import requests
import pandas as pd
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("api_key")

# Constants
SYMBOL = "NVDA"
TIMESPAN = "minute"
MULTIPLIER = 1
ADJUSTED = "true"
LIMIT = 50000
MARKET_HOURS = "regular"
BASE_URL = f"https://api.polygon.io/v2/aggs/ticker/{SYMBOL}/range/{MULTIPLIER}/{TIMESPAN}"

# Time range
END_DATE = datetime.now(timezone.utc)
START_DATE = END_DATE - timedelta(days=180)

# Convert to ISO format
start_date_str = START_DATE.strftime('%Y-%m-%d')
end_date_str = END_DATE.strftime('%Y-%m-%d')

def fetch_data(from_date: str, to_date: str):
    all_results = []
    url = f"{BASE_URL}/{from_date}/{to_date}"
    params = {
        "adjusted": ADJUSTED,
        "sort": "asc",
        "limit": LIMIT,
        "apiKey": API_KEY,
        "marketHours": MARKET_HOURS
    }

    next_url = None
    while True:
        if next_url:
            full_next_url = f"{next_url}&apiKey={API_KEY}"
            print(f"Requesting: {full_next_url}")
            res = requests.get(full_next_url)
        else:
            print(f"Requesting: {url}")
            res = requests.get(url, params=params)

        if res.status_code != 200:
            raise Exception(f"Error: {res.status_code} - {res.text}")

        json_data = res.json()
        results = json_data.get("results", [])
        all_results.extend(results)

        next_url = json_data.get("next_url")
        if not next_url:
            break

    return all_results


# Fetch data
results = fetch_data(start_date_str, end_date_str)

# Convert to DataFrame
df = pd.DataFrame(results)
df['timestamp'] = pd.to_datetime(df['t'], unit='ms')
df.rename(columns={
    'o': 'open',
    'h': 'high',
    'l': 'low',
    'c': 'close',
    'v': 'volume'
}, inplace=True)

df['symbol'] = SYMBOL

df = df[['symbol','timestamp' ,'open', 'high', 'low', 'close', 'volume']]


# Save to CSV
df.to_csv("nvda_180_days_minute_data.csv", index=False)
print(f"✅ Fetched {len(df)} records of NVDA minute-level data (last 90 days, regular hours).")
