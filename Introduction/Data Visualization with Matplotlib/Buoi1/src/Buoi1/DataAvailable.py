# tạo biểu đồ có dữ liệu từ file *.csv.

#
# Step1: nạp thư viện.
#
import matplotlib.pyplot as  plt
import pandas as pd  # <- pip install pandas
import os # <- input/output 

# Get frame chart
fig, ax = plt.subplots()

# 
# Step2: thêm số liệu vào farme
#

# ax.plot (param)
# ax.plot (x,y,label="",marker="0",linestyle="",color="")
# => plot(x, y)        # plot x and y using default line style and color
# => plot(x, y, 'bo')  # plot x and y using blue circle markers
# => plot(y)           # plot y using x as index array 0..N-1
# => plot(y, 'r+')     # ditto, but with red plusses

# Get data từ file *.csv (đọc từ file)
seattle_weather = "Input_Your_flie_location"
austin_weather = pd.read_csv("Buoi1/Data/kaggle/input/austin_weather.csv")

# từ file *.csv:
# austin_weather["MONTH"] >>> lấy dữ liệu từ cột MONTH từ file *.csv
# austin_weather["MLY-PRCP-NORMAL"] >>> lấy dữ liệu từ cột MLY-PRCP-NORMAL từ file *.csv
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

#từ nhập liệu
# Get data (tự nhập)
seattle_weather_X = [32, 43, 5, 4, 66, 35]
seattle_weather_Y = [48, 23, 45, 24, 62, 46]

# Get data -> farme (bỏ # để chạy)
#ax.plot(seattle_weather_X, seattle_weather_Y)


# hiển thị  chart:
plt.show()
