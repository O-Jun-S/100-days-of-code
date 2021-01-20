import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

try:
    csv_data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    csv_data = pandas.read_csv("./data/french_words.csv")

data_list = csv_data.to_dict(orient="records")

current_card = random.choice(data_list)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    card_canvas.itemconfig(canvas_front, image=card_front_image)
    card_canvas.itemconfig(title, fill="black")
    card_canvas.itemconfig(word, fill="black")

    current_card = random.choice(data_list)

    card_canvas.itemconfig(title, text="French")
    card_canvas.itemconfig(word, text=current_card["French"])

    flip_timer = window.after(3000, func=flip_card)


def right_command():
    global current_card
    data_list.remove(current_card)
    save()
    next_card()


def flip_card():
    card_canvas.itemconfig(canvas_front, image=card_back_image)
    card_canvas.itemconfig(title, fill="white")
    card_canvas.itemconfig(title, text="English")
    card_canvas.itemconfig(word, fill="white")
    card_canvas.itemconfig(word, text=current_card["English"])


def save():
    global data_list
    pandas_data_list = pandas.DataFrame(data_list)
    pandas_data_list.to_csv("./"
                            "data/words_to_learn.csv", index=False)


window = tkinter.Tk()
window.title("Flash Cards")
window.config(width=800, height=700, padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(0, func=next_card)

# create canvases
card_canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR,
                             highlightthickness=0)
card_canvas.grid(row=0, column=0, columnspan=2)

# load image
right_image = tkinter.PhotoImage(file="./images/right.png")
wrong_image = tkinter.PhotoImage(file="./images/wrong.png")
card_back_image = tkinter.PhotoImage(file="./images/card_back.png")
card_front_image = tkinter.PhotoImage(file="./images/card_front.png")

canvas_back = card_canvas.create_image(400, 263, image=card_back_image)
canvas_front = card_canvas.create_image(400, 263, image=card_front_image)

# create buttons
wrong_button = tkinter.Button(image=wrong_image,
                              highlightthickness=0,
                              command=next_card)
wrong_button.grid(row=1, column=0)
right_button = tkinter.Button(image=right_image,
                              highlightthickness=0,
                              command=right_command)
right_button.grid(row=1, column=1)

# create texts
title = card_canvas.create_text(400, 150, font=TITLE_FONT)
word = card_canvas.create_text(400, 263, font=WORD_FONT)

window.mainloop()
