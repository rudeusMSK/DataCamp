# Datacamp (video nào nặng quá up lên ziu túp)
---
# Chuyên mục: Day By Day của (T-ara) ! [Link](https://youtu.be/-4MlN-imvck?si=fOEZqhy8dE_b1InV) :3
 <p align="center"><img src="https://github.com/user-attachments/assets/b02cb997-a99c-439f-bd95-6eead1b92bed" width="100"/></p>
<details lose="" align="left">
  <summary>  
  - Day1:
  </summary>
  <p align="center"> CHAPTER 1 </p> 
 <br>
1. biểu đồ ko có data: -⁠ ฅ^•ﻌ•^ฅ
<p align="center">
  <img src="https://github.com/user-attachments/assets/78741f2f-4cc3-47c1-b816-a63e964de7c2" width="600"/>
</p>

2. biểu đồ có data: -⁠ ＜(´⌯  ̫⌯`)＞ฅ

<p align="center">
  <img src="https://github.com/user-attachments/assets/d6803777-9c01-41f9-98f8-cba1857fa1be" width="600"/>
</p>
thành wả -⁠ ＜(´⌯  ̫⌯`)＞:
<p align="center">
  <img src="https://github.com/user-attachments/assets/c70e5abf-da77-4189-88c1-15f73a83bea7" width="600"/>
</p>
3. làm màu đủ thứ !  (-⁠﹏⁠-)
<p align="center">
  <img src="https://github.com/user-attachments/assets/097a0094-6294-4b4c-9eeb-bb72cc16a30c" width="600"/>
</p>
</details>

<details lose="" align="left">
  <summary>  
  - Day2:
  </summary>
  <br>
<p align="center"> CHAPTER 2 </p>
<p align="center"> Plotting time-series data </p>
<details lose="" align="left">
  <summary>  
   # Exercise 1:
  </summary>
<h1> Read data with a time index </h1>  
pandas DataFrame objects can have an index denoting time, this recognized by Matplotlib for axis labeling.

This exercise involves reading data `from climate_change.csv`, containing CO2 levels and temperatures recorded on the 6th of each month from 1958 to 2016, using pandas' `read_csv` function. The `parse_dates` and `index_col` arguments help set a `DateTimeIndex`.

Don't forget to check out the [Matplotlib](https://res.cloudinary.com/dyd911kmh/image/upload/v1676360378/Marketing/Blog/Matplotlib_Cheat_Sheet.pdf) Cheat Sheet for a quick overview of essential concepts and methods.
<h1> Instructions </h1> 

Import the pandas library as `pd` .

. Read in the data from a CSV file called `'climate_change.csv'` using `pd.read_csv`.

. Use the `parse_dates` key-word argument to parse the `"date"` column as dates.

. Use the `index_col` key-word argument to set the `"date"` column as the index.

code:
```python
# Import pandas as pd
import pandas as pd

# Read the data from file using read_csv
climate_change = pd.read_csv('climate_change.csv', parse_dates=["date"], index_col="date")
```
</details>

<details lose="" align="left">
  <summary>  
   # Exercise 2:
  </summary>
<h1> Plot time-series data </h1>  
  
To plot time-series data, we use the `Axes` object `plot` command. The first argument to this method are the values for the x-axis and the second argument are the values for the y-axis.

This exercise provides data stored in a DataFrame called `climate_change`. This variable has a time-index with the dates of measurements and two data columns: `"co2"` and `"relative_temp"`.

In this case, the index of the DataFrame would be used as the x-axis values and we will plot the values stored in the `"relative_temp"` column as the y-axis values. We will also properly label the x-axis and y-axis.
<h1> Instructions </h1> 

Import the pandas library as `pd` .
  
  . Add the data from `climate_change` to the plot: use the DataFrame `index` for the x value and the `"relative_temp"` column for the y values.
  
  . Set the x-axis label to `'Time'`.
  
  . Set the y-axis label to `'Relative temperature (Celsius)'`.
  
  . Show the figure.
code:
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Add the time-series for "relative_temp" to the plot
ax.plot(climate_change.index, climate_change['relative_temp'])

