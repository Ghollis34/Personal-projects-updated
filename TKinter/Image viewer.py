from ast import Lambda
from tkinter import *
from PIL import ImageTk, Image # References pillow that is a jpeg or png image viewer as python doesn't allow these types of image files

root = Tk()
root.title(':)')
root.iconbitmap('C:/Users/gholl/Downloads/favicon (1).ico') # Allows the icon image to be changed in the top left of the program

my_img1 = ImageTk.PhotoImage(Image.open('C:/Users/gholl/Downloads/favicon (1).ico'))
my_img2 = ImageTk.PhotoImage(Image.open('C:/Users/gholl/Downloads/favicon (1).ico'))
my_img3 = ImageTk.PhotoImage(Image.open('C:/Users/gholl/Downloads/favicon (1).ico'))
my_img4 = ImageTk.PhotoImage(Image.open('C:/Users/gholl/Downloads/favicon (1).ico')) # This is defining the image and opening it in the file location, the file location doesn't need to be listed if it's in the same directory as the program
my_img5 = ImageTk.PhotoImage(Image.open('C:/Users/gholl/Downloads/favicon (1).ico'))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5] #Makes a list that makes it easy to cycle through the items, we're just referencing the next or previous item in the list and showing it on the screen, forgetting the previous one that was there


my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label #Globals were used so the the variables work outside of the function
    global button_next
    global button_back

    my_label.grid_forget() # .grid_forget gets rid of something that in the postition so that it can be replaced with a new object
    my_label = Label(image=image_list[image_number-1])#The image we're wanting to show is the current image -1 as the list starts at 0 not 1
    button_next = Button(root, text='Next', command=lambda: forward(image_number+1)) #We want the next image so it's the current image +1
    button_back = Button(root, text='Previous', command=lambda: back(image_number-1))#Going back to the previous image.  We also have to define the buttons again and add them to the grid again for them to be visable when moving to the next image

    if image_number == 5:
        button_next = Button(root, text='Next', state=DISABLED) # This if statement stops the next button from working by disabling it when the image number is 5, as there are only 5 images

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0) 
    button_next.grid(row=1, column=2)

def back(image_number):
    global my_label
    global button_next
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])#The image we're wanting to show is the current image -1 as the list starts at 0 not 1
    button_next = Button(root, text='Next', command=lambda: forward(image_number+1)) #We want the next image so it's the current image +1
    button_back = Button(root, text='Previous', command=lambda: back(image_number-1))#Going back to the previous image.  We also have to define the buttons again and add them to the grid again for them to be visable when moving to the next image

    if image_number == 1:
        button_back = Button(root, text='Previous', state=DISABLED) # This if statement stops the next button from working by disabling it when the image number is 5, as there are only 5 images

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0) 
    button_next.grid(row=1, column=2)

button_back = Button(root, text='Previous', command=back, state=DISABLED) 
button_exit = Button(root, text='Exit', command=root.quit)
button_next = Button(root, text='Next', command=lambda: forward(2)) # Lambda is used again to pass something through the funciton, 2 is used to pass to the second image

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_next.grid(row=1, column=2)


root.mainloop()