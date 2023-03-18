from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('400x400')#This defines the size of the window

def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + 'x' + str(vertical.get()))

vertical = Scale(root, from_=0, to=500)#The scale widget is used to make a slider and two things need to be called, the from_ and to, from_ needs a _ after it
vertical.pack()#It's important to pack the slider on it's own line otherwise it ruins things

horizontal = Scale(root, from_=0, to=500, orient=HORIZONTAL)#use orient=HORIZONTAL to get the widget sideways
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()



my_btn = Button(root, text='click me', command=slide).pack()

root.mainloop()