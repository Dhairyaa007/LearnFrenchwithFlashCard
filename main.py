import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
BLUE = "#16213E"
WHITE = "#FFFFFF"
WORD_FONT = ("ariel", 60, "bold")
LANGUAGE_FONT = ("ariel", 40, "normal")
words_df = pd.read_csv("data/french_words.csv")
count = 0
fr = ''
en = ''
rand_num = 0


def flip_card_en():
    global en, rand_num
    en = words_df.loc[rand_num][1]
    canvas.itemconfig(fr_img, image=card_back_img)
    canvas.itemconfig(language_label, text="ENGLISH", fill=RED)
    canvas.itemconfig(word_label, text=en.capitalize(), fill=WHITE)


def new_card_fr():
    global fr, en, rand_num, flip_timer
    window.after_cancel(flip_timer)
    rand_num = random.randint(0, 100)
    fr = words_df.loc[rand_num][0]
    canvas.itemconfig(fr_img, image=card_front_img)
    canvas.itemconfig(language_label, text="FRENCH", fill=RED)
    canvas.itemconfig(word_label, text=fr.capitalize(), fill=GREEN)
    flip_timer = window.after(3000, func=flip_card_en)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card_en)

canvas = Canvas(width=800, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
right_btn_img = PhotoImage(file="images/right.png")
wrong_btn_img = PhotoImage(file="images/wrong.png")

en_img = canvas.create_image(400, 280, image=card_back_img)
fr_img = canvas.create_image(400, 280, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2, rowspan=2)

language_label = canvas.create_text(400, 200, text="",  font=LANGUAGE_FONT)
canvas.grid(row=0, column=1)

word_label = canvas.create_text(400, 320, text="", font=WORD_FONT)
canvas.grid(row=1, column=1)

right_button = Button(image=right_btn_img, highlightthickness=0, command=new_card_fr)
right_button.grid(row=3, column=1)

wrong_button = Button(image=wrong_btn_img, highlightthickness=0, command=new_card_fr)
wrong_button.grid(row=3, column=2)

new_card_fr()

window.mainloop()
