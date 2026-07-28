import pandas as pd
# import matplotlib
# import matplotlib.pyplot as plt

def weekly_mileage_complete():
    activities = pd.read_csv("../data/processed/clean/clean_activities.csv")

    weekly = (activities.groupby(["year", "week"])
            ["distance_miles"]
            .sum())

    return weekly

def weekly_yards(df, year, week, sports):
    if isinstance(sports, str):
        sports = [sports]

    yards = (
        (
            df[
                (df["activity_type"].isin(sports)) & 
                (df["year"] == year) & 
                (df["week"] == week)
            ]["distance_miles"] * 1760
        )
        .sum()
    )
    return yards

def weekly_mileage(df, year, week, sports):
    if isinstance(sports, str):
        sports = [sports]

    mileage = (
        df[
            (df["activity_type"].isin(sports)) & 
            (df["year"] == year) & 
            (df["week"] == week)
        ]["distance_miles"]
        .sum()
    )
    return mileage