import pandas as pd
from pathlib import Path
import json
from src.utils import garmin_sleep as gs
# Loading sleep data

sleep_folder = Path("data/raw/sleep")
json_files = sleep_folder.glob("*.json")

all_sleep = []

for file in json_files:
    with open(file, "r") as f:
        data = json.load(f)
        print(file)
        print(type(data))
        if isinstance(data, list):
            #print(data.keys())
            all_sleep.extend(data)
        elif isinstance(data, dict):
            print(data.keys())
            all_sleep.append(data["dailySleepDTO"])
            print("Adding:", data["dailySleepDTO"]["calendarDate"])          

df_sleep = pd.DataFrame(all_sleep)

df_sleep["sleepStartTimestampGMT"] = (
    df_sleep["sleepStartTimestampGMT"]
    .apply(gs.normalize_timestamp)
)

df_sleep["sleepEndTimestampGMT"] = (
    df_sleep["sleepEndTimestampGMT"]
    .apply(gs.normalize_timestamp)
)
df_sleep.sort_values("calendarDate")
df_sleep.to_csv("data/processed/raw_sleep_test.csv", index=False)


