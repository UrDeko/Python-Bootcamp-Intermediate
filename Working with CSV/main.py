import csv
import pandas

WEATHER_DATA = "Python Bootcamp/Intermediate/Working with CSV/weather_data.csv"
SQUIRRELS_DATA = "Python Bootcamp/Intermediate/Working with CSV/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240101.csv"

# CSV
with open(WEATHER_DATA) as f:
    data = csv.reader(f)
    temperatures = []
    for row in data:
        if not row[1].isalpha():
            temperatures.append(int(row[1]))

# Pandas
weather_data = pandas.read_csv(WEATHER_DATA)
temperatures = weather_data["temp"]
average = temperatures.mean()
max = temperatures.max()
warmest_day = weather_data[weather_data.temp == weather_data.temp.max()]
celsius_to_farenheit = lambda t: (t * 9/5) + 32
monday = weather_data[weather_data.day == "Monday"]
# print(monday.temp)
# print(celsius_to_farenheit(monday.temp[0]))

students_scores = {"Students": ["Mike", "John", "Ben"],
                   "Scores": [76, 54, 62]
                   }
students_data = pandas.DataFrame(students_scores)
# print(students_data)

students_data.to_csv("/Users/denisstratiev/Documents/Work/Python/Python Bootcamp/Intermediate/Working with CSV/students_data.csv", index=False)

# Squirrels Data
squirrels_data = pandas.read_csv(SQUIRRELS_DATA)
squirrels_count = squirrels_data.value_counts("Primary Fur Color")
# squirrels_count = squirrels_data.groupby("Primary Fur Color")["Primary Fur Color"].count()
print(squirrels_count)
# import pdb; pdb.set_trace()