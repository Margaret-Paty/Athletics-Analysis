import pandas as pd
from pathlib import Path
import ast
from src.utils import garmin_sleep as gs

def clean_sleep() :

    sleep = pd.read_csv("data/processed/raw_sleep.csv")

    # Convert date and time related columns
    sleep["sleep_start"] = pd.to_datetime(sleep["sleepStartTimestampGMT"], unit="ms")
    sleep["sleep_end"] = pd.to_datetime(sleep["sleepEndTimestampGMT"], unit="ms")
    sleep["sleep_duration"] = sleep["sleep_end"] - sleep["sleep_start"]
    sleep["sleep_hours"] = (sleep["sleep_duration"].dt.total_seconds() / 3600).round(2)
    sleep["date"] = pd.to_datetime(sleep["calendarDate"])
    sleep["year"] = sleep["date"].dt.year
    sleep["month"] = sleep["date"].dt.month
    sleep["week"] = sleep["date"].dt.isocalendar().week
    sleep["weekday"] = sleep["date"].dt.day_name()
    # Convert stages to minutes
    sleep["deep_minutes"] = sleep["deepSleepSeconds"] / 60
    sleep["light_minutes"] = sleep["lightSleepSeconds"] / 60
    sleep["rem_minutes"] = sleep["remSleepSeconds"] / 60
    sleep["awake_minutes"] = sleep["awakeSleepSeconds"]
    sleep["unmeasureable_minutes"] = sleep["unmeasurableSeconds"] / 60

    # Convert scores
    # Fill empty sleep score columns with empty dictionary
    sleep["sleepScores"] = sleep["sleepScores"].apply(gs.parse_sleep_scores) 
    sleep["sleepScores"] = sleep["sleepScores"].apply(gs.normalize_sleep_scores) 
    scores = pd.json_normalize(sleep["sleepScores"])

    # Fill empty score fields with zeroes
    scores = scores.fillna(0)

    sleep["overall_score"] = scores["overallScore"]
    sleep["quality_score"] = scores["qualityScore"]
    sleep["duration_score"] = scores["durationScore"]
    sleep["recovery_score"] = scores["recoveryScore"]
    sleep["deep_score"] = scores["deepScore"]
    sleep["light_score"] = scores["lightScore"]
    sleep["rem_score"] = scores["remScore"]
    sleep["deep_percent"] = scores["deepPercentage"]
    sleep["light_percent"] = scores["lightPercentage"]
    sleep["rem_percent"] = scores["remPercentage"]

    # Copy dataframe
    sleep = sleep.copy()

    # Designate columns for cleaned file
    clean_columns = [
        "date", 
        "year", 
        "month", 
        "week", 
        "weekday",
        "sleep_hours", 
        "deep_minutes", 
        "light_minutes", 
        "rem_minutes", 
        "awake_minutes", 
        "unmeasureable_minutes", 
        "overall_score", 
        "quality_score", 
        "duration_score", 
        "recovery_score", 
        "deep_score", 
        "rem_score", 
        "light_score",
        "deep_percent",
        "light_percent", 
        "rem_percent"
    ]

    # Put clean columns together for new dataframe
    sleep_clean = sleep[clean_columns]
    sleep_clean = sleep_clean.sort_values("date", axis=0)

    sleep_clean.to_csv("data/processed/clean/clean_sleep.csv", index=False)
    print("sleep cleaned")

if __name__ == "__main__":
    clean_sleep()