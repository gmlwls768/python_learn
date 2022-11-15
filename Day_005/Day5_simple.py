import random
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
# loop
student_heights = input("Input a list of student heights ").split()
print(student_heights)
len_sum = 0
int_sum = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
for k in student_heights:
    len_sum += 1
for h in student_heights:
    int_sum += h

print(round(int_sum/len_sum))
# use for in with list

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# sort
for n in range(1, 11, 3):
    print(n)
total = 0
for n in range(1, 101):
    total += n
print(total)
total = 0
for n in range(2, 101, 2):
    total += n
print(total)
# add even use loop

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz ")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
# FizzBuzz game use loop

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ""
for char in range(1, nr_letters + 1):
    password += random.choice(letters)
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)
print(password)
# easy level make pw
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ""
pw = []
size = nr_letters + nr_symbols + nr_numbers
for char in range(1, nr_letters + 1):
    pw.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    pw.append(random.choice(symbols))
for char in range(1, nr_numbers + 1):
    pw.append(random.choice(numbers))
random.shuffle(pw)
for i in pw:
    password += i
print(password)
# Hard level make pw use shuffle
