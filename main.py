import turtle
import pandas as pd
from text import Text
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")


score = 0
all_states = data.state.to_list()
true_answers = []
game_on = True
while game_on:
    answer_state = screen.textinput(title=f"Guess the State {score}/50", prompt="What's the state's name").title()
    if answer_state == "Exit":
        missing_states = [item for item in all_states if item not in true_answers]
        game_on = False
    elif score < 50 and answer_state != "Exit":
        for a in range(50):
            if answer_state == data.state[a]:
                position = (data.x[a], data.y[a])
                new_turtle = Text(position)
                new_turtle.print_state(answer_state)
                score += 1
                true_answers.append(answer_state)


df = pd.DataFrame(missing_states)
df.to_csv("unknown_states.csv")
print("You may check out unknown_states.csv for remaining answers")

