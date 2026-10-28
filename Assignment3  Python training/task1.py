import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

gap = px.data.gapminder()
gap_2007 = gap[gap["year"] == 2007]

# Top 10 countries by population
top10 = gap_2007.nlargest(10, "pop").copy()

# Convert population into millions
top10["pop_millions"] = top10["pop"] / 1_000_000

# Sort population in ascending order
top10 = top10.sort_values("pop_millions", ascending=False)

# Create vertical bar graph
plt.figure(figsize=(12, 6))

plt.bar(top10["country"], top10["pop_millions"])

plt.xlabel("Country")
plt.ylabel("Population (millions)")
plt.title("Top 10 Countries by Population in 2007")

# Rotate country names
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.show()
