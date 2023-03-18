from cProfile import label
from errno import EDEADLK
from fileinput import close
from textwrap import fill
from tkinter import *
import ctypes
from tkinter import ttk
from turtle import clear, width
import tkinter as tk
import Pmw

root = Tk()
Pmw.initialise(root)
root.title('Pre-Etch Inspection') # Sets the title for the window
#root.geometry('1280x720') #Changes the dimentions of the window to ''
ctypes.windll.shcore.SetProcessDpiAwareness(1) #Scales the resolution of the window to the current monitor
root.tk.call('tk', 'scaling', 2.0) #Changes the scaling of the text (makes it bigger as scaling the resolution makes the text smaller)
root.iconbitmap('C:/Users/gholl/Downloads/favicon (1).ico') #Upload a .ico picture of the porotech multicolour O onto the P drive and change this directory to that, it will add that as a logo in the corner of the program

#The structure of the program should be 4 frames, one for the buttons, one for the information, one for the inspection and one for the list of wafers in the lot

information_frame = LabelFrame(root) #Not sure how to centre 'text' so I just added a label instead and set it to the middle row
button_frame = LabelFrame(root, padx=22, pady=24)
inspection_frame = LabelFrame(root, padx=0, pady=0)
wafer_list_frame = LabelFrame(root, padx=50, pady=50)

#After looking at the structure of the inspection tab, it might be easier if I make a frame for each widget, so this is what I'm going to do

edge_defects_frame = LabelFrame(inspection_frame, text='Edge Defects')
epi_defects_frame = LabelFrame(inspection_frame, text='Epi Defects')
damage_frame = LabelFrame(inspection_frame, text='Damage', padx=100)
other_frame = LabelFrame(inspection_frame, text='Other', padx=58)
comments_frame = LabelFrame(inspection_frame, text='Comments', padx=25)

edge_defects_frame.grid(row=1, column=2)
epi_defects_frame.grid(row=1, column=0)
damage_frame.grid(row=2, column=0, columnspan=3, sticky=W)
other_frame.grid(row=3, column=0, columnspan=3, sticky=W)
comments_frame.grid(row=4, column=0, columnspan=3, sticky=W)

information_frame.grid(row=0, column=0, sticky=N+E+W+S)
button_frame.grid(row=1, column=0, sticky=S+N+E+W)
inspection_frame.grid(row=0, column=1, rowspan=2, sticky=N+E+W+S)

#label for the information in the top left including the structure of the wafer
information = Label(information_frame, text='Information')
user = Label(information_frame, text='User:')
lotid = Label(information_frame, text='Lot ID:')
lasercode = Label(information_frame, text='Laser Code:')
slotnumber = Label(information_frame, text='Slot Number:')

# The following information needs to be grabbed from the database, for testing purposes I will hard code it in, but the variable data will need to be added
user_id = Label(information_frame, text='George Hollis')
lotid_id = Label(information_frame, text='ST220517005')
lasercode_id = Label(information_frame, text='HJ423280127')
slotnumber_id = Label(information_frame, text='9')


#4 buttons in the bottom left, cancel to close the program, save and close?, Previous to go to the previous wafer in the list, Next to go to the next wafer in the list.

cancel = Button(button_frame, text='Cancel', padx=28, command=root.quit)
saveandclose = Button(button_frame, text='Save & Close', padx=1)
previous = Button(button_frame, text='Previous', padx=20)
next = Button(button_frame, text='Next', padx=36)

#Label for the edge defects and entry for the white edge and clear edge defects, the epi defects label with entry for small, medium and large, entry for minor and major scratches, tick box for cracked, tick box for white spots, black marks preselected percentages
#Finally a comments entry box 
#This might be easier if a frame for each thing that is being inspected is made instead

black_marks_variable=StringVar()
black_marks_variable.set('<0%')




inspection = Label(inspection_frame, text='Inspection')
white_edge_defects = Label(edge_defects_frame, text='White Edge Defects')
white_edge_defects_entry = Entry(edge_defects_frame, width=2)
clear_edge_defects = Label(edge_defects_frame, text='Clear Edge Defects')
clear_edge_defects_entry = Entry(edge_defects_frame, width=2)
small_epi = Label(epi_defects_frame, text='Small:')
small_epi_entry = Entry(epi_defects_frame, width=3)
medium_epi = Label(epi_defects_frame, text='Medium:')
medium_epi_entry = Entry(epi_defects_frame, width=3)
large_epi = Label(epi_defects_frame, text='Large:')
large_epi_entry = Entry(epi_defects_frame, width=3)
cracked = Checkbutton(damage_frame, text='Cracked?')#, variable=cracked_var) #This currently selects both check buttons
minor_scratch = Label(damage_frame, text='Minor Scratch:')
minor_scratch_entry = Entry(damage_frame, width=3)
major_scratch = Label(damage_frame, text='Major Scratch:')
major_scratch_entry = Entry(damage_frame, width=3)
white_spots = Checkbutton(other_frame, text='White Spots?')#, variable=white_spots_var)
black_marks = Label(other_frame, text='Black Marks:')
black_marks_entry = OptionMenu(other_frame, black_marks_variable, '0%', '<1%', '<2%', '<5%')
comment = Entry(comments_frame, width= 40)

