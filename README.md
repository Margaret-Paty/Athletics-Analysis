# Athletics Analysis

## Overview
Athletics Analysis is a Python-based data engineering and analytics project built around the Garmin Connect API. The goal is to automate the entire workflow from data collection to analysis.

The pipeline:
- logs into Garmin Connect
- Retrieves activity and wellness data
- Structures raw JSON into standardized datasets
- cleans and normalizes the data
- Produces analysis-ready CSV files

The long term goal is to build a dashboard that visualizes training trends, recovery metrics, and performance while serving as a portfolio project demonstratind data engineering, statistics, and software development.

## Data Organization

All Garmin data remains local and is excluded from version control.

```text
data/
    raw/
        activities/
        sleep/
        .../
    processed/
        raw_{metric}.csv
        clean/
            clean{metric}.csv
```
## Project Structure

```text
src/
    clean/
        clean_activity_data.py
        clean_sleep_data.py
    structure/
        structure_activities.py
        structure_sleep.py
    config/
        activity_schema.py
    utils/
        garmin_activity.py
        garmin_sleep.py
    retrieve_data.py
    pipeline.py
```

### Module Descriptions

| Module | Purpose |
| `retrieve_data.py` | Logs into Garmin Connect and downloads new data |
| `pipeline.py` | Runs the complete ETL pipeline |
| `structure/` | Converts raw Garmin JSON into standardized CSV files |
| `clean/` | Produces analysis-ready datasets |
| `config/` | Stores schema definitions used during normalization |
| `utils/` | Helper functions shared across the project |