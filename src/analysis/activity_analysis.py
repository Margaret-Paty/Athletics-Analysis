import pandas as pd
# import matplotlib
# import matplotlib.pyplot as plt

def group_activities(df, group_by, metric):
    activities = df

    weekly = (activities.groupby(group_by)
            [metric]
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