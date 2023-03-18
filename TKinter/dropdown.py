from tkinter import *
from PIL import ImageTk, Image

root = Tk()

def show():
    myLabel = Label(root, text=var.get()).pack()

options = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

var = StringVar()
var.set(options[0]) #This sets the default value for the dropdown box

drop = OptionMenu(root, var, *options).pack() #The variable needs to be called here #The asterisk needs to be before the list

myButton = Button(root, text='show selection', command=show).pack()

root.mainloop()