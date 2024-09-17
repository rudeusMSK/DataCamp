# Datacamp (video nào nặng quá up lên ziu túp)
---
# Chuyên mục: Day By Day của (T-ara) ! [Link](https://youtu.be/-4MlN-imvck?si=fOEZqhy8dE_b1InV) :3
 <p align="center"><img src="https://github.com/user-attachments/assets/b02cb997-a99c-439f-bd95-6eead1b92bed" width="100"/></p>
<details lose="" align="left">
  <summary>  
  - Day1:
  </summary>
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

<details open="" align="left">
  <summary>  
  - Day2:
  </summary>
  <br>
<p align="center"> CHAPTER 2 </p>
  
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
</details>

</details>
