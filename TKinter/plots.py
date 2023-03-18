from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt


root = Tk()

def graph():
    houseprices = np.random.normal(200000, 25000, 5000)
    plt.hist(houseprices, 200)
    #plt.pie(houseprices)
    plt.show() #On the matplotlib website they have all the paramaters and the different types of charts

my_button = Button(root, text='Graph it', command=graph).pack()

root.mainloop()