#Below are all of the tips which explain what each measurement is

white_edge_defects_tip = Pmw.Balloon(root)
white_edge_defects_tip.bind(white_edge_defects,"These are white marks around the outside of the wafer")
clear_edege_defects_tip = Pmw.Balloon(root)
clear_edege_defects_tip.bind(clear_edge_defects,"These are edge defects, honestly i can't remember what these include lol")
small_epi_tip = Pmw.Balloon(root)
small_epi_tip.bind(small_epi,"These are epi defects that are less that 1mm in diameter")
medium_epi_tip = Pmw.Balloon(root)
medium_epi_tip.bind(medium_epi,"These are epi defects that are between 1mm and 2mm in diameter")
large_epi_tip = Pmw.Balloon(root)
large_epi_tip.bind(large_epi,"These are epi defects that are larger that 2mm in diameter")
cracked_tip = Pmw.Balloon(root)
cracked_tip.bind(cracked,"These are straight, long, parallel lines from the edge of the wafer")
minor_scratch_tip = Pmw.Balloon(root)
minor_scratch_tip.bind(minor_scratch,"These are small scuffs on the surface of wafer")
major_scratch_tip = Pmw.Balloon(root)
major_scratch_tip.bind(major_scratch,"These are large scuffs on the surface of wafer")
white_spots_tip = Pmw.Balloon(root)
white_spots_tip.bind(white_spots,"These are small white spots?")
black_marks_tip = Pmw.Balloon(root)
black_marks_tip.bind(black_marks,"These are usually black lines located of the back end of the wafer")
comment_tip = Pmw.Balloon(root)
comment_tip.bind(comments_frame,"Add here any abnoramal things noticed on the wafer, e.g. Water marks or a very large number of defects")



#The following is putting all of the widgets created onto the screen

information.grid(row=0, column=1, sticky=EW, pady=(0,10))
user.grid(row=1, column=0, sticky=NW)
lotid.grid(row=2, column=0, sticky=NW)
lasercode.grid(row=3, column=0, sticky=NW)
slotnumber.grid(row=4, column=0, sticky=NW)
user_id.grid(row=1, column=3, sticky=NE)
lotid_id.grid(row=2, column=3, sticky=NE)
lasercode_id.grid(row=3, column=3, sticky=NE)
slotnumber_id.grid(row=4, column=3, sticky=NE)

cancel.grid(row= 0, column=0, padx=10, pady=15)
saveandclose.grid(row=0, column=1, padx=10, pady=15)
previous.grid(row=1, column=0, padx=10, pady=15)
next.grid(row=1, column=1, padx=10, pady=15)

inspection.grid(row=0, column=1, sticky=EW)
white_edge_defects.grid(row=0, column=0, sticky=N+E+S+W)
white_edge_defects_entry.grid(row=0, column=1, sticky=N+E+S+W)
clear_edge_defects.grid(row=1, column=0, sticky=N+E+S+W)
clear_edge_defects_entry.grid(row=1, column=1, sticky=N+E+S+W)
small_epi.grid(row=0, column=0, sticky=N+E+S+W)
small_epi_entry.grid(row=0, column=1, sticky=N+E+S+W)
medium_epi.grid(row=1, column=0, sticky=N+E+S+W)
medium_epi_entry.grid(row=1, column=1, sticky=N+E+S+W)
large_epi.grid(row=2, column=0, sticky=N+E+S+W)
large_epi_entry.grid(row=2, column=1, sticky=N+E+S+W)
cracked.grid(row=0, column=0, sticky=N+E+S+W)
minor_scratch.grid(row=0, column=1, sticky=N+E+S+W)
minor_scratch_entry.grid(row=0, column=2, sticky=N+E+S+W)
major_scratch.grid(row=1, column=1, sticky=N+E+S+W)
major_scratch_entry.grid(row=1, column=2, sticky=N+E+S+W)
white_spots.grid(row=0, column=0, sticky=N+E+S+W)
black_marks.grid(row=0, column=1, sticky=N+E+S+W)
black_marks_entry.grid(row=0, column=2, sticky=N+E+S+W)
comment.grid(sticky=N+E+S+W)





root.mainloop()