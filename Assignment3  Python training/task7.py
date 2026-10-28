
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the Gapminder dataset
gap = px.data.gapminder()

# Create a table: continents as rows, years as columns
pivot = gap.pivot_table(
    index="continent",
    columns="year",
    values="lifeExp",
    aggfunc="mean"
)

# Draw the heatmap
plt.figure(figsize=(14, 6))

sns.heatmap(
    pivot,
    annot=True,
    fmt=".0f",
    cmap="YlGnBu"
)

plt.title("Average Life Expectancy by Continent and Year")
plt.xlabel("Year")
plt.ylabel("Continent")
plt.tight_layout()
plt.show()
