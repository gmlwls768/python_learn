from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters)
                     for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols)
                      for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers)
                      for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)

    if PW_entry.get() == "":
        PW_entry.insert(0, password)
        pyperclip.copy(password)
    else:
        PW_entry.delete(0, 'end')
        PW_entry.insert(0, password)
        pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web = website_entry.get()
    email = Email_entry.get()
    PW = PW_entry.get()

    json_dict = {
        web: {
            "email": email,
            "password": PW,
        }
    }

    if web == "" or PW == "":
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!")
    else:
        is_okay = messagebox.askokcancel(
            title=web, message=f"These are the details entered: \nEmail: {email}"f"\nPassword: {PW} \n Is it okay to save?")
        if is_okay:
            # f = open("Day_029-030/data/data.txt", "a") # It can repleace with open("Day_029-030/data/data.txt", "a") as f
            # f.write(web + " | " + email + " | " + PW + "\n")
            try:
                # How to read json file This type is Dict
                f = open("Day_029-030/data/data.json", "r")
                data = json.load(f)
            except FileNotFoundError:
                f = open("Day_029-030/data/data.json", "w")
                json.dump(json_dict, f, indent=4)  # How to create json file
            else:
                # How to update json file #1 reading old data #2 updating old data with new data #3 saving updated data
                data.update(json_dict)
                f = open("Day_029-030/data/data.json", "w")
                json.dump(data, f, indent=4)  # How to create json file
            finally:
                f.close()
                website_entry.delete(0, 'end')
                PW_entry.delete(0, 'end')

# ---------------------------- Search website ------------------------------- #


def search_web():
    try:
        f = open("Day_029-030/data/data.json", "r")
        data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo("Error", message="No Data File Found.")
    else:
        web = website_entry.get()
        if web in data:
            email_dic = data[web]["email"]
            password_dic = data[web]["password"]
            messagebox.showinfo(
                web, f"Email: {email_dic} \n Password: {password_dic}")
        else:
            messagebox.showinfo(
                "Error", message=f"No details for {web} exists.")

    finally:
        f.close()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)

# img
logo_img = PhotoImage(file="Day_029-030/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# label
Website_label = Label(text="Website:")
Website_label.grid(column=0, row=1)
Email_label = Label(text="Email/Username:")
Email_label.grid(column=0, row=2)
PW_label = Label(text="Password:")
PW_label.grid(column=0, row=3)

# entry
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
Email_entry = Entry(width=35)
Email_entry.insert(0, "@gmail.com")
Email_entry.grid(column=1, row=2, columnspan=2)
PW_entry = Entry(width=21)
PW_entry.grid(column=1, row=3)

# btn
PW_button = Button(text="Generate Password", command=generate_password)
PW_button.grid(column=2, row=3)
ADD_button = Button(text="ADD", width=36, command=save)
ADD_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", command=search_web, width=13)
search_button.grid(column=2, row=1)

window.mainloop()
