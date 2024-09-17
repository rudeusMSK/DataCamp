#
# Exercise 1
#
import matplotlib.pyplot as plt

# Plotting two variables
# If you want to plot two time-series variables that were recorded at the same times, you can add both of them to the same subplot.

# If the variables have very different scales, you'll want to make sure that you plot them in different twin Axes objects. These objects can share one axis (for example, the time, or x-axis) while not sharing the other (the y-axis).

# To create a twin Axes object that shares the x-axis, we use the twinx method.

# In this exercise, you'll have access to a DataFrame that has the climate_change data loaded into it. This DataFrame was loaded with the "date" column set as a DateTimeIndex, and it has a column called "co2" with carbon dioxide measurements and a column called "relative_temp" with temperature measurements.

#
# Instructions
# 

# Use plt.subplots to create a Figure and Axes objects called fig and ax, respectively.
# Initalize a Figure and Axes
fig, ax = plt.subplots()
# Plot the carbon dioxide variable in blue using the Axes plot method.
# Plot the CO2 variable in blue
ax.plot(climate_change.index, climate_change["co2"], color='blue')
# Use the Axes twinx method to create a twin Axes that shares the x-axis.
ax2 = ax.twinx()
# Plot the relative temperature variable in red on the twin Axes using its plot method.
# Plot the relative temperature in red
ax2.plot(climate_change.index, climate_change["relative_temp"], color='red')
plt.show()

#
# Exercise 2
#

# Defining a function that plots time-series data
# Once you realize that a particular section of code that you have written is useful, it is a good idea to define a function that saves that section of code for you, rather than copying it to other parts of your program where you would like to use this code.
# Here, we will define a function that takes inputs such as a time variable and some other variable and plots them as x and y inputs. Then, it sets the labels on the x - and y-axis and sets the colors of the y-axis label, the y-axis ticks and the tick labels.

#
# Instructions
#

# Define a function called plot_timeseries that takes as input an Axes object(axes), data(x, y), a string with the name of a color and strings for x - and y-axis labels.
def plot_timeseries(axes, x, y, color, xlabel, ylabel):
# Plot y as a function of in the color provided as the input color.
  axes.plot(x, y, color=color)
# Set the x - and y-axis labels using the provided input xlabel and ylabel, setting the y-axis label color using color.
  axes.set_xlabel(xlabel)
  axes.set_ylabel(ylabel, color=color)
# Set the y-axis tick parameters using the tick_params method of the Axes object, setting the colors key-word to color.
  axes.tick_params('y', colors=color)


#
# Exercise 3
#
# Using a plotting function
# Defining functions allows us to reuse the same code without having to repeat all of it. Programmers sometimes say "Don't repeat yourself".

# In the previous exercise, you defined a function called plot_timeseries:

# plot_timeseries(axes, x, y, color, xlabel, ylabel)
# that takes an Axes object(as the argument axes), time-series data(as x and y arguments) the name of a color(as a string, provided as the color argument) and x-axis and y-axis labels(as xlabel and ylabel arguments). In this exercise, the function plot_timeseries is already defined and provided to you.

# Use this function to plot the climate_change time-series data, provided as a pandas DataFrame object that has a DateTimeIndex with the dates of the measurements and co2 and relative_temp columns.

#
# Instructions
#

# In the provided ax object, use the function plot_timeseries to plot the "co2" column in blue, with the x-axis label "Time (years)" and y-axis label "CO2 levels".
fig, ax = plt.subplots()
# Plot the CO2 levels time-series in blue
plot_timeseries(ax, climate_change.index,
                climate_change["co2"], "blue", "Time (years)", "CO2 levels")
# Use the ax.twinx method to add an Axes object to the figure that shares the x-axis with ax.
ax2 = ax.twinx()
# Use the function plot_timeseries to add the data in the "relative_temp" column in red to the twin Axes object, with the x-axis label "Time (years)" and y-axis label "Relative temperature (Celsius)".
plot_timeseries(ax2, climate_change.index,
                climate_change["relative_temp"], "red", "Time (years)", "Relative temperature (Celsius)")