# Set the x-axis label
ax.set_xlabel('Time')

# Set the y-axis label
ax.set_ylabel('Relative temperature (Celsius)')

# Show the figure
plt.show()
```
Output:
<p align="center">
  <img src="https://github.com/user-attachments/assets/10ec765e-3616-4848-b833-8f5728f3b218" width="600"/>
</p>

</details>

<details lose="" align="left">
  <summary>  
   # Exercise 3:
  </summary>
<h1> Using a time index to zoom in </h1>  
  
When a time-series is represented with a time index, we can use this index for the x-axis when plotting. We can also select a range of dates to zoom in on a particular period within the time-series using pandas' indexing facilities. In this exercise, you will select a portion of a time-series dataset and you will plot that period.

The data to use is stored in a DataFrame called `climate_change`, which has a time-index with dates of measurements and two data columns: `"co2"` and `"relative_temp"`.
<h1> Instructions </h1> 

Import the pandas library as `pd` .
  
. Use `plt.subplots` to create a Figure with one Axes called `fig` and `ax`, respectively.

. Create a variable called `seventies` that includes all the data between `"1970-01-01"` and `"1979-12-31"`.

. Add the data from `seventies` to the plot: use the DataFrame `index` for the x value and the `"co2"` column for the y values.

code:
```python
import matplotlib.pyplot as plt

# Use plt.subplots to create fig and ax
fig, ax = plt.subplots()

# Create variable seventies with data from "1970-01-01" to "1979-12-31"
seventies = climate_change["1970-01-01":"1979-12-31"]

# Add the time-series for "co2" data from seventies to the plot
ax.plot(seventies.index, seventies["co2"])

# Show the figure
plt.show()
```
Output:
<p align="center">
  <img src="https://github.com/user-attachments/assets/0f72fbdd-855e-4d86-a6dc-ae1032b97590" width="600"/>
</p>

</details>


<p align="center"> Plotting time-series with different variables </p>


<details lose="" align="left">
  <summary>  
   # Exercise 1:
  </summary>
 
<h1> Plotting two variables </h1>  
 
If you want to plot two time-series variables that were recorded at the same times, you can add both of them to the same subplot.

If the variables have very different scales, you'll want to make sure that you plot them in different twin Axes objects. These objects can share one axis (for example, the time, or x-axis) while not sharing the other (the y-axis).

To create a twin Axes object that shares the x-axis, we use the twinx method.

In this exercise, you'll have access to a DataFrame that has the climate_change data loaded into it. This DataFrame was loaded with the "date" column set as a DateTimeIndex, and it has a column called "co2" with carbon dioxide measurements and a column called "relative_temp" with temperature measurements.

<h1> Instructions </h1> 

. Use plt.subplots to create a Figure and Axes objects called fig and ax, respectively.

. Plot the carbon dioxide variable in blue using the Axes plot method.

. Use the Axes twinx method to create a twin Axes that shares the x-axis.

. Plot the relative temperature variable in red on the twin Axes using its plot method.
code:
```python
import matplotlib.pyplot as plt

# Initalize a Figure and Axes
fig, ax = plt.subplots()

# Plot the CO2 variable in blue
ax.plot(climate_change.index, climate_change["co2"], color='blue')

# Create a twin Axes that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature in red
ax2.plot(climate_change.index, climate_change["relative_temp"], color='red')

