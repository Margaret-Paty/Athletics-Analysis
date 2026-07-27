import pandas as pd
from pathlib import Path
import json
from src.utils import garmin_sleep as gs
# Loading sleep data

def structure_sleep():
    sleep_folder = Path("data/raw/sleep")
    json_files = sleep_folder.glob("*.json")

    all_sleep = []

    for file in json_files:
        with open(file, "r") as f:
            data = json.load(f)
            if isinstance(data, list):
                all_sleep.extend(data)
            elif isinstance(data, dict):
                all_sleep.append(data["dailySleepDTO"])

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
    df_sleep.to_csv("data/processed/raw_sleep.csv", index=False)
    
    print("sleep structured")

if __name__ == "__main__":
    structure_sleep()
