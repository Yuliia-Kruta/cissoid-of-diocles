from tkinter import messagebox as mb
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

# Function to handle input for 'a'
def get_a():
    try:
        a = float(txt1.get())
        if a < 0:
            mb.showerror("Error", "The entered number is less than zero. Try again.")
            txt1.delete(0, END)
            return None
    except ValueError:
        mb.showerror("Error", "Enter a number!")
        txt1.delete(0, END)
        return None
    return a

# Function to handle input for left boundary x1
def get_x1(a):
    try:
        x1 = float(txt2.get())
        if x1 < 0 or x1 >= a:
            mb.showerror("Error", "The entered number is not in the range [0;a). Try again.")
            txt2.delete(0, END)
            return None
    except ValueError:
        mb.showerror("Error", "Enter a number!")
        txt2.delete(0, END)
        return None
    return x1

# Function to handle input for right boundary x2
def get_x2(a, x1):
    try:
        x2 = float(txt3.get())
        if x2 < 0 or x2 >= a or x2 < x1:
            mb.showerror("Error", "The entered number is not in the range [0;a) or less than the left boundary. Try again.")
            txt3.delete(0, END)
            return None
    except ValueError:
        mb.showerror("Error", "Enter a number!")
        txt3.delete(0, END)
        return None
    return x2

# Function to handle input for step
def get_step():
    try:
        step = float(txt4.get())
        if step <= 0:
            mb.showerror("Error", "The entered number is less than or equal to zero.")
            txt4.delete(0, END)
            return None
    except ValueError:
        mb.showerror("Error", "Enter a number!")
        txt4.delete(0, END)
        return None
    return step

# Function to build the graph
def buildGraph():
    a = get_a()
    if a is None:
        return
    x1 = get_x1(a)
    if x1 is None:
        return
    x2 = get_x2(a, x1)
    if x2 is None:
        return
    step = get_step()
    if step is None:
        return

    fig, ax = plt.subplots()
    ax.set_title("Cissoid of Diocles")
    x = np.arange(x1, x2, step)
    y1 = ((x ** 3) / (a - x)) ** 0.5
    y2 = -y1
    ax.plot(x, y1, label="+ Cissoid of Diocles")
    ax.plot(x, y2, label="- Cissoid of Diocles")
    ax.legend()
    plt.show()

# Creating the GUI window
window = Tk()
window.title("Cissoid of Diocles")
window.geometry('545x245')

# Labels and entry fields
Label(window, text="To get the graph, enter the parameter values.", font='Arial 15', pady=2).grid(column=0, row=0)
Label(window, text="Use a dot after the integer part for fractional numbers.", font='Arial 15').grid(column=0, row=1, pady=(0, 20))

Label(window, text="Enter a (it should not be less than zero)", font='Arial 14').grid(column=0, row=4)
txt1 = Entry(window, width=10)
txt1.grid(column=1, row=4)

Label(window, text="Enter the left boundary of the range, which should be within [0;a)", font='Arial 14').grid(column=0, row=5)
txt2 = Entry(window, width=10)
txt2.grid(column=1, row=5)

Label(window, text="Enter the right boundary of the range, which should be within [0;a)", font='Arial 14').grid(column=0, row=6)
txt3 = Entry(window, width=10)
txt3.grid(column=1, row=6)

Label(window, text="Enter the step (the number should be greater than zero)", font='Arial 14').grid(column=0, row=7)
txt4 = Entry(window, width=10)
txt4.grid(column=1, row=7)

Button(window, text="Build Graph", command=buildGraph, font='Arial 14').grid(column=0, row=9, pady=(5, 0))

window.mainloop()
