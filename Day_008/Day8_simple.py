import os
import art
import math


def greet():
    print("hi")
    print("how do you do")
    print(":D")


greet()
# no parameter func


def greet_name(name):  # parameter is send by argument
    print(f"hi {name}")
    print("how do you do")
    print("good :D")


greet_name("ocean")  # argument
# parameter func


def greet_name_location(name, location):
    print(f"Hello  {name}")
    print(f"What is it like in {location}")


greet_name_location("ocean", "korea")
greet_name_location(location="korea", name="ocean")
# multiple parameter and keyword argument


def paint_calc(height, width, cover):
    print(f"you need {math.ceil((height * width) / cover)} cans of paint")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
# use parameter func and simple cal


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if (number % i == 0):
            is_prime = False
    if is_prime:
        print("yes")
    else:
        print("not")


n = int(input("Check this number: "))
prime_checker(number=n)
# prime num check

# def encode(text, shift):
#     cipher_text = ""
#     for i in text:
#         position = alphabet.index(i)
#         new_position = position + shift
#         if new_position >= 26:
#             new_position -= 26
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"encode is {cipher_text}")


# def decode(text, shift):
#     cipher_text = ""
#     for i in text:
#         position = alphabet.index(i)
#         new_position = position - shift
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"decode is {cipher_text}")


# if direction == "encode":
#     encode(text, shift)
# elif direction == "decode":
#     decode(text, shift)


def caesar(direction, text, shift):
    cipher_text = ""
    if direction == "decode":
        shift *= -1
    for i in text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + shift
            while new_position >= 26:
                new_position -= 26
                # or use moduler new_position = new_position % 26
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += i
    print(f"{direction} is {cipher_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

os.system('clear')
print(art.logo)
loop = True
while loop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    text_list = []
    for i in range(len(text)):
        text_list.append(text[i])
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    loop = input("loop yes or no: ").lower()
    if loop == "No":
        loop = False
        print("Bye~")
# complete Caesaris code
# implemented to loop and ignore not alphabet and import logo
