from turtle import Turtle, Screen
import pandas
from states import write_state, game_over, quit_game

screen = Screen()
turtle = Turtle()
screen.title("U.S. States Game")  # Setting a screen title
image = "blank_states_img.gif"
screen.addshape(image)  # Adding the shape to screen
turtle.shape(image)  # Turtle can use the shape as it is loaded.
score = 0

game_is_on = True
states_data = pandas.read_csv("50_states.csv")
states = states_data.state.tolist()
states_guessed = []

while game_is_on:
    answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")
    if answer == "Exit":
        missed_states = [state for state in states if state not in states_guessed]
        missed_state_data = pandas.DataFrame(missed_states)
        missed_state_data.to_csv("missed_states.csv")
        quit_game()
        game_is_on = False
        # missed_states_dict = {
        #     "Missed State": [],
        #     "x": [],
        #     "y": [],
        # }
        # for missed_state in missed_states:
        #     missed_state_details = states_data[states_data["state"] == missed_state]
        #     x_value = float(missed_state_details["x"])
        #     y_value = float(missed_state_details["y"])
        #     missed_states_dict["Missed State"].append(missed_state)
        #     missed_states_dict["x"].append(x_value)
        #     missed_states_dict["y"].append(y_value)
        # missed_state_data = pandas.DataFrame(missed_states_dict)
        # missed_state_data.to_csv("missed_states.csv")

    for state in states:
        if state.lower() == answer.lower():
            score += 1
            selected_state = states_data[states_data.state == state]
            xcor = float(selected_state["x"])
            ycor = float(selected_state["y"])
            write_state(xcor, ycor, state)
            states_guessed.append(state)

    if score >= 50:
        game_over()
        game_is_on = False

screen.exitonclick()
