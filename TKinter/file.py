from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog # this needs to be imported so files can be opened

root = Tk()

root.filename = filedialog.askopenfilename(initialdir='/', title='Select a file', filetypes=(('png files', '*.png'),('all files', '*.*')))
#The first thing is the starting directory, when the box pops up which directory will be showing - with initialdir=, using '/' opens the C directory
#The title= is the title of the box that pops up with what directory to select
#Then it's what types of files to show in the pop up by using filetypes=, for several file types they need to be in () seperated with a comma. The first bit in the () is the description of the file that's shown in the dropdown box of the file explorer
#in the second () it is the file type that it's searching for, the * means anything then the suffex of what you want to be selected. *.* returns all files
my_label = Label(root, text=root.filename).pack() #This label shows the directory of the file that is selected in the previous step
my_img = ImageTk.PhotoImage(Image.open(root.filename))#This grabs the image from the directory that is selected in the pop up window
my_img_label = Label(image=my_img).pack()

def open():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir='/', title='Select a file', filetypes=(('png files', '*.png'),('all files', '*.*')))
    my_label = Label(root, text=root.filename).pack() #This label shows the directory of the file that is selected in the previous step
    my_img = ImageTk.PhotoImage(Image.open(root.filename))#This grabs the image from the directory that is selected in the pop up window
    my_img_label = Label(image=my_img).pack()


my_btn = Button(root, text='open file', command=open).pack()


root.mainloop()