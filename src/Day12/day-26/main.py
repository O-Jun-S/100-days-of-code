# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
#
# name = "Angela"
# new_list = [letter for letter in name]

# new_numbers = [n * 2 for n in range(1, 5)]

# names = ["Alex", "Beth", "Caroline", "Eleanor", "Freddie"]
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)

# exercise 1
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# squared_numbers = [n * n for n in numbers]
#
# print("exercise1")
# print(squared_numbers)
#
# # exercise 2
#
# result = [n for n in numbers if n % 2 == 0]
#
# print("exercise 2")
# print(result)

# exercise 3
# with open("file1.txt") as file1:
#     file1_lines = file1.readlines()
#     file1_nums = [int(n) for n in file1_lines]
#
# with open("file2.txt") as file2:
#     file2_lines = file2.readlines()
#     file2_nums = [int(n) for n in file2_lines]
#
# common_numbers = [n for n in file1_nums if n in file2_nums]
#
# print("exercise 3")
# print(common_numbers)

# dictionary
# import random
#
# names = ["Alex", "Beth", "Caroline", "Dave" "Eleanor", "Freddie"]
# students_scores = {name: random.randint(1, 101) for name in names}
# passed_students = {name: score for (name, score) in students_scores.items() if score >= 60}
# print(passed_students)

# dictionary exercise 1
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print("exercise 1")
# print(result)

# dictionary exercise 2
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
# print("exercise 2")
# print(weather_f)

# pandas dataframe
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(row.student)