plt.show()
```
Output:
<p align="center">
  <img src="https://github.com/user-attachments/assets/03be6a42-2dcc-4e65-9603-0ff5e1e13b60" width="600"/>
</p>
</details>

<details lose="" align="left">
  <summary>  
   # Exercise 2:
  </summary>
<h1> Defining a function that plots time-series data </h1>  

Once you realize that a particular section of code that you have written is useful, it is a good idea to define a function that saves that section of code for you, rather than copying it to other parts of your program where you would like to use this code.

Here, we will define a function that takes inputs such as a time variable and some other variable and plots them as x and y inputs. Then, it sets the labels on the x- and y-axis and sets the colors of the y-axis label, the y-axis ticks and the tick labels.

<h1> Instructions </h1> 

. Define a function called plot_timeseries that takes as input an Axes object (axes), data (x,y), a string with the name of a color and strings for x- and y-axis labels.

. Plot y as a function of in the color provided as the input color.

. Set the x- and y-axis labels using the provided input xlabel and ylabel, setting the y-axis label color using color.

. Set the y-axis tick parameters using the tick_params method of the Axes object, setting the colors key-word to color.

code:
```python
# Define a function called plot_timeseries
def plot_timeseries(axes, x, y, color, xlabel, ylabel):

  # Plot the inputs x,y in the provided color
  axes.plot(x, y, color=color)

  # Set the x-axis label
  axes.set_xlabel(xlabel)

  # Set the y-axis label
  axes.set_ylabel(ylabel, color=color)

  # Set the colors tick params for y-axis
  axes.tick_params('y', colors=color)
```

</details>

<details lose="" align="left">
  <summary>  
   # Exercise 3:
  </summary>
<h1> Using a plotting function </h1>  

Defining functions allows us to reuse the same code without having to repeat all of it. Programmers sometimes say "Don't repeat yourself".

In the previous exercise, you defined a function called plot_timeseries:

```python
plot_timeseries(axes, x, y, color, xlabel, ylabel)
```

that takes an Axes object (as the argument axes), time-series data (as x and y arguments) the name of a color (as a string, provided as the color argument) and x-axis and y-axis labels (as xlabel and ylabel arguments). In this exercise, the function plot_timeseries is already defined and provided to you.

Use this function to plot the climate_change time-series data, provided as a pandas DataFrame object that has a DateTimeIndex with the dates of the measurements and co2 and relative_temp columns.

<h1> Instructions </h1> 

. In the provided ax object, use the function plot_timeseries to plot the "co2" column in blue, with the x-axis label "Time (years)" and y-axis label "CO2 levels".

. Use the ax.twinx method to add an Axes object to the figure that shares the x-axis with ax.

. Use the function plot_timeseries to add the data in the "relative_temp" column in red to the twin Axes object, with the x-axis label "Time (years)" and y-axis label "Relative temperature (Celsius)".

code:
```python
fig, ax = plt.subplots()

# Plot the CO2 levels time-series in blue
plot_timeseries(ax, climate_change.index, climate_change["co2"], "blue", "Time (years)", "CO2 levels")

# Create a twin Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_timeseries(ax2, climate_change.index, climate_change["relative_temp"], "red", "Time (years)", "Relative temperature (Celsius)")

plt.show()
```

Output:
<p align="center">
  <img src="https://github.com/user-attachments/assets/20a8a10e-5963-44b8-ac47-253b85b6dd6b" width="600"/>
</p>
</details>

<p align="center"> Annotating time-series data </p>


<details lose="" align="left">
  <summary>  
   # Exercise 1:
  </summary>
 
<h1> Annotating a plot of time-series data </h1>  

 Annotating a plot allows us to highlight interesting information in the plot. For example, in describing the climate change dataset, we might want to point to the date at which the relative temperature first exceeded 1 degree Celsius.

For this, we will use the annotate method of the Axes object. In this exercise, you will have the DataFrame called climate_change loaded into memory. Using the Axes methods, plot only the relative temperature column as a function of dates, and annotate the data.

<h1> Instructions </h1> 

. Use the `ax.plot` method to plot the DataFrame index against the `relative_temp` column.

. Use the `annotate` method to add the text `'>1 degree'` in the location `(pd.Timestamp('2015-10-06'), 1)`.

code:
```python
fig, ax = plt.subplots()

# Plot the relative temperature data
ax.plot(climate_change.index, climate_change["relative_temp"])

# Annotate the date at which temperatures exceeded 1 degree
ax.annotate('>1 degree', xy= (pd.Timestamp('2015-10-06'), 1))

