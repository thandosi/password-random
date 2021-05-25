from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("form")
root.geometry("500x500")
root.config(bg="blue")

s =[2, 22, 90, 34]


def sorting(sequence):
    lenght= len(sequence)

    if lenght <=1:
        return sequence
    else:
        pivot = sequence.pop()
    items_greater =[]
    items_lower =[]

    for i in sequence:
        if i > pivot:
            items_greater.append(i)
        else:
            items_lower.append(i)
    return sorting(items_lower) + [pivot] + sorting(items_greater)


def result():
    messagebox.showinfo("result", sorting(s))


mybtn=Button(root, text="Sorted list", command=result)
mybtn.place(x=5, y=150)
root.mainloop()
