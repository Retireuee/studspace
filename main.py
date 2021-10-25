from tkinter import *
from tkinter.ttk import Combobox
import random
from random import randint
import time


def shell(data):
    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return data


def insertion(data):
    #for i in range(len(data)):
       # j = i - 1
       # key = data[i]
       # while data[j] > key and j >= 0:
         #   data[j + 1] = data[j]
        #    j -= 1
       # data[j + 1] = key
    return data


def partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx


def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx - 1)
    quick_sort_recursion(array, pivot_idx + 1, end)
    return array


def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    return quick_sort_recursion(array, begin, end)


def bubble(arr):
    def swap(y, j):
        arr[y], arr[j] = arr[j], arr[y]

    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
    return arr


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
        self.rand_button = Button(text="randomize", command=self.rand_output)
        self.label = Label(self.root, text="-")
        self.gg = ""
        self.ll = []
        self.entry = []
        self.amount_elems = 1
        self.runtime = 0
        self.runtime_log = Label(self.root, text="runtime")

        self.rand_array()
        self.fill()

    def fill(self):
        self.text.place(x=20, y=30)
        self.red.place(x=600, y=30)
        self.green.place(x=600, y=90)
        self.blue.place(x=600, y=150)
        self.button.place(x=20, y=150)
        self.yellow.place(x=600, y=210)
        self.label.place(x=30, y=210)
        self.rand_button.place(x=160, y=150)

    def rand_array(self):
        self.amount_elems = randint(100, 1000)
        for i in range(self.amount_elems):
            self.entry.append(randint(1, 2000))

    def rand_output(self):
        if self.var.get() == 0:
            self.ll = entry.copy()
            start_time = time.time()
            shell(self.ll)
            amount_time = time.time() - start_time
            self.label["text"] = self.ll
        elif self.var.get() == 1:
            start_time = time.time()
            insertion(self.ll)
            amount_time = time.time() - start_time
            self.label["text"] = self.ll
        elif self.var.get() == 2:
            start_time = time.time()
            quick_sort(self.ll)
            amount_time = time.time() - start_time
            self.label["text"] = "здесь хранится ", self.amount_elems, " элементов,\nя не буду выводить это на экран"
        elif self.var.get() == 3:
            start_time = time.time()
            bubble(self.ll)
            amount_time = time.time() - start_time
            self.label["text"] = "здесь хранится ", self.amount_elems, " элементов,\nя не буду выводить это на экран"

    def change(self):
        self.label["text"] = ""
        message = self.text.get(0.1, END)
        if self.var.get() == 0:
            gg = message.split()
            start_time = time.time()
            shell(gg)
            amount_time = time.time() - start_time
            self.label["text"] = gg
        elif self.var.get() == 1:
            gg = message.split()
            start_time = time.time()
            insertion(gg)
            amount_time = time.time() - start_time
            self.label["text"] = gg
        elif self.var.get() == 2:
            gg = message.split()
            start_time = time.time()
            quick_sort(gg)
            amount_time = time.time() - start_time
            self.label["text"] = gg
        elif self.var.get() == 3:
            gg = message.split()
            start_time = time.time()
            bubble(gg)
            amount_time = time.time() - start_time
            self.label["text"] = gg


a = gui()
a.root.mainloop()
