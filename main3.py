from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x300")
root.title("test it is")
root.config(bg="purple")

import random
import string


def gen():
 output_string = ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(6))
 messagebox.showinfo("generate", output_string)


def exit_program():
    root.destroy()



button_1 = Button(root, text="generate", command=gen)
button_1.place(x=5, y=10)
exit_btn = Button(root, text="Exit", borderwidth="10", bg="purple", command=exit_program, fg="white")
exit_btn.place(x=5, y=100)



root.mainloop()
