# Exercise 1
# Adding error-bars to a plot
# Adding error-bars to a plot is done by using the errorbar method of the Axes object.

# Here, you have two DataFrames loaded: seattle_weather has data about the weather in Seattle and austin_weather has data about the weather in Austin. Each DataFrame has a column "MONTH" that has the names of the months, a column "MLY-TAVG-NORMAL" that has the average temperature in each month and a column "MLY-TAVG-STDDEV" that has the standard deviation of the temperatures across years.

# In the exercise, you will plot the mean temperature across months and add the standard deviation at each point as y errorbars.

# Instructions
# 100 XP
# Use the ax.errorbar method to add the Seattle data: the "MONTH" column as x values, the "MLY-TAVG-NORMAL" as y values and "MLY-TAVG-STDDEV" as yerr values.
# Add the Austin data: the "MONTH" column as x values, the "MLY-TAVG-NORMAL" as y values and "MLY-TAVG-STDDEV" as yerr values.
# Set the y-axis label as "Temperature (Fahrenheit)".
fig, ax = plt.subplots()

# Add Seattle temperature data in each month with error bars
ax.errorbar(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"],
            yerr=seattle_weather["MLY-TAVG-STDDEV"])

# Add Austin temperature data in each month with error bars
ax.errorbar(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"],
            yerr=austin_weather["MLY-TAVG-STDDEV"])
# Set the y-axis label
ax.set_ylabel("Temperature (Fahrenheit)")

plt.show()


# Exercise 2
# Creating boxplots
# Boxplots provide additional information about the distribution of the data that they represent. They tell us what the median of the distribution is , what the inter-quartile range is and also what the expected range of approximately 99 % of the data should be. Outliers beyond this range are particularly highlighted.

# In this exercise, you will use the data about medalist heights that you previously visualized as histograms, and as bar charts with error bars, and you will visualize it as boxplots.

# Again, you will have the mens_rowing and mens_gymnastics DataFrames available to you, and both of these DataFrames have columns called "Height" that you will compare.

# Instructions
# 100 XP
# Create a boxplot that contains the "Height" column for mens_rowing on the left and mens_gymnastics on the right.
# Add x-axis tick labels: "Rowing" and "Gymnastics".
# Add a y-axis label: "Height (cm)".

fig, ax = plt.subplots()

# Add a boxplot for the "Height" column in the DataFrames
ax.boxplot([mens_rowing["Height"], mens_gymnastics["Height"]])

# Add x-axis tick labels:
ax.set_xticklabels(["Rowing", "Gymnastics"])

# Add a y-axis label
ax.set_ylabel("Height (cm)")

plt.show()
