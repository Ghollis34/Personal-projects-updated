# This is importing *(everything) from the tkinter module to use. It's best practise to import everything from the module
from tkinter import *

# This is the root widget, thought of as the window. This has to happen first, before anything else.
root = Tk()

# You first have to create the label widgets by defining objects and giving them some text
mylabel1 = Label(root, text='Hello World!')
mylabel2 = Label(root, text='My name is George')
mylabel3 = Label(root, text='           ').grid(row=1, column=1) # The .grid can be added at the end of the oject that is created. It is better practice to seperate them to allow for easier reading of the code
# You then have to put what you have defined onto the screen by using .grid or .list- there is probably more, these make them viewable in the UI
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=2)

# This loop is ran as the program itself is a loop that is contantly updating, this is required at the end for the program to work properly
root.mainloop()