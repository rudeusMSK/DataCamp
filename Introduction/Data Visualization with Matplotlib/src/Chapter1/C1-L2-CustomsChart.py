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

#
##
#

# Create a figure and an array of axes: 2 rows, 1 column with shared y axis
fig, ax = plt.subplots(2, 1, sharey=True)

# Plot Seattle precipitation data in the top axes
ax[0].plot(seattle_weather["MONTH"],
           seattle_weather["MLY-PRCP-NORMAL"], color='b')
ax[0].plot(seattle_weather["MONTH"],
           seattle_weather["MLY-PRCP-25PCTL"], color='b', linestyle='--')
ax[0].plot(seattle_weather["MONTH"],
           seattle_weather["MLY-PRCP-75PCTL"], color='b', linestyle='--')

# Plot Austin precipitation data in the bottom axes
ax[1].plot(austin_weather["MONTH"],
           austin_weather["MLY-PRCP-NORMAL"], color='r')
ax[1].plot(austin_weather["MONTH"],
           austin_weather["MLY-PRCP-25PCTL"], color='r', linestyle='--')
ax[1].plot(austin_weather["MONTH"],
           austin_weather["MLY-PRCP-75PCTL"], color='r', linestyle='--')

plt.show()
