# with open("Day_025/weather_data.csv") as dataread:
#     data = dataread.readlines()

# import csv

# with open("Day_025/weather_data.csv") as dataread:
#     data = csv.reader(dataread)
#     tempertures = []
#     for row in data:
#         if row[1] != 'temp':
#             tempertures.append(int(row[1]))

#     print(tempertures)

import pandas  # use pandas lib
data = pandas.read_csv("Day_025/weather_data.csv")

data_dic = data.to_dict()
print(data_dic)

temp = data["temp"].to_list()

# temp_sum = sum(temp) / len(temp)
temp_sum = data["temp"].mean()
temp_sum = round(temp_sum)

temp_max = data["temp"].max()

# print(data[data.temp == temp_max])
print(data["temp"].max())

monday = data[data.day == "Monday"]

monday_temp_F = int(monday.temp) * 1.8 + 32
print(monday_temp_F)

data_dict = {
    "studemts": ["amy", "james"],  # how to make pandas dataframe
    "scores": [76, 56]
}
dataTemp = pandas.DataFrame(data_dict)
dataTemp.to_csv("Day_025/Data.csv")  # can make csv

data = pandas.read_csv(
    "Day_025/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_color = len(data[data["Primary Fur Color"] == "Gray"])
red_color = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color = len(data[data["Primary Fur Color"] == "Black"])

squirrel_data_dic = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_color, red_color, black_color]
}
squirrel_data_convert = pandas.DataFrame(squirrel_data_dic)
squirrel_data_convert.to_csv("Day_025/squirrel_count.csv")
