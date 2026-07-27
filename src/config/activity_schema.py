# Garmin activity column mapping
# Maps Garmin JSON fields to standardized dataframe column names

ACTIVITY_COLUMN_MAP = {

    # Activity identifiers
    "activityId": "activity_id",
    "name": "activity_name",
    "sportType": "sport_type",
    "activityType": "activity_type",
    "beginTimestamp": "start_timestamp",

    # Duration and distance
    "distance": "distance_meters",
    "duration": "duration_ms",
    "elapsedDuration": "elapsed_duration_ms",

    # Speed / pace
    "avgSpeed": "avg_speed",
    "maxSpeed": "max_speed",

    # Heart rate
    "avgHr": "avg_hr",
    "maxHr": "max_hr",

    # Cadence
    "avgBikeCadence": "avg_bike_cadence",
    "avgRunCadence": "avg_run_cadence",

    # Power
    "avgPower": "avg_power",
    "normPower": "norm_power",
    "maxPower": "max_power",

    # Training metrics
    "activityTrainingLoad": "training_load",
    "trainingEffectLabel": "training_effect",
    "aerobicTrainingEffect": "aerobic_effect",
    "anaerobicTrainingEffect": "anaerobic_effect",
    "trainingStressScore": "training_stress_score",

}


# Columns to keep as raw JSON
# These contain nested data that will be analyzed later

RAW_ACTIVITY_COLUMNS = [
    "splits",
    "measurements",
    "splitSummaries",
]