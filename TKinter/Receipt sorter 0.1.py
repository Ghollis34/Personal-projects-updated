from tkinter import *
import ctypes

root = Tk()
root.geometry('1280x720')
ctypes.windll.shcore.SetProcessDpiAwareness(1)
root.tk.call('tk', 'scaling', 2.0)

jacob_entry = Entry(root)
george_entry = Entry(root)
charlie_entry = Entry(root)

def jacob_total():
    jtotal = jacob_entry.get()

def george_total():
    jtotal = jacob_entry.get()
    sum(jtotal)

def charlie_total():
    jtotal = jacob_entry.get()
    sum(jtotal)


jacob_button = Button(root, text="Calculate Jacob's total", command=jacob_total)
george_button = Button(root, text="Calculate George's total", command=george_total)
charlie_button = Button(root, text="Calculate Charlie's total", command=charlie_total)

jacob_entry.grid(row=0, column=0, padx=50, pady=50)
charlie_entry.grid(row=1, column=0, padx=50, pady=50)
george_entry.grid(row=2, column=0, padx=50, pady=50)
jacob_button.grid(row=0, column=1)
george_button.grid(row=1, column=1)
charlie_button.grid(row=2, column=1)


root.mainloop()