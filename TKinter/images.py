from tkinter import *
from PIL import ImageTk, Image # References pillow that is a jpeg or png image viewer as python doesn't allow these types of image files

root = Tk()
root.title(':)')
root.iconbitmap('C:/Users/gholl/Downloads/favicon (1).ico') # Allows the icon image to be changed in the top left of the program

my_img = ImageTk.PhotoImage(Image.open('C:/Users/gholl/Downloads/favicon (1).ico')) # This is defining the image and opening it in the file location, the file location doesn't need to be listed if it's in the same directory as the program
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(root, text='Exit Program', command=root.quit)# Adding root.quit as the command for the button quits the program
button_quit.pack()

root.mainloop()