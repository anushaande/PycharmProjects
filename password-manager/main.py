from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- SEARCH DATA -------------------------------------- #
def search_data():
    website = website_entry.get()
    # read website from json
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror("ERROR", "No Data File Found")
    else:
        try:
            messagebox.showinfo(website, f'Email : {data[website]["email"]}\nPassword: {data[website]["password"]}')
        except KeyError:
            messagebox.showerror("ERROR", "No Record for the given website")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbol_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    number_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letters_list + symbol_list + number_list
    random.shuffle(password_list)

    password = "".join(password_list)

    pwd_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_entry.get()
    uname = uname_entry.get()
    pwd = pwd_entry.get()
    new_data = {website_name: {"email": uname,
                               "password": pwd
                               }

                }

    if len(website_name) == 0 or len(pwd) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            pwd_entry.delete(0, END)

    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=33)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=1)

search_btn = Button(text="Search", width=14, command=search_data)
search_btn.grid(column=2, row=1)

uname_label = Label(text="Email/Username:")
uname_label.grid(column=0, row=2)

uname_entry = Entry(width=52)
uname_entry.grid(column=1, row=2, columnspan=2)
uname_entry.insert(0, "andeanusha24@gmail.com")

pwd_label = Label(text="Password:")
pwd_label.grid(column=0, row=3)

pwd_entry = Entry(width=33)
pwd_entry.grid(column=1, row=3)

generate_pwd_btn = Button(text="Generate Password", width=14, command=generate_password)
generate_pwd_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=44, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
