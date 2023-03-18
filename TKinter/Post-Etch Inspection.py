from tkinter import *
import ctypes

root = Tk()
root.geometry('1280x720') #Changes the dimentions of the window to ''
ctypes.windll.shcore.SetProcessDpiAwareness(1) #Scales the resolution of the window to the current monitor
root.tk.call('tk', 'scaling', 2.0) #Changes the scaling of the text (makes it bigger as scaling the resolution makes the text smaller)


root.mainloop()