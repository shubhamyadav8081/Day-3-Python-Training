
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
regions = ["north", "south", "east", "west"]
sales=[120,100,80,90]
plt.figure(figsize=(9, 5))
plt.bar(regions, sales, color=['blue', 'orange', 'green', 'red'])
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.grid(axis="y",alpha=0.3)

plt.show()