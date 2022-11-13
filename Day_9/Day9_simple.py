# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again.", 
#     }
# # Dictionary = {Key : Value}
# print(programming_dictionary["Bug"])
# programming_dictionary["Loop"] ="The action of doing something over and over again"
# #add new item
# # empty_dictionary = {}

# programming_dictionary["Bug"] = "A moth in your computer"
# #edit dictionary

# for key in programming_dictionary:
#     print(key) #print key
#     print(programming_dictionary[key]) #print Value
# #loop dictionary
#     #dictionary

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# student_grades = {}

# for len_score in student_scores:
#     if student_scores[len_score] >= 91:
#         student_grades[len_score] = "Outstanding"
#     elif student_scores[len_score] >= 81:
#         student_grades[len_score] = "Exceeds Expections"
#     elif student_scores[len_score] >= 71:
#         student_grades[len_score] = "Acceptable"
#     else:
#         student_grades[len_score] = "Fail"

# print(student_grades)

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# travel_log = {
#     "japan": {"city_visited": ["Osaka", "Tokyo", "Kyoto"], "total_visits": 3} ,
#     "Taiwan":{"city_visited": ["Taipai"], "total_visits": 1} ,
# }
# #nesting dictionary
# print(travel_log)

# travel_log = [
#     {
#         "country": "japan", 
#         "city_visited": ["Osaka", "Tokyo", "Kyoto"], 
#         "total_visits": 3
#         },
#     {
#         "country": "Taiwan", 
#         "city_visited": ["Taipai"], 
#         "total_visits": 1
#         },
# ]

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]

# def add_new_country(country, visit, list):
#     new_country = {}
#     new_country["country"] = country
#     new_country["visits"] = visit
#     new_country["cities"] = list
#     travel_log.append(new_country)

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
import os
import art
os.system('clear')
print(art.logo)
print("Welcome to the secret auction program")
loop_bool = True
auction = {}
while loop_bool:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?:  $"))
    auction[name] = bid
    loop = input("Are there any other bidders? Type 'yes' or 'no': ")
    if loop == "yes":
        loop_bool = True
        os.system('clear')
    else:
        loop_bool = False

number = 0

for num in auction:
    if auction[num] > number:
        number = auction[num]
        winner = num
print(f"winner is {winner}")