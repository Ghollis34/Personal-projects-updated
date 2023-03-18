from tkinter import *
from tokenize import maybe

root = Tk()

# To get a button to do something you have to give it a funciton which has to be defined
def myClick():
    myLabel = Label(root, text="I clicked a button")
    myLabel.pack()

myButton = Button(root, text='Click Me!', command=myClick, bg='red') #state=DISABLED - this disables the button from working
                                                    #padx= - this changes the size of the button in the x direction (wider)
                                                    #pady= - this changes the size of the button in the y direction (taller)
                                                    #command= - this gives the button a function that calls the function. You cannot add () after the name of the function or it will run it before the button is pressed
                                                    #fg= 'colour of your choice' - this makes the text a colour of your choice. Hexcode colours also work
                                                    #bg= 'colour of your choice' - this makes the background a colour of your choice. Hexcode colours also work
myButton.pack()

root.mainloop()
