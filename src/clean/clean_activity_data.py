import pandas as pd
from pathlib import Path

def clean_activities():
    # clean activities
    activities = pd.read_csv("data/processed/raw_activities.csv")

    print(activities.columns.tolist())

    # print(activities.head())
    # print(activities.info())

    #Rename  activity detail columns
    activities["sport_type"] = activities["sport_type"].str.lower()
    activities["activity_type"] = (activities["activity_type"].str.title().str.replace("_", " "))

    # Convert time and date fields
    activities["start_time"] = pd.to_datetime(activities["start_timestamp"], unit="ms")
    activities["time_of_day"] = activities["start_time"].dt.strftime("%H:%M:%S")
    activities["date"] = activities["start_time"].dt.date
    activities["year"] = activities["start_time"].dt.year
    activities["month"] = activities["start_time"].dt.month
    activities["week"] = activities["start_time"].dt.isocalendar().week
    activities["weekday"] = activities["start_time"].dt.day_name()

    # Convert duration field
    activities["duration_minutes"] = (activities["duration_ms"] / 1000 / 60).round(1)
    activities["duration_hours"] = (activities["duration_ms"] / 1000 / 3600).round(2)
    activities["duration_elapsed"] = activities["elapsed_duration_ms"]

    # Convert distance
    activities["distance_miles"] = (activities["distance_meters"] / 160934).round(2)

    # Convert speed
    activities["avg_speed_mph"] = (activities["avg_speed"] * 2.237).round(1)
    activities["max_speed_mph"] = (activities["max_speed"] * 2.237).round(1)
    activities["avg_pace"] = (60 / activities["avg_speed"])

    # Convert heart rate
    activities["avg_hr"] = activities["avg_hr"].round(0)
    activities["max_hr"] = activities["max_hr"].round(0)

    # Convert cadence
    activities["avg_bike_cadence_rpm"] = (activities["avg_bike_cadence"].round(0))
    activities["avg_run_cadence_spm"] = (activities["avg_run_cadence"].round(0))

    # Convert power
    activities["avg_power"] = activities["avg_power"].round(0)
    activities["norm_power"] = activities["norm_power"].round(0)
    activities["max_power"] = activities["max_power"].round(0)

    # Convert calories, training load, and stress
    activities["calories"] = activities["calories"].round(0)
    activities["training_load"] = activities["training_load"].round(2)
    activities["training_effect"] = (activities["training_effect"].str.title())
    activities["aerobic_effect"] = (activities["aerobic_effect"].round(2))
    activities["anaerobic_effect"] = (activities["anaerobic_effect"].round(2))
    activities["training_stress_score"] = (activities["training_stress_score"].round(2))

    activities = activities.copy()

    # Select final columns for cleaned dataset
    clean_columns = [
        "activity_id",
        "activity_name",
        "sport_type",
        "activity_type",
        "start_time",
        "time_of_day",
        "date",
        "year",
        "month",
        "week",
        "weekday",
        "duration_minutes",
        "duration_hours",
        "avg_hr",
        "max_hr",
        "distance_miles",
        "avg_pace",
        "avg_speed_mph",
        "max_speed_mph",
        "avg_bike_cadence_rpm",
        "avg_run_cadence_spm",
        "avg_power",
        "norm_power",
        "max_power",
        "calories",
        "training_load",
        "training_effect",
        "aerobic_effect",
        "anaerobic_effect",
        "training_stress_score"
    ]

    activities_clean = activities[clean_columns]

    # Get rid of duplicates
    activities_clean = activities_clean.drop_duplicates("activity_id")

    # Load clean version of data
    activities_clean.to_csv("data/processed/clean/clean_activities.csv", index=False)
    
    print("activities cleaned")

if __name__ == "__main__":
    clean_activities()