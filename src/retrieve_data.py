from garminconnect import Garmin
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime
import json
import os

# Path for the raw  data
def retrieve_data():
    PATH_RAW = Path("data/raw/")

    # Make sure you use a .env file, don't have your password just in the world
    BASE_DIR = Path(__file__).resolve().parent.parent
    load_dotenv(BASE_DIR/".env")

    username = os.getenv("GARMIN_USERNAME")
    password = os.getenv("GARMIN_PASSWORD")


    # creating the client to login and actually get the data
    garmin = Garmin(username, password)

    garmin.login()

    today = datetime.now().strftime("%Y-%m-%d")

    # retrieve all activity data
    activities = garmin.get_activities_by_date(today)


    # pipe to raw file
    file = (PATH_RAW / "activities/" / f"activities_{today}.json" )

    with open(file, "w") as f:
        json.dump(activities, f, indent=4)
        
    # Get sleep data for today
    sleep = garmin.get_sleep_data(today)

    # Pipe to raw file
    file = (PATH_RAW / "sleep/" / f"sleep_{today}.json")
    with open(file, "w") as f:
        json.dump(sleep, f, indent=4)

    # Get race predictions as of today
    race_predictions = garmin.get_race_predictions()

    # Pipe to raw file
    file = (PATH_RAW / "race predictions/" / f"predictions_{today}.json")
    with open(file, "w") as f:
        json.dump(race_predictions, f, indent=4)
    print("data retrieved")

if __name__ == "__main__":
    retrieve_data()