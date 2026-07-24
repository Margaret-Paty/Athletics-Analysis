from garminconnect import Garmin
from dotenv import load_dotenv
from dotenv import dotenv_values
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR/".env")

username = os.getenv("GARMIN_USERNAME")
password = os.getenv("GARMIN_PASSWORD")

# creating the client to login and actually get the data
garmin = Garmin(username, password)

garmin.login()

# retrieve all data


# pipe to raw file


