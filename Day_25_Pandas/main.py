#import csv
#with open("weather_data .csv", mode='r') as data_file:
#    data = csv.reader(data_file)
#    temperature = []
#    for i in data:
#        if i[1] != "temp":
#            temperature.append(int(i[1]))
#   print(temperature)

import pandas as pd

data = pd.read_csv("weather_data .csv")
temp_list = data["temp"].to_list()
avg_temp = data["temp"].mean()              ## Returning values of a column or Series(pandas)
max_temp = data["temp"].max()
min_temp = data["temp"].min()
#print(avg_temp)
#print(max_temp)
#print(min_temp)

## Returning values of a row:

#print(data[data.temp == data.temp.max()]) # Returning the row which has maximum temp.

monday = data[data.day == "Monday"]
print((monday.temp*1.8) + 32)


