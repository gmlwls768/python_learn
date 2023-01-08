from tkinter import *
from pandas import *
from random import *
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


try:
    csv_read = read_csv("Day_031/data/words_to_learn.csv")
except FileNotFoundError:
    csv_read = read_csv("Day_031/data/eng_kor.csv")
    csv_read.to_csv("Day_031/data/words_to_learn.csv", index=False)
    eng_dict = csv_read.to_dict("records")
else:
    eng_dict = csv_read.to_dict("records")


def turn_under():
    canvas.itemconfig(canvas_img, image=card_back)
    canvas.itemconfig(title, text="Korean", fill="white")
    canvas.itemconfig(word, text=current_card["Korean"], fill="white")


def quiz():
    global current_card, turn_timer
    window.after_cancel(turn_timer)
    rand = randrange(len(eng_dict))
    current_card = eng_dict[rand]
    canvas.itemconfig(canvas_img, image=card_front)

    canvas.itemconfig(title, text="English", fill="black")
    canvas.itemconfig(word, text=current_card["English"], fill="black")
    turn_timer = window.after(3000, func=turn_under)


def right_answer():
    eng_dict.remove(current_card)
    df = DataFrame(eng_dict)
    df.to_csv("Day_031/data/words_to_learn.csv", index=False)
    quiz()


# back
card_back = PhotoImage(
    file="Day_031/images/card_back.png")


canvas = Canvas(width=800, height=526,
                highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="Day_031/images/card_front.png")
canvas_img = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

# btn
right = PhotoImage(file="Day_031/images/right.png")
wrong = PhotoImage(file="Day_031/images/wrong.png")
right_button = Button(image=right, highlightthickness=0, command=right_answer)
wrong_button = Button(image=wrong, highlightthickness=0, command=quiz)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

# text
title = canvas.create_text(400, 150, fill="black", text="",
                           font=("Areil", 40, "italic"))
word = canvas.create_text(400, 263, fill="black", text="",
                          tags="text", font=("Areil", 65, "bold"))

# csv_read = read_csv("Day_031/data/eng_kor.csv")
# eng_dict = csv_read.to_dict("records")

turn_timer = window.after(3000, func=turn_under)
quiz()

window.mainloop()
