import pandas as pd
import plotly_express as px
import plotly.figure_factory as ff
import csv

df = pd.read_csv("c108.csv")

arr = df["Avg Rating"].tolist()

fig = ff.create_distplot([arr],["Avg rating"])
fig.show()
