import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

IMAGE_FILE = "logo.png"
EMAIL = "your.email@mail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    generated_password = "".join(password_list)
    return generated_password


def set_password():
    password = generate_password()
    password_entry.insert(tkinter.END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def delete():
    website_entry.delete(0, tkinter.END)
    password_entry.delete(0, tkinter.END)


def save():
    website = website_entry.get()
    user_name = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": user_name,
            "password": password
        }
    }

    any_is_empty = len(website) == 0 or len(user_name) == 0 or len(password) == 0
    if any_is_empty:
        messagebox.showerror(title="Oops",
                             message="Please make sure you haven't any fields empty!")

    if not any_is_empty:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                              f"Username: {user_name}\n"
                                                              f"Password: {password}\n")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            except json.decoder.JSONDecodeError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                delete()


# ---------------------------- FIND PASSWORD ------------------------ #


def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Oops",
                             message="No Data File Found.\n"
                                     "Please Add Password data.")
    else:
        website = website_entry.get()
        if website in data:
            password_data = data[website]
            messagebox.showinfo(title="Found!",
                                message=f"Website: {website}\n"
                                        f"Email/Username: {password_data['username']}\n"
                                        f"Password: {password_data['password']}\n"
                                        f"You can paste password now.")
            pyperclip.copy(password_data['password'])

        else:
            messagebox.showinfo(title="Oops",
                                message="No details for the website exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
image = tkinter.PhotoImage(file=IMAGE_FILE)
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = tkinter.Label(text="Email/Username:")
username_label.grid(row=2, column=0)
password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = tkinter.Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
username_entry = tkinter.Entry(width=39)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(tkinter.END, EMAIL)
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = tkinter.Button(text="Generate Password",
                                 command=set_password)
generate_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = tkinter.Button(text="Search", width=13,
                               command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
