#
# Exercise 1
#

# Bar chart
# Bar charts visualize data that is organized according to categories as a series of bars, where the height of each bar represents the values of the data in this category.

# For example, in this exercise, you will visualize the number of gold medals won by each country in the provided medals DataFrame. The DataFrame contains the countries as the index, and a column called "Gold" that contains the number of gold medals won by each country, according to their rows.

#
# Instructions
#

# Call the ax.bar method to plot the "Gold" column as a function of the country.
fig, ax = plt.subplots()
# Plot a bar-chart of gold medals as a function of country
ax.bar(medals.index, medals["Gold"])
# Use the ax.set_xticklabels to set the x-axis tick labels to be the country names.
# In the call to ax.set_xticklabels rotate the x-axis tick labels by 90 degrees by using the rotation key-word argument.
ax.set_xticklabels(medals.index, rotation=90)
# Set the y-axis label to "Number of medals".
ax.set_ylabel("Number of medals")
plt.show()

#
# Exercise 2
#

# Stacked bar chart
# A stacked bar chart contains bars, where the height of each bar represents values. In addition, stacked on top of the first variable may be another variable. The additional height of this bar represents the value of this variable. And you can add more bars on top of that.

# In this exercise, you will have access to a DataFrame called medals that contains an index that holds the names of different countries, and three columns: "Gold", "Silver" and "Bronze". You will also have a Figure, fig, and Axes, ax, that you can add data to.

# You will create a stacked bar chart that shows the number of gold, silver, and bronze medals won by each country, and you will add labels and create a legend that indicates which bars represent which medals.

#
# Instructions
#

# Call the ax.bar method to add the "Gold" medals. Call it with the label set to "Gold".
ax.bar(medals.index, medals["Gold"], label="Gold")
# Call the ax.bar method to stack "Silver" bars on top of that, using the bottom key-word argument so the bottom of the bars will be on top of the gold medal bars, and label to add the label "Silver".
ax.bar(medals.index,  medals["Silver"], bottom=medals["Gold"], label="Silver")
ax.bar(medals.index,  medals["Bronze"],
       bottom=medals["Silver"] + medals["Gold"], label="Bronze")
# Use ax.bar to add "Bronze" bars on top of that, using the bottom key-word and label it as "Bronze".
ax.bar(medals.index,  medals["Bronze"],
       bottom=medals["Silver"] + medals["Gold"], label="Bronze")
# Display the legend
ax.legend()

plt.show()
