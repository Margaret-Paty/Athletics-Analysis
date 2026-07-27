This project is designed to allow me to, in one script: log in to Garmin, retrieve whatever data I want, structure and clean the data into .csv files that can be used for analysis, and analyze the data however I want to. The script has been automated to run every day at a certain time and pull all of the data for that day from the Garmin API.
Ultimately, there will be a dashboard with some data visualization, and moe advanced analytics. 

All data exists only on my computer, and does not get uploaded to git, but is structured as follows:
data/
    raw/
        individual metric folder/
            .json files
    processed/
        raw_{metric}.csv
        clean/
            clean{metric}.csv

The code structure for this project is as follows (with explanations):
src/
    clean/
        clean_activity_data.py -> cleans the raw activity csv file (end result only includes metrics I want)
        clean_sleep_data.py -> cleans the raw sleep csv file
    structure/
        structure_activities.py -> structures the activity json files into csv, normalizes column names
        structure_sleep.py -> structures the sleep json files into csv, normalizes units
    config/
        activity_schema.py -> outlines column names for the activity csv file, helps with normalizing the data
    utils/
        garmin_activity.py -> includes helper functions for activity cleaning and analysis
        garmin_sleep.py -> includes helper functions for sleep cleaning and analysis
    retrieve_data.py -> actually logs into garmin and pulls all of the data
    pipeline.py -> combines all programs into one data pipeline to maximize efficiency (retrieval through cleaning)

