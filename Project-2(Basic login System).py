#Basic Login System
#A simple login window
from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("1099x600")
win.config(bg="yellow")
win.title("Basic Login System")

def selected_login():
    
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Define separate StringVars for username and password
username_var = StringVar()
password_var = StringVar()

#--------------------------------------------------------------------------------------------------------#
label_username = Label(win, text="username", font=("Times New Roman", 50, "bold"), bg="red")
label_username.place(x=70, y=50, width=300, height=100)

entry_username = Entry(win, font=("Times New Roman", 50, "bold"), bd=8, textvariable=username_var)
entry_username.place(x=400, y=50, width=700, height=100)

#--------------------------------------------------------------------------------------------------------#
label_password = Label(win, text="password", font=("Times New Roman", 50, "bold"), bg="red")
label_password.place(x=70, y=200, width=300, height=100)

entry_password = Entry(win, font=("Times New Roman", 50, "bold"), bd=8, show="*", textvariable=password_var)
entry_password.place(x=400, y=200, width=700, height=100)

#--------------------------------------------------------------------------------------------------------#
login_button = Button(win, text="Login", font=("Times New Roman", 50, "bold"), bg="lightgreen", bd=8, command=selected_login)
login_button.place(x=400, y=400, width=300, height=100)

win.mainloop()
