from tkinter import * 
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_psw():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list=[]

    password_list += [ choice(letters) for char in range(randint(8,10))]
    password_list += [ choice(symbols) for char in range(randint(2,4))]
    password_list += [ choice(numbers) for char in range(randint(2,4))]

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_to_txt():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = { website:

        {"email":email,
        "password": password,}
    }
    if website != "" and  password != "":
        is_ok = messagebox.askokcancel(title="Check your info", message=f"I'm going to save for {website}:\n User: {email} \n Password: {password}.\n Press 'OK' to save")

        if is_ok:
            try:
                with open("password.json","r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("password.json", "w") as data_file:
                    json.dump(new_data,data_file, indent=4)

            else: 
                data.update(new_data)
                with open("password.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
    else:
        messagebox.showerror(title="Warning!", message="Do not leave any field empty")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(height=200,width=200)
logo = PhotoImage(file= "logo.png")
canvas.create_image(100,100,  image = logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(column=1,row=1,columnspan=2)


email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

email_entry = Entry(width=40)
email_entry.insert(0,"youremail@email.com")
email_entry.grid(column=1,row=2,columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

password_button = Button(text="Generate Password", command=gen_psw)
password_button.grid(column=2, row=3)

save_button = Button(text="Save", width=40, command=save_to_txt)
save_button.grid(column=1,row=4, columnspan=2)

window.mainloop()

