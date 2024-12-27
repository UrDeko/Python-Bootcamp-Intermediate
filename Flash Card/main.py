from tkinter import *
import os
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT = "Python Bootcamp/Intermediate/Flash Card/images/card_front.png"
CARD_BACK = "Python Bootcamp/Intermediate/Flash Card/images/card_back.png"
BUTTON_RED = "Python Bootcamp/Intermediate/Flash Card/images/wrong.png"
BUTTON_GREEN = "Python Bootcamp/Intermediate/Flash Card/images/right.png"
FONT_LANGUAGE = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")
DATA_FILE = "Python Bootcamp/Intermediate/Flash Card/data/french_words.csv"
WORDS_TO_LEARN_FILE = "Python Bootcamp/Intermediate/Flash Card/data/words_to_learn.csv"

# ---------------------------- DATA ------------------------------- #

if os.path.exists(WORDS_TO_LEARN_FILE) and not os.stat(WORDS_TO_LEARN_FILE).st_size == 0:
    data = pandas.read_csv(WORDS_TO_LEARN_FILE).to_dict(orient="records")
else:
    data = pandas.read_csv(DATA_FILE).to_dict(orient="records")
card_data = {}

# ---------------------------- ACTIONS ------------------------------- #

def next_card():
    global card_data, flip, data
    window.after_cancel(flip)
    try:
        card_data = random.choice(data)
    except IndexError:
        data = pandas.read_csv(DATA_FILE).to_dict(orient="records")

    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(card_language, text="French")
    canvas.itemconfig(card_word, text=card_data["French"])
    flip = window.after(3000, flip_card)

def flip_card():
    global card_data
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_language, text="English")
    canvas.itemconfig(card_word, text=card_data["English"])

def save_word():
    global card_data
    data.remove(card_data)
    pandas.DataFrame(data).to_csv(WORDS_TO_LEARN_FILE, index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.geometry("+%d+%d" % (600, 150))

card_front = PhotoImage(file=CARD_FRONT)
card_back = PhotoImage(file=CARD_BACK)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)
card_image = canvas.create_image(400, 263, image=card_front)
card_language = canvas.create_text(400, 150, text="Language", font=FONT_LANGUAGE)
card_word = canvas.create_text(400, 263, text="Word", font=FONT_WORD)

image_wrong = PhotoImage(file=BUTTON_RED)
btn_red = Button(image=image_wrong, highlightbackground=BACKGROUND_COLOR, command=next_card)
btn_red.grid(row=1, column=0)

image_right = PhotoImage(file=BUTTON_GREEN)
btn_green = Button(image=image_right, highlightbackground=BACKGROUND_COLOR, command=save_word)
btn_green.grid(row=1, column=1)

flip = window.after(3000, flip_card)
next_card()

window.mainloop()