import random

import my_module
random_int = random.randint(1, 10)
# include 1 and 10
print(random_int)
print(my_module.pi)
random_float = random.random()
print(random_float)
# random float 0.0~1.0 not include 0 and 1
random_float = random.random()*5
print(random_float)
# random float 0 to 5
# module and random func
love_score = random.randint(1, 100)
print(f"your love score is {love_score}")

head_tail = random.randint(0, 1)
if head_tail == 0:
    print("Heads")
else:
    print("Tails")

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
                     "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america[-1])
states_of_america[1] = "pencilvania"
# edit
states_of_america.append("Angelaland")
# add single item
states_of_america.extend(["korea", "japan"])
# add extra list
print(states_of_america)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# split and save list
payman = random.randint(0, len(names)-1)
print(f"{names[payman]} is going to buy the meal today!")
fruits = ["Strawberries",  "Nectarines", "Apples",
          "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
# merge list
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
A = int(position[0]) - 1
B = int(position[1]) - 1
map[B][A] = "X"
print(f"{row1}\n{row2}\n{row3}")
# multiple list
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
Type = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
com = random.randint(0, 2)
command = [rock, paper, scissors]
if Type > 2:
    print("You type an invalid number, you lose!")
else:
    print(command[Type])
    print("Computer chose:")
    print(command[com])
    if Type == com:
        print("draw")
    elif Type-com == 1 or Type-com == -2:
        print("win")
    else:
        print("lose")
# simple game
