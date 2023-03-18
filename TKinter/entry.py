from tkinter import *

root = Tk()

e = Entry(root, width=50) # Creates an entry widget
                # width = - changes the width of the text entry box
                #bg= - changes the background colour of the text box
                #fg= - changes the text colour
                #borderwidth= - adds a border to the text box
e.pack()
e.insert(0, 'Enter your name') #Puts default text inside the text box
#e.get() - Gets everything that was added into the 'e' text box

def myClick():
    hello = 'Hello ' + e.get()
    myLabel = Label(root, text=hello) #Gets everything that was added into the 'e' text box
    myLabel.pack()


myButton = Button(root, text='Enter your name', command=myClick, bg='red')
myButton.pack()

root.mainloop()