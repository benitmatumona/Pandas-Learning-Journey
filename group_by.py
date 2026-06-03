import pandas as pd

df = pd.read_csv("fifa_data.csv")

countries = df.groupby("Nationality").Age.agg(["count", "mean", "median", "mode", "range"])

mean_numerical_data = df.groupby("Nationality").mean()