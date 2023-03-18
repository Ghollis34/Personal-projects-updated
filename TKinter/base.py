from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title('Hello')

def open():
    top = Toplevel() # This top level function creates a new window
    top.title('world') # If there is a variable inside the function it will need to be defined as global 
    btn2 = Button(top, text='close window', command=top.destroy).pack() # This will create a button that will then close the pop up window that's made as that is the function of .destroy

btn = Button(root, text='open second window', command=open).pack()

#top = Toplevel() # This top level function creates a new window
#top.title('world')
#my_img = ImageTk.PhotoImage(Image.open("C:\Users\gholl\Downloads\favicon (1).ico"))
#my_label = Label(top, image=my_img).pack()
#lbl = Label(top, text='hello world').pack()

root.mainloop()