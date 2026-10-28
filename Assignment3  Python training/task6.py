
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Step 1: Load dataset
gap = px.data.gapminder()

# Step 2: Select data for 2007
gap_2007 = gap[gap["year"] == 2007]

# Task 6: Correlation heatmap

# Step 1: Select columns and calculate correlation
corr = gap[["lifeExp", "pop", "gdpPercap"]].corr()

# Step 2: Draw heatmap
plt.figure(figsize=(8, 6))

sns.heatmap (
    corr,
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    fmt=".2f"
)

# Step 3: Add title and display
plt.title("Correlation Heatmap(2007)")
plt.tight_layout()
plt.show()
