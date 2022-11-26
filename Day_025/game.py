import pandas
import turtle
TOTAL_COUNT = 50
screen = turtle.Screen()
screen.title("U.S States Game")
image = "Day_025/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data_read = pandas.read_csv("Day_025/50_states.csv")
data_read_States = data_read["state"].to_list()
guessed_state = []
answer_state = screen.textinput(
    title="Guess the State", prompt="What's another state's name?").capitalize()
while len(guessed_state) <= TOTAL_COUNT:

    if answer_state == "Exit":
        save_list = []
        for list in data_read_States:
            if list not in guessed_state:
                save_list.append(list)

        dict_save = {
            "States": save_list
        }
        save = pandas.DataFrame(dict_save)
        save.to_csv("Day_025/states_to_learn.csv")
        break

    if answer_state in data_read_States:
        guessed_state.append(answer_state)
        xcor = int(data_read[data_read.state == answer_state].x)
        ycor = int(data_read[data_read.state == answer_state].y)
        answer_turtle = turtle.Turtle(visible=False)
        answer_turtle.penup()
        answer_turtle.goto(xcor, ycor)
        answer_turtle.write(answer_state)

    if len(guessed_state) < TOTAL_COUNT:
        answer_state = screen.textinput(
            title=f"{len(guessed_state)}/{TOTAL_COUNT} States Correct", prompt="What's another state's name?").capitalize()
