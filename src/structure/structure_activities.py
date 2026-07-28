from src.config.activity_schema import ACTIVITY_COLUMN_MAP
import pandas as pd
from pathlib import Path
import json

def structure_activities() :
    # Loading activity data

    activity_folder = Path("data/raw/activities")

    json_files = activity_folder.glob("*.json")



    all_activities = []

    for file in json_files: 
        with open(file, "r") as f:
            data = json.load(f)

            if (
                isinstance(data, list)
                and len(data) > 0
                and isinstance(data[0], dict)
                and "summarizedActivitiesExport" in data[0]
            ):
                activities = data[0]["summarizedActivitiesExport"]
            else:
                activities = data

            all_activities.extend(activities)

    df_act = pd.DataFrame(all_activities)
    # Flatten nested Garmin fields

    def extract_type(value):
        if isinstance(value, dict):
            return value.get("typeKey")
        return value

    for column in ["activityType", "sportType", "privacy", "eventType"]:
        if column in df_act.columns:
            df_act[column] = df_act[column].apply(extract_type)

    # Rename columns to match previous activity schema

    rename_columns = {
        "startTimeGMT": "startTimeGmt",
        "averageSpeed": "avgSpeed",
        "maximumSpeed": "maxSpeed",
        "averageHeartRate": "avgHr",
        "maximumHeartRate": "maxHr",
        "averageBikingCadenceInRevPerMinute": "avgBikeCadence",
        "maximumBikingCadenceInRevPerMinute": "maxBikeCadence",
        "averageRunningCadenceInStepsPerMinute": "avgRunCadence",
        "maximumRunningCadenceInStepsPerMinute": "maxRunCadence",
    }

    df_act = df_act.rename(columns=rename_columns)

    # Remove duplicate activities

    def extract_type(value):
        if isinstance(value, dict):
            return value.get("typeKey")
        return value


    for column in ["activityType", "sportType", "privacy", "eventType"]:
        if column in df_act.columns:
            df_act[column] = df_act[column].apply(extract_type)



    # Rename columns using activity schema

    df_act = df_act.rename(
        columns=ACTIVITY_COLUMN_MAP
    )


    # Remove duplicate activities

    if "activity_id" in df_act.columns:
        df_act = (
            df_act.sort_values("start_timestamp")
                .drop_duplicates("activity_id", keep="last")
                )

    df_act.to_csv("data/processed/raw_activities.csv", index=False)
    print("activities structured")

if __name__ == "__main__":
    structure_activities()