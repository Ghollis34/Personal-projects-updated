# from tkinter import *
# from tkinter.tix import *

# root = Tk()

# #Create tooltip
# tip = Balloon(root)
# tip.config(bg='red') #This changes the outside border of the tooltip to red

# #we can play with subcatagories
# tip.label.config(bg='red', fg='green') # This changes the background and forground colour of the 'label' which is actually the arrow in the top left hand corner of the tooltip
# tip.message.config(bg='white', fg='black')#This will change the actual tooltip message box, the foreground is the colour of the text and the bg is the colour of the background
# for sub in tip.subwidgets_all():
#     sub.configure(bg='white')
# #label
# my_label = Label(root, text='Text')
# my_label.pack(pady=20)

# #button
# my_button = Button(root, text='Click me')
# my_button.pack(pady=50)

# #bind tooltip to button
# tip.bind_widget(my_button, balloonmsg= 'This is a cool tooltip')

# tip.bind_widget(my_label, balloonmsg= 'This is a cool ')


# root.mainloop()



#You need to pip install pmw on the computer for this code to work


from tkinter import *
import Pmw #This is the module that needs to be imported for them to work

root = Tk()
Pmw.initialise(root) # This bit of text needs to be added

# Create some random widget
button = Button(root, text = " This is a Test", pady = 30)
button.pack(pady = 10)

# create ballon object and bind it to the widget 
balloon = Pmw.Balloon(root)
balloon.bind(button,"Text for the tool tip")

mainloop()