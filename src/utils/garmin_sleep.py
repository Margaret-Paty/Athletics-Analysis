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

    # Old Garmin export
    if "overallScore" in scores:
        return scores

    # New Garmin Connect API
    if "overall" in scores:

        return {
            "overallScore": scores.get("overall", {}).get("value"),

            "durationScore":
                scores.get("totalDuration", {}).get("qualifierKey"),

            "stressQualifier":
                scores.get("stress", {}).get("qualifierKey"),

            "awakeQualifier":
                scores.get("awakeCount", {}).get("qualifierKey"),

            "remScore":
                scores.get("remPercentage", {}).get("value"),

            "remQualifier":
                scores.get("remPercentage", {}).get("qualifierKey"),

            "lightScore":
                scores.get("lightPercentage", {}).get("value"),

            "lightQualifier":
                scores.get("lightPercentage", {}).get("qualifierKey"),

            "deepScore":
                scores.get("deepPercentage", {}).get("value"),

            "deepQualifier":
                scores.get("deepPercentage", {}).get("qualifierKey"),

            "restlessnessScore":
                scores.get("restlessness", {}).get("qualifierKey"),
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