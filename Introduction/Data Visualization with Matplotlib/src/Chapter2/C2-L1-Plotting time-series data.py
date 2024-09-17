#
# Exercise 1
#

# Read data with a time index
# pandas DataFrame objects can have an index denoting time, this recognized by Matplotlib for axis labeling.

# This exercise involves reading data from climate_change.csv, containing CO2 levels and temperatures recorded on the 6th of each month from 1958 to 2016,
#  using pandas' read_csv function. The parse_dates and index_col arguments help set a DateTimeIndex.

# Don't forget to check out the Matplotlib Cheat Sheet for a quick overview of essential concepts and methods.

#
# Instructions
#

# Import the pandas library as pd.
import matplotlib.pyplot as plt
import pandas as pd

# Read in the data from a CSV file called 'climate_change.csv' using pd.read_csv.
# Use the parse_dates key-word argument to parse the "date" column as dates.
# Use the index_col key-word argument to set the "date" column as the index.
climate_change = pd.read_csv('climate_change.csv', parse_dates=["date"], index_col="date")

#
# Exercise 2
#

# Plot time-series data
# To plot time-series data, we use the Axes object plot command. The first argument to this method are the values for the x-axis and the second argument are the values for the y-axis.

# This exercise provides data stored in a DataFrame called climate_change. This variable has a time-index with the dates of measurements and two data columns: "co2" and "relative_temp".

# In this case, the index of the DataFrame would be used as the x-axis values and we will plot the values stored in the "relative_temp" column as the y-axis values. We will also properly label the x-axis and y-axis.

#
# Instructions
#

# Add the data from climate_change to the plot: use the DataFrame index for the x value and the "relative_temp" column for the y values.
fig, ax = plt.subplots()
# Add the time-series for "relative_temp" to the plot
ax.plot(climate_change.index, climate_change['relative_temp'])
# Set the x-axis label to 'Time'.
ax.set_xlabel('Time')
# Set the y-axis label to 'Relative temperature (Celsius)'.
ax.set_ylabel('Relative temperature (Celsius)')
# Show the figure.
plt.show()

#
# Exercise 3
#
# Using a time index to zoom in
# When a time-series is represented with a time index, we can use this index for the x-axis when plotting. We can also select a range of dates to zoom in on a particular period within the time-series using pandas' indexing facilities. In this exercise, you will select a portion of a time-series dataset and you will plot that period.

# The data to use is stored in a DataFrame called climate_change, which has a time-index with dates of measurements and two data columns: "co2" and "relative_temp".

#
# Instructions
#

# Use plt.subplots to create a Figure with one Axes called fig and ax, respectively.
fig, ax = plt.subplots()
# Create a variable called seventies that includes all the data between "1970-01-01" and "1979-12-31".
seventies = climate_change["1970-01-01":"1979-12-31"]
# Add the data from seventies to the plot: use the DataFrame index for the x value and the "co2" column for the y values.
ax.plot(seventies.index, seventies["co2"])
# Show the figure
plt.show()