plt.show()
```

Output:
<p align="center">
  <img src="https://github.com/user-attachments/assets/8809a64f-8ade-40c9-a1ed-156919703a1f" width="600"/>
</p>

</details>

<details lose="" align="left">
  <summary>  
   # Exercise 2:
  </summary>
 
<h1> Plotting time-series: putting it all together </h1>  

 In this exercise, you will plot two time-series with different scales on the same Axes, and annotate the data from one of these series.

The CO2/temperatures data is provided as a DataFrame called climate_change. You should also use the function that we have defined before, called plot_timeseries, which takes an Axes object (as the axes argument) plots a time-series (provided as x and y arguments), sets the labels for the x-axis and y-axis and sets the color for the data, and for the y tick/axis labels:

```python
plot_timeseries(axes, x, y, color, xlabel, ylabel)
```
Then, you will annotate with text an important time-point in the data: on 2015-10-06, when the temperature first rose to above 1 degree over the average.

<h1> Instructions </h1> 

. Use the plot_timeseries function to plot CO2 levels against time. Set xlabel to "Time (years)" ylabel to "CO2 levels" and color to 'blue'.

. Create ax2, as a twin of the first Axes.

. In ax2, plot temperature against time, setting the color ylabel to "Relative temp (Celsius)" and color to 'red'.

. Annotate the data using the ax2.annotate method. Place the text ">1 degree" in x=pd.Timestamp('2008-10-06'), y=-0.2 pointing with a gray thin arrow to x=pd.Timestamp('2015-10-06'), y = 1.

code:
```python
fig, ax = plt.subplots()

# Plot the CO2 levels time-series in blue
plot_timeseries(ax, climate_change.index, climate_change["co2"], 'blue', "Time (years)", "CO2 levels")

# Create an Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_timeseries(ax2, climate_change.index, climate_change["relative_temp"], 'red', "Time (years)", "Relative temp (Celsius)")

# Annotate point with relative temperature >1 degree
ax2.annotate(">1 degree", xy=(pd.Timestamp('2015-10-06'),1), xytext=(pd.Timestamp('2008-10-06'),-0.2), arrowprops={'arrowstyle':'->', 'color':'gray'})

plt.show()
```

Output:
<p align="center">
  <img src="https://github.com/user-attachments/assets/6236a17d-504e-41c1-a80d-c8c647178be7" width="600"/>
</p>

</details>

</details>



<details open="" align="left">
  <summary>  
  - Day3:
  </summary>
  <br>
<p align="center"> CHAPTER 3 </p>


<p align="center"> Quantitative comparisons: bar-charts </p>
 <details lose="" align="left">
  <summary>  
   # Exercise 1:
  </summary>
<h1> Bar chart </h1>  

Bar charts visualize data that is organized according to categories as a series of bars, where the height of each bar represents the values of the data in this category.

For example, in this exercise, you will visualize the number of gold medals won by each country in the provided medals DataFrame. The DataFrame contains the countries as the index, and a column called "Gold" that contains the number of gold medals won by each country, according to their rows.

<h1> Instructions </h1> 

. Call the ax.bar method to plot the "Gold" column as a function of the country.

. Use the ax.set_xticklabels to set the x-axis tick labels to be the country names.

. In the call to ax.set_xticklabels rotate the x-axis tick labels by 90 degrees by using the rotation key-word argument.

. Set the y-axis label to "Number of medals".

code:
```python
fig, ax = plt.subplots()

# Plot a bar-chart of gold medals as a function of country
ax.bar(medals.index, medals["Gold"])

# Set the x-axis tick labels to the country names
ax.set_xticklabels(medals.index, rotation=90)

# Set the y-axis label
ax.set_ylabel("Number of medals")

