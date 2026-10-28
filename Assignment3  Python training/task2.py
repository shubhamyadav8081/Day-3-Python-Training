import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

gap = px.data.gapminder()

# Step 1: Select 1952 and 2007 data
g = gap[gap["year"].isin([1952, 2007])].groupby(
    ["continent", "year"]
)["lifeExp"].mean().unstack()

# Step 2: Print the average life expectancy table
print(g.round(2))

# Step 3: Draw grouped bar chart
g.plot(kind="bar", figsize=(10, 6))

plt.xlabel("Continent")
plt.ylabel("Average Life Expectancy (years)")
plt.title("Life Expectancy by Continent: 1952 vs 2007")
plt.xticks(rotation=0)
plt.legend(title="Year")
plt.tight_layout()
plt.show()

# Step 4: Find the continent with the greatest improvement
improvement = g[2007] - g[1952]

print("\nLife expectancy improvement:")
print(improvement.round(2))

print("\nMost improved continent:", improvement.idxmax())
