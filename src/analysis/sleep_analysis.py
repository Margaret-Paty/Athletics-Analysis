import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# weekly_average computes the average number of hours of sleep per night for each week
def weekly_average():
    sleep = pd.read_csv("../data/processed/clean/clean_sleep.csv")

    sleep_weekly = (sleep.groupby(["year", "week"])
                    ["sleep_hours"]
                    .mean())

    sleep_weekly.plot()



