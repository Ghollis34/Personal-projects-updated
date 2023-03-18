from tkinter import *
from PIL import ImageTk, Image

root = Tk()

#r = IntVar()#We want the value to be an intiger so we need to define the variable as int, this function allows tkinter to keep track of the variable over time #If we wanted to pass a string through it would be StringVar()
#r.set(2)#We want to get whatever the variable is at the moment, why we're using this rather than regular python variables. #.set sets the default value for the variable

toppings = [
    ('Pepperoni', 'Pepperoni'),#creating a tuple for each radio button that is going to be made, inside two values are needed
    ('Cheese', 'Cheese'), #The first string is the thing that is going to show up on the screen, the second is the actual value that is going to pass
    ('Mushroom', 'Mushroom'),
    ('Onion', 'Onion'),
]

pizza = StringVar()
pizza.set('Pepperoni')

for text, topping in toppings: #this loops through modes and we take each value (text, mode), easier than making seperate radio buttons
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

def clicked(value): 
    myLabel = Label(root, text=value) #When one of the buttons is clicked, this will pass the value function through and update the label
    myLabel.pack()

#Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack() #The variable has to be assigned to each button so we know what button is pressed and we can do something with the variable if someone clicks the button. #The value is option 1, as it's the first option
#Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda: clicked(r.get())).pack()

#myLabel = Label(root, text=pizza.get())
#myLabel.pack()

myButton = Button(root, text='Click me', command=lambda: clicked(pizza.get())).pack()

root.mainloop()