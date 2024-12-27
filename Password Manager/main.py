import json
import os
import random

from tkinter import *
from tkinter import messagebox

IMAGE_PATH = "Python Bootcamp/Intermediate/Password Manager/logo.png"
ARCHIVE_PATH = "Python Bootcamp/Intermediate/Password Manager/archive.txt"
DATA_FILE = "Python Bootcamp/Intermediate/Password Manager/data_file.json"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
WEBSITE_PLACEHOLDER = "somesite.com"
EMAIL_PLACEHOLDER = "somemail@mail.com"
PASSWORD_PLACEHOLDER = "S0m3P@ssw0rd?"
PLACEHOLDER_COLOUR = "Gray"
ORIGINCAL_FONT_COLOUR = "Black"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password  = [random.choice(LETTERS) for _ in range(random.randint(3, 6))]
    password += [random.choice(NUMBERS) for _ in range(random.randint(2, 4))]
    password += [random.choice(SYMBOLS) for _ in range(random.randint(2, 4))]
    random.shuffle(password)
    
    password_input.delete(0, END)
    password_input.insert(0, "".join(password))
    password_input.config(fg=ORIGINCAL_FONT_COLOUR)

# ---------------------------- SAVE PASSWORD ------------------------------- #
    
def save_password():

    if any([website_input.cget("fg") == PLACEHOLDER_COLOUR,
            email_input.cget("fg") == PLACEHOLDER_COLOUR,
            password_input.cget("fg") == PLACEHOLDER_COLOUR]):
        messagebox.showerror("Invalid input", "Empty field/s")
        return
    else:
        website = website_input.get()
        email = email_input.get()
        password = password_input.get()

        new_data = {
            website: {
                "email": email,
                "password": password
            }
        }

        try:
            with open(DATA_FILE, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open(DATA_FILE, "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open(DATA_FILE, "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            website_input.insert(0, WEBSITE_PLACEHOLDER)
            website_input.config(fg=PLACEHOLDER_COLOUR)
            website_input.focus()
            email_input.delete(0, END)
            email_input.insert(0, EMAIL_PLACEHOLDER)
            email_input.config(fg=PLACEHOLDER_COLOUR)
            password_input.delete(0, END)
            password_input.insert(0, PASSWORD_PLACEHOLDER)
            password_input.config(fg=PLACEHOLDER_COLOUR)

        with open(ARCHIVE_PATH, "a") as file:
            file.write(format_output(website, email, password))

def format_output(website, email, password):
    output = ""
    line = f"+{'-' * 30}+{'-' * 30}+{'-' * 30}+ \n"

    if os.path.getsize(ARCHIVE_PATH) == 0:
        output += line
        output += f"|{'Website'.center(30, ' ')}|{'Email/Username'.center(30, ' ')}|{'Password'.center(30, ' ')}|\n"
        output += line

    output += f"|{website.center(30, ' ')}|{email.center(30, ' ')}|{password.center(30, ' ')}|\n"
    output += line

    return output

# ---------------------------- SEARCH ------------------------------- #

def search():

    website = website_input.get()

    try:
        with open(DATA_FILE, "r") as file:
                data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Info", message="No data file found")
    else:
        if website in data:
            messagebox.showinfo(title="Info", message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Info", message="No data entry found")

# ---------------------------- UI EFFECTS ------------------------------- #

def on_focus(event, widget):
    
    match widget:
        case "website":
            if website_input.get() == WEBSITE_PLACEHOLDER and website_input.cget("fg") == PLACEHOLDER_COLOUR:
                website_input.delete(0, END)
                website_input.config(fg=ORIGINCAL_FONT_COLOUR)
        case "email":
            if email_input.get() == EMAIL_PLACEHOLDER and email_input.cget("fg") == PLACEHOLDER_COLOUR:
                email_input.delete(0, END)
                email_input.config(fg=ORIGINCAL_FONT_COLOUR)
        case "password":
            if password_input.get() == PASSWORD_PLACEHOLDER and password_input.cget("fg") == PLACEHOLDER_COLOUR:
                password_input.delete(0, END)
                password_input.config(fg=ORIGINCAL_FONT_COLOUR)

def off_focus(event, widget):

    match widget:
        case "website":
            if not website_input.get():
                website_input.insert(0, WEBSITE_PLACEHOLDER)
                website_input.config(fg=PLACEHOLDER_COLOUR)
        case "email":
            if not email_input.get():
                email_input.insert(0, EMAIL_PLACEHOLDER)
                email_input.config(fg=PLACEHOLDER_COLOUR)
        case "password":
            if not password_input.get():
                password_input.insert(0, PASSWORD_PLACEHOLDER)
                password_input.config(fg=PLACEHOLDER_COLOUR)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.geometry("+600+200")

image = PhotoImage(file=IMAGE_PATH)
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_input = Entry(width=24)
website_input.insert(0, WEBSITE_PLACEHOLDER)
website_input.config(fg=PLACEHOLDER_COLOUR)
website_input.grid(row=1, column=1)
website_input.focus()
website_input.bind("<FocusIn>", lambda e: on_focus(e, "website"))
website_input.bind("<FocusOut>", lambda e: off_focus(e, "website"))
search_button = Button(text="Search", width=6, command=search)
search_button.grid(row=1, column=2, sticky=E+W)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_input = Entry(width=35)
email_input.insert(0, EMAIL_PLACEHOLDER)
email_input.config(fg=PLACEHOLDER_COLOUR)
email_input.grid(row=2, column=1, columnspan=2, pady=5)
email_input.bind("<FocusIn>", lambda e: on_focus(e, "email"))
email_input.bind("<FocusOut>", lambda e: off_focus(e, "email"))

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_input = Entry(width=24)
password_input.insert(0, PASSWORD_PLACEHOLDER)
password_input.config(fg=PLACEHOLDER_COLOUR)
password_input.grid(row=3, column=1)
password_input.bind("<FocusIn>", lambda e: on_focus(e, "password"))
password_input.bind("<FocusOut>", lambda e: off_focus(e, "password"))

generate_button = Button(text="Generate", command=generate_password)
generate_button.grid(row=3, column=2, sticky=E+W)

add_button = Button(text="Add", command=save_password)
add_button.grid(row=4, column=0, columnspan=3, pady=(5, 0), sticky=E+W)


window.mainloop()