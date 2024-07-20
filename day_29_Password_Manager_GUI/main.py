from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

FONT = 'Courier'


#--------------------PASSWORD GENERATION------#
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)


#--------------------SAVE PASSWORD------------#
def data():
    website = website_entry.get()
    username = username_entry.get()
    password_ = password_entry.get()

    if len(website) == 0 or len(password_) == 0:
        messagebox.showinfo(title="Retry", message="Please dont leave boxes empty")

    else:
        message_box = messagebox.askokcancel(title=website,
                                             message=f'Details: \nE-Mail \ username: {username} \nPassword: {password_} \nSave?')
        if message_box is True:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password_}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


#--------------------UI SETUP-----------------#
window = Tk()
window.title("Wayne Secure Password Manager")
window.config(padx=20, pady=20)

photo = PhotoImage(file="logo.png")
canvas = Canvas(width=250, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=photo)
canvas.grid(column=2, row=1)

website_label = Label(text="Website: ", font=(FONT, 10, 'bold'), padx=20)
website_label.grid(column=1, row=2)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=2, row=2, columnspan=2)

username_label = Label(text="E-Mail/Username: ", font=(FONT, 10, 'bold'), padx=20)
username_label.grid(column=1, row=3)
username_entry = Entry(width=35)
username_entry.insert(END, '@gmail.com')
username_entry.grid(column=2, row=3, columnspan=2)

password_label = Label(text='Password:', font=(FONT, 10, 'bold'), padx=20)
password_label.grid(column=1, row=4)
password_entry = Entry(width=21)
password_entry.grid(column=2, row=4, columnspan=2)

generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(column=4, row=4)

add_button = Button(text="Add", width=10, command=data)
add_button.grid(column=2, row=5, columnspan=2)

window.mainloop()