plt.show()
```

Output:
<p align="center">
  <img src="https://github.com/user-attachments/assets/aed18191-473c-4884-86d0-0af92edd4621" width="600"/>
</p>

</details>


 <details lose="" align="left">
  <summary>  
   # Exercise 2:
  </summary>
<h1> Stacked bar chart </h1>  
A stacked bar chart contains bars, where the height of each bar represents values. In addition, stacked on top of the first variable may be another variable. The additional height of this bar represents the value of this variable. And you can add more bars on top of that.

In this exercise, you will have access to a DataFrame called medals that contains an index that holds the names of different countries, and three columns: "Gold", "Silver" and "Bronze". You will also have a Figure, fig, and Axes, ax, that you can add data to.

You will create a stacked bar chart that shows the number of gold, silver, and bronze medals won by each country, and you will add labels and create a legend that indicates which bars represent which medals.

<h1> Instructions </h1> 

. Call the ax.bar method to add the "Gold" medals. Call it with the label set to "Gold".

. Call the ax.bar method to stack "Silver" bars on top of that, using the bottom key-word argument so the bottom of the bars will be on top of the gold medal bars, and label to add the label "Silver".

. Use ax.bar to add "Bronze" bars on top of that, using the bottom key-word and label it as "Bronze".

code:
```python
# Add bars for "Gold" with the label "Gold"
ax.bar(medals.index, medals["Gold"], label="Gold")

# Stack bars for "Silver" on top with label "Silver"
ax.bar(medals.index,  medals["Silver"], bottom=medals["Gold"], label="Silver")

# Stack bars for "Bronze" on top of that with label "Bronze"
ax.bar(medals.index,  medals["Bronze"], bottom=medals["Silver"] + medals["Gold"], label="Bronze")

# Display the legend
ax.legend()

plt.show()
```

Output:
<p align="center">

  <img src="https://github.com/user-attachments/assets/d046ef27-ab86-4c5f-9691-4113a77e8843" width="600"/>
</p>

</details>


 
<p align="center"> Quantitative comparisons: histograms </p>
 <details lose="" align="left">
  <summary>  
   # Exercise 1:
  </summary>
<h1> Creating histograms </h1>  
Histograms show the full distribution of a variable. In this exercise, we will display the distribution of weights of medalists in gymnastics and in rowing in the 2016 Olympic games for a comparison between them.

You will have two DataFrames to use. The first is called mens_rowing and includes information about the medalists in the men's rowing events. The other is called mens_gymnastics and includes information about medalists in all of the Gymnastics events.
<h1> Instructions </h1> 

. Use the ax.hist method to add a histogram of the "Weight" column from the mens_rowing DataFrame.

. Use ax.hist to add a histogram of "Weight" for the mens_gymnastics DataFrame.

. Set the x-axis label to "Weight (kg)" and the y-axis label to "# of observations".

code:
```python
fig, ax = plt.subplots()
# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing["Weight"])

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics["Weight"])

# Set the x-axis label to "Weight (kg)"
ax.set_xlabel("Weight (kg)")

# Set the y-axis label to "# of observations"
ax.set_ylabel("# of observations")

plt.show()
```

Output:
<p align="center">
  <img src="https://github.com/user-attachments/assets/20211801-0ef0-46ec-9968-034574ee57d9" width="600"/>
</p>

</details>




 <details lose="" align="left">
  <summary>  
   # Exercise 2:
  </summary>
<h1> "Step" histogram </h1>  

Histograms allow us to see the distributions of the data in different groups in our data. In this exercise, you will select groups from the Summer 2016 Olympic Games medalist dataset to compare the height of medalist athletes in two different sports.

The data is stored in a pandas DataFrame object called summer_2016_medals that has a column "Height". In addition, you are provided a pandas GroupBy object that has been grouped by the sport.

In this exercise, you will visualize and label the histograms of two sports: "Gymnastics" and "Rowing" and see the marked difference between medalists in these two sports.

<h1> Instructions </h1> 

. Use the hist method to display a histogram of the "Weight" column from the mens_rowing DataFrame, label this as "Rowing".

. Use hist to display a histogram of the "Weight" column from the mens_gymnastics DataFrame, and label this as "Gymnastics".

. For both histograms, use the histtype argument to visualize the data using the 'step' type and set the number of bins to use to 5.

. Add a legend to the figure, before it is displayed.

code:
```python
fig, ax = plt.subplots()

# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing["Weight"], label ='Rowing', histtype='step',bins=5)

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics["Weight"],histtype='step', label ='Gymnastics', bins=5)

