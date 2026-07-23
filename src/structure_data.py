import pandas as pd
from pathlib import Path
import json

# Loading activity data

activity_folder = Path("data/raw/activities")

json_files = activity_folder.glob("*.json")



all_activities = []

for file in json_files: 
    with open(file, "r") as f:
        data = json.load(f)
        # print(file)
        # print(type(data))
        # print(data[0].keys())
        activities = data[0]["summarizedActivitiesExport"]
        # print(len(activities))
        # print(activities[0])
        all_activities.extend(activities)
        # print(len(all_activities))

df_act = pd.DataFrame(all_activities)
df_act.to_csv("data/clean/raw_activities.csv", index=False)

# print(df.head())
# print(df.columns)


# Loading sleep data




