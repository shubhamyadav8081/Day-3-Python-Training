
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px

# Create DataFrame
df = pd.DataFrame({
    "month": ["jan", "feb", "mar", "apr", "may", "jun",
              "jul", "aug", "sep", "oct", "nov", "dec"],

    "north": [120, 135, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240],
    "south": [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210],
    "east": [90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],
    "west": [80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
})

# Calculate total sales
df["total_sales"] = df[["north", "south", "east", "west"]].sum(axis=1)

# Plot sales trend
plt.figure(figsize=(11, 5))

plt.plot(
    df["month"],
    df["total_sales"],
    marker="o",
    label="Total Sales",
    color="blue"
)

plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Sales Trend")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

