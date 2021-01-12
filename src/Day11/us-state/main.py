import turtle
import pandas

ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
csv_file = "50_states.csv"

screen.addshape(image)
turtle.shape(image)

tom = turtle.Turtle()
tom.penup()
tom.hideturtle()

csv_data = pandas.read_csv(csv_file)
all_states = csv_data.state.to_list()

score = 0
num_states = len(csv_data)
answered_states = []

while len(answered_states) < 50:
    answer_state = screen.textinput(title=f"{score}/{num_states}Guess the State",
                                    prompt="What's another state's name?")
    answer_state_title_case = answer_state.title()
    if answer_state_title_case == "Exit":
        missing_states = [state for state in all_states if state not in answered_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    for state in all_states:
        if state == answer_state_title_case:
            if state in answered_states:
                pass
            else:
                score += 1
                state_data = csv_data[csv_data.state == state]
                x = int(state_data["x"])
                y = int(state_data["y"])
                tom.goto(x, y)
                tom.write(state, font=FONT, align=ALIGNMENT)
                answered_states.append(state)

turtle.mainloop()
