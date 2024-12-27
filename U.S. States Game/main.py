import pandas

from state import State
from turtle import Screen

DATA_FILE = "Python Bootcamp/Intermediate/U.S. States Game/50_states.csv"
SAVED_DATA_FILE = "Python Bootcamp/Intermediate/U.S. States Game/states_to_learn.csv"
IMAGE = "Python Bootcamp/Intermediate/U.S. States Game/blank_states_img.gif"

# def func(x, y):
#     tim.goto(x, y)
#     tim.write(str(x)+","+str(y))

screen = Screen()
screen.addshape(IMAGE)
screen.bgpic(IMAGE)
screen.setup(width=730, height=510)

states_data = pandas.read_csv(DATA_FILE)
all_states = states_data["state"].to_list()
guessed = set()

if screen.textinput("Guess States", "Start Game: Yes/No").title() == "Yes":
    while len(guessed) < 50:
        guess = screen.textinput(f"{len(guessed)}/{len(all_states)} States Correct", "What's another state name?")

        if guess:
            guess = guess.title()

            # print(guess)
            if guess.lower() == "exit":
                states_to_learn = set(all_states).difference(guessed)
                progress = {"state": [s for s in states_to_learn]}

                data_to_save = pandas.DataFrame(progress)
                data_to_save.to_csv(SAVED_DATA_FILE)
                break

            if guess in all_states and not guess in guessed:
                row_data = states_data[states_data["state"] == guess]
                # row_data = states_data[states_data["state"] == guess].values.flatten().tolist()
                s_name, x_pos, y_pos = row_data.iloc[0].state, row_data.iloc[0].x, row_data.iloc[0].y
                # state = State(row_data[0], (row_data[1], row_data[2]))
                state = State(s_name, (x_pos, y_pos))
                guessed.add(guess)