ax.set_xlabel("Weight (kg)")
ax.set_ylabel("# of observations")

# Add the legend and show the Figure
ax.legend()
plt.show()
```

Output:
<p align="center">
  <img src="https://github.com/user-attachments/assets/df5795bb-008e-4af1-8c5e-a548675d9f3b)" width="600"/>
</p>

</details>



<p align="center"> Statistical plotting </p>

 <details lose="" align="left">
  <summary>  
   # Exercise 1:
  </summary>

  <h1> Adding error-bars to a bar chart </h1>  

Statistical plotting techniques add quantitative information for comparisons into the visualization. For example, in this exercise, we will add error bars that quantify not only the difference in the means of the height of medalists in the 2016 Olympic Games, but also the standard deviation of each of these groups, as a way to assess whether the difference is substantial relative to the variability within each group.

For the purpose of this exercise, you will have two DataFrames: mens_rowing holds data about the medalists in the rowing events and mens_gymnastics will hold information about the medalists in the gymnastics events.

<h1> Instructions </h1> 

. Add a bar with size equal to the mean of the "Height" column in the mens_rowing DataFrame and an error-bar of its standard deviation.

. Add another bar for the mean of the "Height" column in mens_gymnastics with an error-bar of its standard deviation.

. Add a label to the the y-axis: "Height (cm)".

code:
```python
fig, ax = plt.subplots()

# Add a bar for the rowing "Height" column mean/std
ax.bar("Rowing", mens_rowing["Height"].mean(), yerr=mens_rowing["Height"].std())

# Add a bar for the gymnastics "Height" column mean/std
ax.bar("Gymnastics", mens_gymnastics["Height"].mean(), yerr=mens_gymnastics["Height"].std())

# Label the y-axis
ax.set_ylabel("Height (cm)")

plt.show()
```

Output:
<p align="center">
  <img src="https://github.com/user-attachments/assets/1377c9f5-5405-46eb-a8b0-979c4cc59fb5" width="600"/>
</p>

</details>


 <details lose="" align="left">
  <summary>  
   # Exercise 2:
  </summary>
<h1> Adding error-bars to a plot </h1>  
  
Adding error-bars to a plot is done by using the errorbar method of the Axes object.

Here, you have two DataFrames loaded: seattle_weather has data about the weather in Seattle and austin_weather has data about the weather in Austin. Each DataFrame has a column "MONTH" that has the names of the months, a column "MLY-TAVG-NORMAL" that has the average temperature in each month and a column "MLY-TAVG-STDDEV" that has the standard deviation of the temperatures across years.

In the exercise, you will plot the mean temperature across months and add the standard deviation at each point as y errorbars.

<h1> Instructions </h1> 

. Use the ax.errorbar method to add the Seattle data: the "MONTH" column as x values, the "MLY-TAVG-NORMAL" as y values and "MLY-TAVG-STDDEV" as yerr values.

. Add the Austin data: the "MONTH" column as x values, the "MLY-TAVG-NORMAL" as y values and "MLY-TAVG-STDDEV" as yerr values.

. Set the y-axis label as "Temperature (Fahrenheit)".

code:
```python
fig, ax = plt.subplots()

