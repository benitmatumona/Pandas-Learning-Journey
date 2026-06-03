import pandas as pd

df = pd.read_csv("fifa_data.csv")

df.groupby("Nationality").Age.agg(["count", "mean", "median", "mode", "range"])