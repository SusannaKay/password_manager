from tkinter import * 
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_to_txt():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website != "" and  password != "":
        is_ok = messagebox.askokcancel(title="Check your info", message=f"I'm going to save for {website}:\n User: {email} \n Password: {password}.\n Press 'OK' to save")

        if is_ok:
            with open("password.txt", "a") as txt:
                txt.write(f"{website} | {email} | {password}\n")

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

password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3)

save_button = Button(text="Save", width=40, command=save_to_txt)
save_button.grid(column=1,row=4, columnspan=2)

window.mainloop()

