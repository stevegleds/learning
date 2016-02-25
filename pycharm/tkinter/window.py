from tkinter import *
mygui = Tk()
mysecondgui = Tk()

def hello():
    lastuserinput = userinput.get()
    mylabel3 = Label(mysecondgui, text=lastuserinput).pack()


def dele():
    mylabel4 = Label(text='deleted').pack()

userinput = StringVar()
mygui.title('Hello')
mygui.geometry("450x400+450+100")
mysecondgui.title('Second Window')
mysecondgui.geometry("450x500+900+60")
mylabel1 = Label(mygui, text='RESULTS', fg='red', bg='white', font=30).pack()
mybutton1 = Button(mygui, text='Enter', bg='blue', fg='white',font=20, command=hello).place(x=200, y=200)
mybutton2 = Button(mysecondgui, text='Delete', bg='red', fg='white',font=20, command=dele).place(x=300, y=400)
text = Entry(textvariable=userinput).pack()

mygui.mainloop()
