# Athletics Analysis

## Overview
Athletics Analysis is a Python-based data engineering and analytics project built around the Garmin Connect API. The goal is to automate the entire workflow from data collection to analysis.

The pipeline:
- logs into Garmin Connect
- Retrieves activity and wellness data
- Structures raw JSON into standardized datasets
- cleans and normalizes the data
- Produces analysis-ready CSV files
- Performs exploratory analysis on training, recovery, and performance trends

The pipeline is automated to run everyday at 2300 (11 pm) and pull sleep and activity data from that day.

The long term goal is to build a dashboard that visualizes training trends, recovery metrics, and performance while serving as a portfolio project demonstrating data engineering, statistics, and software development.

## Data Pipeline

The project follows an ETL (Extract, Transform, Load) workflow:

```text
Garmin Connect API
        ↓
Raw JSON Data
        ↓
Structured CSV Files
        ↓
Clean Analysis Datasets
        ↓
Statistical Analysis
        ↓
Visualization / Dashboard
```

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
            clean_{metric}.csv
```

## Analysis
Exploratory analysis is performed using Jupyter notebooks.

Current analyses include:
- Weekly mileage trends
- Sleep trends by week
- Relationship between sleep and running performance

Future analysis goals include:
- Recovery modeling
- Training optimization
- Performance prediction
- Interactive dashboard development

```text
notebooks/
    explore_activities.ipynb
    explore_sleep.ipynb
```

## Project Structure

```text
src/
    analysis/
        activity_analysis.py
        sleep_analysis.py
        sleep_and_activities.py
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
        logger.py
    retrieve_data.py
    pipeline.py
```

### Module Descriptions

 Module | Purpose 

- `retrieve_data.py` | Logs into Garmin Connect and downloads new data 
- `pipeline.py` | Runs the complete ETL pipeline 
- `structure/` | Converts raw Garmin JSON into standardized CSV files 
-  `clean/` | Produces analysis-ready datasets 
-  `config/` | Stores schema definitions used during normalization 
-  `utils/` | Helper functions shared across the project and logs for automation
- `analysis/` | Analysis functions based on code tested in the Jupyter notebook

## Technologies

- Python
- Pandas
- NumPy
- Jupyter Notebook
- Garmin Connect API
- Git/GitHub
- Automation (Mac Launcher)