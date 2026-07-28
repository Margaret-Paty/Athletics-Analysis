import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# weekly_average computes the average number of hours of sleep per night for each week
def weekly_average():
    sleep = pd.read_csv("../data/processed/clean/clean_sleep.csv")

    sleep_weekly = (sleep.groupby(["year", "week"])
                    ["sleep_hours"]
                    .mean())
    
    return sleep_weekly

def avg_metric(df, year, group, target, metric):
    sleep = (
        df [
            (df["year"] == year) &
            (df[group] == target) 
        ][metric]
        .mean()
    ).round(2)
    return sleep

def group_sleep(df, filters, group_by, metric, order=None):
    filtered = df.copy()

    for column, value in filters.items():
        filtered = filtered[filtered[column] == value]

    sleep_group = (
        filtered
        .groupby(group_by)[metric]
        .mean()
    )

    if order is not None:
        sleep_group = sleep_group.reindex(order)

    return sleep_group


