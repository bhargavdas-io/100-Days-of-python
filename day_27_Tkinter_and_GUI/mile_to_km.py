from tkinter import *


def convert():
    miles = float(mile_entry.get())
    kilometer = miles * 1.609
    km_result_label.config(text=f"{kilometer}")


window = Tk()
window.title("Mile to Kilometer converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

mile_entry = Entry(width=5, bd=3)
mile_entry.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="KM")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

window.mainloop()
