from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    if timer_label.cget("text") == "Timer":
        reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60
        if reps % 2 == 0:
            if reps % 8 == 0:
                count_down(long_break_sec)
                timer_label.config(text="Break", fg=RED)
            else:
                count_down(short_break_sec)
                timer_label.config(text="Break", fg=RED)
        else:
            count_down(work_sec)
            timer_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    min = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"  # dynamic data type
        canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        canvas.itemconfig(timer_text, text=f"{min}:{sec}")
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        check_label.config(text="✓" * int(reps/2))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", fg=GREEN, font=(
    FONT_NAME, 50, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Day_028/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)


window.mainloop()
