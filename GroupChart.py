
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
regions = ["north", "south", "east", "west"]
jan=[120,100,80,90]
feb=[135,110,90,100]
dec=[200,210,180,190]
x=np.arange(len(regions))
width=0.35
plt.figure(figsize=(9, 5))
plt.bar(x - width/2, jan, width, label='Jan', color='blue')
plt.bar(x, feb, width, label='Feb', color='orange')
plt.bar(x + width/2, dec, width, label='Dec', color='green')

plt.title("Sales by Region for Jan, Feb, and Dec")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.show()