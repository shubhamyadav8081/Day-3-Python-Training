
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px

# Data define karna
df = pd.DataFrame({
    "month": ["jan", "feb", "mar", "apr", "may", "jun",
              "jul", "aug", "sep", "oct", "nov", "dec"],

    "north": [120, 135, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240],
    "south": [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210],
    "east": [90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],
    "west": [80, 90, 190, 110, 120, 130, 140, 150, 160, 170, 180, 220]
})

regions = ["north", "south", "east", "west"]

jan = [120, 100, 80, 90]
feb = [135, 110, 90, 100]
dec = [200, 210, 180, 190]

x = np.arange(len(regions))

plt.figure(figsize=(9, 5))

for region in ["north", "south", "east", "west"]:
    plt.plot(
        df["month"],
        df[region],
        marker="o",
        label=region
    )

plt.title("Region Sales Performance")
plt.xlabel("Month")
plt.ylabel("Sales (thousands)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

