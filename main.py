from tkinter import * 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_to_txt():
    txt = open("password.txt", "a")
    txt.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
    txt.close()
    website_entry.delete(0,END)
    password_entry.delete(0,END)



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

