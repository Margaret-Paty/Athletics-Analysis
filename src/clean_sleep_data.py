import pandas as pd
from pathlib import Path
import ast

sleep = pd.read_csv("data/processed/raw_sleep.csv")

# print(sleep.head())
# print(sleep.info())

# columns = 
# sleep_start
# sleep_end
# date
# deep_minutes
# light_minutes
# rem_minutes
# awake_minutes
# unmeasureable_minutes
# overall_score
# quality_score
# duration_score
# recovery_score
# deep_score
# rem_score
# light_score

# Convert date and time related columns
sleep["sleep_start"] = pd.to_datetime(sleep["sleepStartTimestampGMT"], unit="ms")
sleep["sleep_end"] = pd.to_datetime(sleep["sleepEndTimestampGMT"], unit="ms")
sleep["sleep_duration"] = sleep["sleep_end"] - sleep["sleep_start"]
sleep["sleep_hours"] = (sleep["sleep_duration"].dt.total_seconds() / 3600).round(2)
sleep["date"] = sleep["calendarDate"]

# Convert stages to minutes
sleep["deep_minutes"] = sleep["deepSleepSeconds"] / 60
sleep["light_minutes"] = sleep["lightSleepSeconds"] / 60
sleep["rem_minutes"] = sleep["remSleepSeconds"] / 60
sleep["awake_minutes"] = sleep["awakeSleepSeconds"]
sleep["unmeasureable_minutes"] = sleep["unmeasurableSeconds"] / 60

# Convert scores
# Fill empty sleep score columns with empty dictionary
sleep["sleepScores"] = sleep["sleepScores"].apply(
    lambda x: ast.literal_eval(x) if pd.notna(x) else {}) 
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

# Copy dataframe
sleep = sleep.copy()

# Designate columns for cleaned file
clean_columns = [
    "date", 
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
    "light_score"
]

# Put clean columns together for new dataframe
sleep_clean = sleep[clean_columns]

sleep_clean.to_csv("data/processed/clean/clean_sleep.csv", index=False)



