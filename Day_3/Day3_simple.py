water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue")
# if else in python

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("enter your age"))
    if age < 12:
        print("Child tickets 5$")
        bill = 5
    elif age <= 18:
        print("Youth tickets 7$")
        bill = 7
    elif 45 <= age and age <= 55:
        bill = 0
        print("Everything is going to be ok. Have a free ride on us!")
        print("Adult tickets 12$")
        bill = 12
    photo = input("Do you want a photo taken? Y or N ")

    if photo == "Y":
        bill += 3
    print(f"YOur final bill is {bill}$")
else:
    print("Sorry, you have to grow taller before you can ride.")

number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI = round(weight / height**2)
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are slightly under weight")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you are slightly normal weight")

elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly over weight")

elif BMI < 35:
    print(f"Your BMI is {BMI}, you are slightly obese")

else:
    print(f"Your BMI is {BMI}, you are slightly clinically obese")
# BMI code with if

year = int(input("Which year do you want to check? "))
if (year % 4 == 0):
    if (year % 100 != 0):
        print("Leap year")
    elif (year % 400 == 0):
        print("Leap year")
    else:
        print("Not leap year.")
else:
    print("not leap year")
# if elif else

print("Welcome to Pyhton Pizza Deliveries!")
size = input("What size pizza do you want? S,M,L ")
add_pepperoni = input("Do you want pepperoni? Y, N ")
extra_cheese = input("Do you want to extea cheese? Y, N ")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}")
# use multiple if then print

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name = name1 + name2
name.lower()  # change letter big to small
cal1 = name.count("t") + name.count("r") + \
    name.count("u") + name.count("e")
cal2 = name.count("l") + name.count("o") + \
    name.count("v") + name.count("e")
cal = cal1*10 + cal2
print(cal)
if (10 > cal or 90 < cal):
    print(f"Your score is {cal}, you go together like coke and mentos.")
if (40 < cal and 50 > cal):
    print(f"Your score is {cal}, you are alright together.")
else:
    print(f"Your score is {cal}.")
# lower and count func

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island \n Your mission is to find the treasure.")
le_ri = input('you\'re at a crossroad. "left" or "right"? ').lower()
if le_ri == "left":
    sw_wa = input('you\'ve come to lake. "swim" or "wait" ').lower()
    if sw_wa == "wait":
        door = input("there are yellow, blue, red doors. Which door?").lower()
        if door == "yellow":
            print("find treasure! You Win!")
        elif door == "red":
            print("full of fire. Game Over")
        elif door == "blue":
            print("room of beasts. Game Over")
        else:
            print("Game Over.")

    else:
        print("You got attacked by trout. Game Over.")

else:
    print("You fell into a hole. Game Over.")
# simple text game
