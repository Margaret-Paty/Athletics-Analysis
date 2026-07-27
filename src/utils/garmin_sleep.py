import ast
import pandas as pd
# This file contains util functions for sleep structure, cleaning, and analysis

# Go throught he sleep scores
def parse_sleep_scores(value):
    if (pd.isna(value)):
        return{}
    if isinstance(value, dict):
        return value
    if isinstance(value, str):
        return ast.literal_eval(value)
    return {}

def normalize_sleep_scores(scores):

    # Handle missing values
    if not isinstance(scores, dict):
        return {}

    # Old Garmin export
    if "overallScore" in scores:

        return {
            "overallScore": scores.get("overallScore"),
            "qualityScore": scores.get("qualityScore"),
            "durationScore": scores.get("durationScore"),
            "recoveryScore": scores.get("recoveryScore"),

            "deepScore": scores.get("deepScore"),
            "lightScore": scores.get("lightScore"),
            "remScore": scores.get("remScore"),

            "deepPercentage": None,
            "lightPercentage": None,
            "remPercentage": None,

            "feedback": scores.get("feedback"),
            "insight": scores.get("insight"),
        }


    # New Garmin Connect API
    if "overall" in scores:

        return {
            "overallScore": scores.get("overall", {}).get("value"),

            "qualityScore": None,
            "recoveryScore": None,

            "deepScore": None,
            "lightScore": None,
            "remScore": None,

            "deepPercentage":
                scores.get("deepPercentage", {}).get("value"),

            "lightPercentage":
                scores.get("lightPercentage", {}).get("value"),

            "remPercentage":
                scores.get("remPercentage", {}).get("value"),

            "durationScore":
                scores.get("totalDuration", {}).get("qualifierKey"),

            "feedback": None,
            "insight": None,
        }

    return {}

# get all timestamps in the right units
def normalize_timestamp(value):
    if pd.isna(value):
        return value

    # Already milliseconds
    if isinstance(value, (int, float)):
        return value

    # ISO string
    if isinstance(value, str):
        return int(pd.Timestamp(value).timestamp() * 1000)

    return value  