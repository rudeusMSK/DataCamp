import matplotlib.pyplot as plt
import pandas as pd  # <- pip install pandas
import os  # <- input/output

fig, ax = plt.subplots()
seattle_weather = pd.read_csv("Buoi1/Data/kaggle/input/seattle_weather.csv")
austin_weather = pd.read_csv("Buoi1/Data/kaggle/input/austin_weather.csv")

ax.plot(seattle_weather["MONTH"], 
        seattle_weather["MLY-PRCP-NORMAL"],
        marker='o',
        linestyle='--',
        color='r')
ax.plot(austin_weather["MONTH"],
         austin_weather["MLY-PRCP-NORMAL"],
         marker='v',
         linestyle='--',
         color='b')

# Customize the x-axis label
ax.set_xlabel("Time (months)")

# Customize the y-axis label
ax.set_ylabel("Precipitation (inches)")

# Add the title
ax.set_title("Weather patterns in Austin and Seattle")

# Display the figure
plt.show()
