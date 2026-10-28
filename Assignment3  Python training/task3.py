import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

gap = px.data.gapminder()



# Step 1: Select four countries
countries = gap[gap["country"].isin([
    "India",
    "China",
    "Brazil",
    "United States"
])]

# Step 2: Draw line chart
plt.figure(figsize=(12, 6))

sns.lineplot(
    data=countries,
    x="year",
    y="lifeExp",
    hue="country",
    marker="o"
)

# Step 3: Add labels and title
plt.xlabel("Year")
plt.ylabel("Life Expectancy (years)")
plt.title("Life Expectancy Over Time: Four Countries")
plt.legend(title="Country")
plt.tight_layout()
plt.show()
