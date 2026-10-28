
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px

np.random.seed(42)

df = pd.DataFrame({
    "month": ["jan", "feb", "mar", "apr", "may", "jun",
              "jul", "aug", "sep", "oct", "nov", "dec"],

    "north": [120, 135, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240],
    "south": [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210],
    "east": [90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],
    "west": [80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],

    "Marketing_spend": [20, 25, 28, 30, 32, 35, 38, 40, 42, 45, 48, 50],
    "customers": [200, 240, 280, 310, 350, 390, 420, 460, 490, 530, 570, 610]
})

# Total sales
df["total_sales"] = df[["north", "south", "east", "west"]].sum(axis=1)

# Profit
df["profit"] = (df["total_sales"] * 0.20).round(2)

# Average data
print("\n===== AVERAGE DATA =====")
print(df[["north", "south", "east", "west",
          "total_sales", "profit", "Marketing_spend",
          "customers"]].mean().round(2))

# Group-wise data: month-wise data ko quarters mein group karna
df["quarter"] = ["Q1", "Q1", "Q1",
                 "Q2", "Q2", "Q2",
                 "Q3", "Q3", "Q3",
                 "Q4", "Q4", "Q4"]

print("\n===== GROUP-WISE DATA =====")
group_data = df.groupby("quarter")[
    ["total_sales", "profit", "Marketing_spend", "customers"]
].mean().round(2)

print(group_data)

# Complete data
print("\n===== COMPLETE DATA =====")
print(df)
