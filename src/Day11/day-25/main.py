import termcolor
import pandas

print(termcolor.colored("Reading CSV!", "blue"))
# data = pandas.read_csv("weather_data.csv")

# temp_list = data["temp"].to_list()
# average_temp = sum(temp_list) / len(temp_list)

# average_temp = data["temp"].mean()
# print(average_temp)

# max_temp = data["temp"].max()
# print(data[data.day == "Monday"])
# print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
count_data = data["Primary Fur Color"].value_counts()
black_squirrels_count = count_data["Black"]
red_squirrels_count = count_data["Cinnamon"]
gray_squirrels_count = count_data["Gray"]
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
