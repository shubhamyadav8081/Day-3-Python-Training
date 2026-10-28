
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Step 1: Load dataset
gap = px.data.gapminder()

# Step 2: Select data for 2007
gap_2007 = gap[gap["year"] == 2007]

# Step 3: Create interactive bubble chart
fig = px.scatter(
    gap_2007,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=50,
    title="GDP per Capita vs Life Expectancy in 2007"
)

fig.update_layout(
    xaxis_title="GDP per Capita (log scale)",
    yaxis_title="Life Expectancy (years)"
)

# Step 4: Display interactive chart
fig.show()
