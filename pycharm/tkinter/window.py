from tkinter import *
from tkinter import messagebox
mygui = Tk()
mysecondgui = Tk()


def hello():
    lastuserinput = userinput.get()
    mylabel3 = Label(mysecondgui, text=lastuserinput).pack()


def dele():
    mylabel4 = Label(text='deleted').pack()


def newfile():
    myLabel5 = Label(mygui, text = 'clicked new file', font=('roman', 24, 'italic')).pack()


def savemessagebox():
    messagebox.showinfo(title='save', message='are you sure?')


def quitprogram():
    quitresponse = messagebox.askyesno(title='Quit', message='Are you sure you want to go home?')
    if quitresponse == 1:
        mygui.destroy()


userinput = StringVar()
mygui.title('Hello')
mygui.geometry("450x400+150+100")
mysecondgui.title('Second Window')
mysecondgui.geometry("450x400+650+100")
mylabel1 = Label(mygui, text='RESULTS', fg='red', bg='white', font=('arial', 24, 'italic')).pack()
mybutton1 = Button(mygui, text='Enter', bg='blue', fg='white', font=('times', 24, 'bold'), command=hello, ).place(x=200, y=200)
mybutton2 = Button(mysecondgui, text='Delete', bg='red', fg='white',font=20, command=dele).place(x=300, y=400)
text = Entry(textvariable=userinput).pack()

mymenu = Menu()
listfile = Menu()
listfile.add_command(label='New File', command=newfile) #note not newfile()
listfile.add_command(label='Edit')
listfile.add_command(label='Save File', command=savemessagebox)
listfile.add_command(label='Quit', command=quitprogram)
listedit = Menu()
listedit.add_command(label='undo')
listedit.add_command(label='redo')

mymenu.add_cascade(label="File", menu=listfile)
mymenu.add_cascade(label="Edit", menu=listedit)
mymenu.add_cascade(label="Format")
mymenu.add_cascade(label="Run")

mygui.config(menu=mymenu)

mygui.mainloop()
