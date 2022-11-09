import os
import random
import hangman_art
import hangman_words
word_list = hangman_words.word_list
stages = hangman_art.stages
logo = hangman_art.logo
# or from hangman_art import logo, stages
selected_word = random.choice(word_list)
os.system('clear')

print_screen = []
selected_screen = []
print(logo, "\n")

for A in range(len(selected_word)):
    print_screen += "-"

for B in range(len(selected_word)):
    selected_screen += selected_word[B]

# or use
# if " n "not in print_screen:
#   end_game = True
# while not endgame

# or life = 6 and change count to life
count = -1
while (print_screen != selected_screen) and (count > -7):
    check = 0
    print(print_screen)
    print(stages[count])
    user = input("Guess a letter: ").lower()
    os.system('clear')
    if user in print_screen:
        print(f'''You've already guessed {user}''')
    for i in range(len(selected_word)):
        if user == selected_word[i]:
            print_screen[i] = selected_word[i]
            check += 1
    # or
    # if user not in selected_word:
    #   count -= 1
    #   print(f"You guessed {user}, that's not in the word. You lose a life")
    if check == 0:
        count -= 1
        print(f"You guessed {user}, that's not in the word. You lose a life")
    if print_screen == selected_screen:
        print("You Win")
        print(stages[count])
    if count == -7:
        print("You lose.")
        print(stages[count])
        print(selected_word)
