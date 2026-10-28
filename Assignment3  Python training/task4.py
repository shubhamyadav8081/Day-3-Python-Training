
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Step 1: Load dataset
gap = px.data.gapminder()

# Step 2: Select 2007 data
gap_2007 = gap[gap["year"] == 2007]

# Step 3: Create two charts side by side
fig, ax = plt.subplots(1, 2, figsize=(14, 5))

# Step 4: Left chart - Linear scale
sns.scatterplot(
    data=gap_2007,
    x="gdpPercap",
    y="lifeExp",
    ax=ax[0]
)

ax[0].set_xlabel("GDP per Capita")
ax[0].set_ylabel("Life Expectancy (years)")
ax[0].set_title("Linear Scale")

# Step 5: Right chart - Log scale
sns.scatterplot(
    data=gap_2007,
    x="gdpPercap",
    y="lifeExp",
    ax=ax[1]
)

ax[1].set_xscale("log")
ax[1].set_xlabel("GDP per Capita (log scale)")
ax[1].set_ylabel("Life Expectancy (years)")
ax[1].set_title("Log Scale")

# Step 6: Display charts
plt.tight_layout()
plt.show()
