# importing from tkinter

from tkinter import *
from tkinter import messagebox

# creating a window


root = Tk()
root.title("Login")
root.geometry("500x500")
root.config(bg="purple")

# Creating my labels and entries
input_label1 = Label(root, text="Please enter Username")
input_label1.place(x=5, y=5)
user_entry = Entry(root)
user_entry.place(x=200, y=5)

input_label2 = Label(root, text="Please enter Password")
input_label2.place(x=5, y=50)
pass_entry = Entry(root, show="*")
pass_entry.place(x=200, y=50)

# Functions


def log():
    username = ["sive", "lihle", "nathi", "thando"]
    passwords = ["1234", "1111", "0000", "9090"]
    found = False
    for x1 in range(len(username)):
        if user_entry.get() == username[x1] and pass_entry.get() == passwords[x1]:
            found = True
        if found == True:
            messagebox.showinfo("STATUS", "Access granted")
            root.destroy()
            import main3

    else:
        messagebox.showinfo("ERROR INFO", "Access denied")



def clear():
    user_entry.delete(0, END)
    pass_entry.delete(0, END)


def exit_program():
    root.destroy()

# creating btn


log_btn = Button(root, text="Login", borderwidth="10", bg="purple", command=log, fg="white")
log_btn.place(x=125, y=100)
clear_btn = Button(root, text="Clear", borderwidth="10", bg="purple", command=clear, fg="white")
clear_btn.place(x=250, y=100)
exit_btn = Button(root, text="Exit", borderwidth="10", bg="purple", command=exit_program, fg="white")
exit_btn.place(x=375, y=100)

root.mainloop()
