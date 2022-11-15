import os
import random
import art
enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

player_health = 2


def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
# local scope global scope


def example_increase_enemies():
    global enmines
    enemies += 1
    print(f"enemies inside function: {enemies}")
    # ==


def example_increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies+1
# how to use global scope in function

# global scope name recommended uppercase


EASY_LEVEL = 10
HARD_LEVEL = 5


def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def num_check(guess, answer, turns):
    if answer > guess:
        print("Too low.")
        return turns - 1
    elif answer < guess:
        print("Too high.")
        return turns - 1
    else:
        print(f"You got it! the answer was {answer}.")
        loop = turns
        return loop


def game():
    os.system('clear')
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    turns = difficulty()
    guess = -1
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = num_check(guess, answer, turns)
        if turns == 0:
            print("You lose ")
            return
        elif guess != answer:
            print("Guess again.")


game()
# simple game
