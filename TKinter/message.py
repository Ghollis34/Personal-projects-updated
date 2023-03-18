from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()

def popup():
    response = messagebox.showerror('This is my popup', 'hello world') #There are several different types of message box, messagebox.showinfo() shows a message on the screen, the first paramaeter is the title of the pop up window, the second is the text inside the window
                                                            #showwarning - it has a warning sign and error sound, showerror - it has an error warning sign and sound, askquestion - gives a yes or no pop up, askokcancel - gives an okay or cancel pop up, askyesno- gives a yes or no pop up
    Label(root, text=response).pack()
    #if response == 'yes':
    #    Label(root, text='you clicked yes').pack()
    #else:
    #    Label(root, text='you clicked no').pack()

Button(root, text='pop-up', command=popup).pack()

root.mainloop()

#show info returns ok
#show warning returns ok
#askyesno returns 1 for yes and 0 for no
#askokcancel returns 1 for yes and 0 for cancel
#askquestion returns yes for yes and no for no
#showerror returns ok