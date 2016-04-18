from tkinter import *
import tkinter.colorchooser
a = Tk()
def mcolour():
        colour = tkinter.colorchooser.askcolor()
        label = Label(text="your chosen colour", bg=colour[1]).pack()  # .pack() produces colour in rgb and hex
button = Button(text="Choose colour", width=30, command= mcolour).pack()
a.mainloop()
