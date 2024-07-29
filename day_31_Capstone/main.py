from tkinter import *
import random
import pandas
import pandas as pd

#--------------------------CONSTANTS----------------------------#
ORANGE = "#FF7F3E"
CREAM = "#FFF6E9"
SKY = "#80C4E9"
VIOLET = "#604CC3"
BACKGROUND = "#B1DDC6"
current_card = {}
to_learn = {}
#--------------------------RANDOMISE----------------------------#
try:
    df = pd.read_csv('words_to_learn.csv')

except FileNotFoundError:
    original_data = pandas.read_csv('spanish.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = df.to_dict(orient='records')


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    word = current_card["Spanish"]
    canvas.itemconfig(card_title, text="Spanish", fill='black')
    canvas.itemconfig(card_word, text=word, fill='black')
    canvas.itemconfig(canvas_image, image=front_photo)
    timer = window.after(3000, func=flip_card)


#-------------------------NEW CSV----------------------------#
def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index = False)
    next_card()


#-------------------------FLIP-------------------------------#
def flip_card():
    canvas.itemconfig(card_title, text="English", fill=CREAM)
    canvas.itemconfig(card_word, text=current_card["English"], fill=CREAM)
    canvas.itemconfig(canvas_image, image=back_photo)


#-----------------------------UI--------------------------------#

window = Tk()
window.title("FlashQuiz")
window.config(padx=50, pady=50, bg=BACKGROUND)
timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND, highlightthickness=0)
front_photo = PhotoImage(file='card_front.png')
back_photo = PhotoImage(file='card_back.png')
canvas_image = canvas.create_image(400, 270, image=front_photo)
canvas.grid(row=0, column=1, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

right_image = PhotoImage(file='right.png')
wrong_image = PhotoImage(file='wrong.png')
right_button = Button(image=right_image, highlightthickness=0, pady=50, command=next_card)
wrong_button = Button(image=wrong_image, highlightthickness=0, pady=50, command=is_known)

right_button.grid(row=2, column=1)
wrong_button.grid(row=2, column=2)

next_card()

window.mainloop()
