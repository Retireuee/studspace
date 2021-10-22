from tkinter import *
from tkinter.ttk import Combobox


def shell(arr):
    print(arr)
    gg = arr.sort()
    return gg


def spr(arr):
    print(arr)
    gg = arr.sort()
    return gg


def qsort(arr):
    print(arr)
    gg = arr.sort()
    return gg


def bubble(arr):
    print(arr)
    gg = arr.sort()
    return gg


class gui:

    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x800")
        self.text = Text(self.root, width=55, height=4, bg="white", fg='black', font=15, wrap=WORD)
        self.var = IntVar()
        self.var.set(0)
        self.red = Radiobutton(text="шелл", variable=self.var, value=0)
        self.green = Radiobutton(text="разделение", variable=self.var, value=1)
        self.blue = Radiobutton(text="квиксорт", variable=self.var, value=2)
        self.yellow = Radiobutton(text="пузырек", variable=self.var, value=3)
        self.button = Button(text="обновить результат", command=self.change)
        self.label = Label(self.root, text="-")
        self.gg = ""

        self.fill()

    def fill(self):
        self.text.place(x=20, y=30)
        self.red.place(x=600, y=30)
        self.green.place(x=600, y=90)
        self.blue.place(x=600, y=150)
        self.button.place(x=20, y=150)
        self.yellow.place(x=600, y=210)
        self.label.place(x=30, y=210)

    def change(self):
        self.label["text"] = ""
        message = self.text.get(0.1, END)
        if self.var.get() == 0:
            gg = message.split()
            shell(gg)
            self.label["text"] = gg
        elif self.var.get() == 1:
            gg = message.split()
            spr(gg)
            self.label["text"] = gg
        elif self.var.get() == 2:
            gg = message.split()
            qsort(gg)
            self.label["text"] = gg
        elif self.var.get() == 3:
            gg = message.split()
            bubble(gg)
            self.label["text"] = gg


a = gui()
a.root.mainloop()
