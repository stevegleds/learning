from tkinter import *
import tkinter.colorchooser
import tkinter.filedialog

a = Tk()
a.title("Input File")

def mcolour():
        colour = tkinter.colorchooser.askcolor()
        label = Label(text="your chosen colour", bg=colour[1]).pack()  # .pack() produces colour in rgb and hex


def mfileopen():
    filepath = tkinter.filedialog.askopenfile()
    # label = Label(text=filepath).pack()  #  Displays file / filepath chosen by user in Tk window
    filename = filepath.name
    f = open(filename)
    label2 = Label(text=f.read(), font=('arial', 24, 'italic')).pack()



button = Button(text="Choose colour", width=30, command=mcolour).pack()
button = Button(text="Open File", width=30, command=mfileopen).pack()
button = Button(text="Quit", width=30, command=a.destroy).pack()


a.mainloop()
