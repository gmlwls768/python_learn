import art
import os
import random
############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.

# Difficulty Expert 🤯: Only use Hint 1 to complete the project.
############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

if input("Do you want to play a game of Blackjack? Type 'y' or 'n'") == "y":
    game = True


def final_hand():
    print("----------------------------------------------")
    print(f"Your final hand: {usr_card_list}, current score:{usr_card}")
    print(f"computer final hand: {com_card_list}, current score:{com_card}")


def win():
    final_hand()
    print("win")


def lose():
    final_hand()
    print("lose")


def draw():
    final_hand()
    print("draw")


def calcu(card_list):
    if 11 in usr_card_list and sum(usr_card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)


def is_card_ok():
    if usr_card > 21 and com_card > 21:
        draw()
    elif usr_card > 21 and com_card <= 21:
        lose()
    elif usr_card <= 21 and com_card > 21:
        win()
    elif usr_card <= 21 and com_card <= 21:
        if usr_card > com_card:
            win()
        elif usr_card == com_card:
            draw()
        else:
            lose()


while game:
    os.system('clear')
    print(art.logo)
    usr_card_list = []
    com_card_list = []
    for twice in range(2):
        usr_card_list.append(cards[random.randint(0, 12)])
        com_card_list.append(cards[random.randint(0, 12)])
    usr_card = calcu(usr_card_list)
    com_card = calcu(com_card_list)
    print(f"Your cards: {usr_card_list}, current score: {usr_card}")
    print(f"Computer's first card: {com_card_list[0]}")
    com_loop = True
    while com_loop:
        if com_card < 21 - 4:
            com_card_list.append(cards[random.randint(0, 12)])
            com_card = calcu(com_card_list)
        else:
            com_loop = False
    loop = True
    while loop:
        if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
            usr_card_list.append(cards[random.randint(0, 12)])
            usr_card = calcu(usr_card_list)
            if usr_card > 21:
                loop = False
                is_card_ok()
            else:
                print(f"Your cards: {usr_card_list}, current score:{usr_card}")
                print(f"Computer's first card: {com_card_list[0]}")

        else:
            loop = False
            is_card_ok()
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n'") == "y":
        game = True
    else:
        game = False