# Add Seattle temperature data in each month with error bars
ax.errorbar(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"], yerr=seattle_weather["MLY-TAVG-STDDEV"])

# Add Austin temperature data in each month with error bars
ax.errorbar(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"], yerr=austin_weather["MLY-TAVG-STDDEV"])
# Set the y-axis label
ax.set_ylabel("Temperature (Fahrenheit)")

plt.show()
```

Output:
<p align="center">
  <img src="https://github.com/user-attachments/assets/cc79ac81-5be9-46ef-8965-5830af22504e" width="600"/>
</p>

</details>


  <details lose="" align="left">
  <summary>  
   # Exercise 3:
  </summary>
<h1> Creating boxplots </h1>  

Boxplots provide additional information about the distribution of the data that they represent. They tell us what the median of the distribution is, what the inter-quartile range is and also what the expected range of approximately 99% of the data should be. Outliers beyond this range are particularly highlighted.

In this exercise, you will use the data about medalist heights that you previously visualized as histograms, and as bar charts with error bars, and you will visualize it as boxplots.

Again, you will have the mens_rowing and mens_gymnastics DataFrames available to you, and both of these DataFrames have columns called "Height" that you will compare.

<h1> Instructions </h1> 

. Create a boxplot that contains the "Height" column for mens_rowing on the left and mens_gymnastics on the right.

. Add x-axis tick labels: "Rowing" and "Gymnastics".

. Add a y-axis label: "Height (cm)".

code:
```python
fig, ax = plt.subplots()

# Add a boxplot for the "Height" column in the DataFrames
ax.boxplot([mens_rowing["Height"],mens_gymnastics["Height"]])

# Add x-axis tick labels:
ax.set_xticklabels(["Rowing","Gymnastics"])

# Add a y-axis label
ax.set_ylabel("Height (cm)")

plt.show()
```

Output:
<p align="center">
  <img src="https://github.com/user-attachments/assets/145370c9-bad3-4a74-b34a-ddac34263715" width="600"/>
</p>
</details>



<p align="center"> Quantitative comparisons: scatter plots </p>
 <details lose="" align="left">
  <summary>  
   # Exercise 1:
  </summary>
  
<h1> Simple scatter plot </h1>  

Scatter are a bi-variate visualization technique. They plot each record in the data as a point. The location of each point is determined by the value of two variables: the first variable determines the distance along the x-axis and the second variable determines the height along the y-axis.

In this exercise, you will create a scatter plot of the climate_change data. This DataFrame, which is already loaded, has a column "co2" that indicates the measurements of carbon dioxide every month and another column, "relative_temp" that indicates the temperature measured at the same time.

<h1> Instructions </h1> 

.Using the ax.scatter method, add the data to the plot: "co2" on the x-axis and "relative_temp" on the y-axis.

.Set the x-axis label to "CO2 (ppm)".

.Set the y-axis label to "Relative temperature (C)".

code:
```python
fig, ax = plt.subplots()

# Add data: "co2" on x-axis, "relative_temp" on y-axis
ax.scatter(climate_change["co2"], climate_change["relative_temp"])

# Set the x-axis label to "CO2 (ppm)"
ax.set_xlabel("CO2 (ppm)")

# Set the y-axis label to "Relative temperature (C)"
ax.set_ylabel("Relative temperature (C)")

plt.show()
```

Output:
<p align="center">
  <img src="https://github.com/user-attachments/assets/d51faf31-d463-4ba1-85c5-48fb72d7df5d" width="600"/>
</p>

</details>




<details lose="" align="left">
  <summary>  
   # Exercise 2:
  </summary>
  
<h1> Encoding time by color </h1>  

The screen only has two dimensions, but we can encode another dimension in the scatter plot using color. Here, we will visualize the climate_change dataset, plotting a scatter plot of the "co2" column, on the x-axis, against the "relative_temp" column, on the y-axis. We will encode time using the color dimension, with earlier times appearing as darker shades of blue and later times appearing as brighter shades of yellow.

<h1> Instructions </h1> 

. Using the ax.scatter method add a scatter plot of the "co2" column (x-axis) against the "relative_temp" column.

. Use the c key-word argument to pass in the index of the DataFrame as input to color each point according to its date.

. Set the x-axis label to "CO2 (ppm)" and the y-axis label to "Relative temperature (C)".

code:
```python
fig, ax = plt.subplots()

# Add data: "co2", "relative_temp" as x-y, index as color
ax.scatter(climate_change["co2"], climate_change["relative_temp"], c=climate_change.index)

# Set the x-axis label to "CO2 (ppm)"
ax.set_xlabel("CO2 (ppm)")

# Set the y-axis label to "Relative temperature (C)"
ax.set_ylabel("Relative temperature (C)")

plt.show()
```

Output:
<p align="center">
  <img src="!https://github.com/user-attachments/assets/e385f91b-f0f1-46bd-b48d-bf6655395684" width="600"/>
</p>

</details>




</details>
