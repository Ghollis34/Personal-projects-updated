from tkinter import *
from PIL import ImageTk, Image

root = Tk()

def show():
    myLabel = Label(root, text=var.get()).pack()

#var = IntVar() #For a checkbox the value that you are assigning to the checkbox is either a 0 or a 1, so it needs to be an int variable. #The first thing that needs to be defined for a checkbox is a variable

var = StringVar()#This will allow the selection to be a string

c = Checkbutton(root, text='Check this box', variable=var, onvalue='on', offvalue='off') #You have to assign the variable that you want it to be stored as #The on and off value functions allow you to name what you want the box values to return
c.deselect() #This deselects the checkbox by default
c.pack()


myButton = Button(root, text='show selection', command=show).pack()

root.mainloop()