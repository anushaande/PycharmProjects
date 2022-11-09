"""-------------------------------------- Turning a file into list ------------------------------------------ :
# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
# for day in data:
#     print(day.strip()) """

""" ---------------------------- Getting hold of temperature using csv ------------------------------------- :
# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures) """

# Using pandas to deal with data.
import pandas

gray = 0
cinnamon = 0
black = 0
squirrel_dict = {}

s_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = ["Gray", "Cinnamon", "Black"]
squirrel_dict = {
    "Fur Color": [],
    "Count": [],
}

# for color in s_data["Primary Fur Color"]:
#     if color == "Gray":
#         gray += 1
#     elif color == "Cinnamon":
#         cinnamon += 1
#     elif color == "Black":
#         black += 1
# #
# # pandas.DataFrame({
# #     "Gray": gray,
# #     "Cinnamon": cinnamon,
# #     "Black": black,
# #                   })
# squirrel_dict["Fur Color"] = ["gray", "cinnamon", "black"]
# squirrel_dict["count"] = [gray, cinnamon, black]
# print(f"{squirrel_dict}")
# data = pandas.DataFrame(squirrel_dict)
# print(data)
# data.to_csv("squirrel_data.csv")

for color in colors:
    color_set = s_data[s_data["Primary Fur Color"] == color]
    print(type(color_set))
    squirrel_dict["Fur Color"].append(color)
    squirrel_dict["Count"].append(len(color_set))
squirrel_color_data = pandas.DataFrame(squirrel_dict)
squirrel_color_data.to_csv("squirrel_data.csv")
