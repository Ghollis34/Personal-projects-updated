from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title(':P')
root.iconbitmap('C:/Users/gholl/Downloads/favicon (1).ico')

frame = LabelFrame(root, padx=50, pady=50)#The padx and pady here make the space inside of the frame larger #text= - this gives the frame a title of sorts
frame.pack(padx=10, pady=10)#The padx and pady here make the space outside of the frame larger

b = Button(frame, text="Don't click on this")#This places the button inside the frame rather than in the root
b.grid(row=0, column=0)# You can do a grid inside of the frame, which is different to usual where you can only use either pack or grid

a = Button(frame, text= 'or here')
a.grid(row=1, column=0)

root.mainloop()