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





 
</details>
