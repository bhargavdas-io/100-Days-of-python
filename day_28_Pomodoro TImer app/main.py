from tkinter import *
import math

PINK = '#e2979c'
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# -------------TIMER RESET-----------------#
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    tick.config(text="")
    global reps
    reps = 0


#--------------TIMER MECHANISM-------------#

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="WORK", fg=GREEN)


#--------------COUNTDOWN MECHANISM---------#
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # Dynamic typing
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        for i in range(math.floor(reps / 2)):
            marks += '✔'
        tick.config(text=marks)


#--------------UI SETUP--------------------#
window = Tk()
window.iconbitmap('icon.ico')
window.title("BHARGAV'S POMODORO TIMER")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)
#count_down(5)

start = Button(text="Start", command=start_timer)
reset = Button(text='Reset', command=reset_timer)
start.grid(row=3, column=1)
reset.grid(row=3, column=3)

title_label = Label(text="TIMER", font=(FONT_NAME, 25, "bold"), fg=RED, highlightthickness=0, bg=YELLOW)
title_label.grid(row=1, column=2)

tick = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
tick.grid(row=4, column=2)

window.mainloop()
