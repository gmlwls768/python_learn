import os
import art
import game_data
import random

# 'name': 'Instagram',
#     'follower_count': 346,
#     'description': 'Social media platform',
#     'country': 'United States'


current_score = 0
score = True
while score:
    os.system('clear')
    print(art.logo)

    random_countA = random.randint(0, len(game_data.data) - 1)
    nameA = game_data.data[random_countA]['name']
    follower_countA = game_data.data[random_countA]['follower_count']
    descriptionA = game_data.data[random_countA]['description']
    countryA = game_data.data[random_countA]['country']
    if current_score > 0:
        print(f"You're right! Current score: {current_score}.")

    print(f"Compare A: {nameA}, {descriptionA}, from {countryA}.")

    print(art.vs)
    random_countB = random.randint(0, len(game_data.data) - 1)
    while random_countA == random_countB:
        random_countB
    nameB = game_data.data[random_countB]['name']
    follower_countB = game_data.data[random_countB]['follower_count']
    descriptionB = game_data.data[random_countB]['description']
    countryB = game_data.data[random_countB]['country']

    print(f"Against B: {nameB}, {descriptionB}, from {countryB}.")

    compare = input("Who has more followers? Type 'A' or 'B': ")

    if compare == "A":
        if follower_countA > follower_countB:
            current_score += 1
            score = True
        else:
            score = False
            os.system('clear')
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {current_score}")
    else:
        if follower_countB > follower_countA:
            current_score += 1
            score = True
        else:
            score = False
            os.system('clear')
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {current_score}")
