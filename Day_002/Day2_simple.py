print("Hello"[4])
# print
print("123" + "456")
print(123 + 456)
# differnce Data Type
num_char = len(input("What is your name?"))
print(type(num_char))
# print data type
a = float(123)
print(type(a))
print(a + 100)
# print float sum
print(str(a) + str(100))
# print string sum

two = input("input 2 integer")
print(int(two[0]) + int(two[1]))
# input two integer number to output sum each element

print(2 ** 10)
# print 2^10
# priorty is
# ()
# **
# * /
# + -

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
result = float(weight) / (float(height)) ** 2
print(int(result))
# print bmi
# to casting string to float
# to casting floatt to int
print(round(8 / 3))  # round div
print(round(2.66666, 2))  # round to 2
print(8//3)  # float to int

# f-string
# no need to parse differnt data type
score = 0
height = 1.8
isWinning = True
print(
    f"your score is {score}, your height is {height}, you are winning is {isWinning}")

age = input("what is your current age? ")
month_90 = 90 * 12
week_90 = 90 * 52
day_90 = 90 * 365
month = int(age) * 12
week = int(age) * 52
day = int(age) * 365
print(
    f"You have {day_90 - day} days, {week_90 - week} weeks and {month_90 - month} months left")
# life time remid
print("Welcome to the tip calculrator")
bill = input("What was the total bill? $")
tip_percent = input(
    "What percentage tip would you like to give? 10, 12, or 15? ")
person = input("How many people to split the bill? ")
tip = (float(bill) * (int(tip_percent)/100) + float(bill)) / int(person)
tip = round(tip, 2)
tip = "{:.2f}".format(tip)  # print  .xx float 2 demicimal point
print(f"Each person should pay: {tip}")
