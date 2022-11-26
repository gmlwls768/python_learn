# list comprehension
import pandas
import random
num = [1, 2, 3]
new_num = [n+1 for n in num]

name = "heejin"
new_name = [letter for letter in name]

new_range = [num * 2 for num in range(1, 5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

short_names = [name for name in names if len(name) <= 4]
long_names = [name.upper() for name in names if len(name) > 5]

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
new_numbers = [n**2 for n in numbers]

result = [n for n in numbers if n % 2 == 0]
# print(result)

with open("Day_026/file1.txt")as file1:
    file_1 = file1.readlines()
with open("Day_026/file2.txt")as file2:
    file_2 = file2.readlines()

compare_list = [int(n) for n in file_1 if n in file_2]

students_score = {
    "Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"

}
students_score = {student: random.randint(1, 100) for student in names}

passed_student = {
    student: score for (student, score) in students_score.items() if students_score[student] >= 60}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_result = {word: len(word) for word in sentence.split()}

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_result = {day: (tem*9/5) + 32 for (day, tem) in weather_c.items()}

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}


student_data = pandas.DataFrame(student_dict)

# for (key, value) in student_data.items():
#     print(value)

for (index, row) in student_data.iterrows():
    if row.student == "Angela":
        print(row.score)

nato = pandas.read_csv("Day_026/nato_phonetic_alphabet.csv")
nato = {row.letter: row.code for (index, row) in nato.iterrows()}

user_input = input("Enter a word: ").upper()
list = [nato[n] for n in user_input]
print(list)
