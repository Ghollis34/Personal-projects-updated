from fileinput import filename
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror
from tkinter.ttk import Combobox
from unittest import TestCase
from src.fitting import run
from pathlib import Path
from src.model import get_list_of_material_codes


root = Tk()
root.title('Delta Thickness')

paths_frame = LabelFrame(root, padx=5, pady=5, text='Paths', relief=RIDGE)
paths_frame.grid(row=0, column=0, padx=10)

mat_codes_frame = LabelFrame(root, padx=50, pady=15, text='Material Codes', relief=RIDGE)
mat_codes_frame.grid(row=1, column=0)

res_dir_frame = LabelFrame(root, padx=17, pady=15, text='Results Directory', relief=RIDGE)
res_dir_frame.grid(row=2, column=0)

def pre_open():
    variables['pre_etch_reflectivity_directory'] = filedialog.askdirectory(initialdir='/', title='Select a File')
    pre_etch_ref_path_entry.insert(0, str(variables['pre_etch_reflectivity_directory']))

def post_open():
    variables['post_etch_reflectivity_directory'] = filedialog.askdirectory(initialdir='/', title='Select a File')
    post_etch_ref_path_entry.insert(0, str(variables['post_etch_reflectivity_directory']))

def results_dir_open():
    variables['results_directory'] = filedialog.askdirectory(initialdir='/', title='Select a File')
    results_dir_path_entry.insert(0, str(variables['results_directory']))

def run_function():
    test = True
    try: 
        if  not variables['pre_etch_reflectivity_directory'].get():
            showerror('Error', 'No Pre-Etch Reflectivity Directory Has Been Selected.')
            test = False
    except:
        pass
    try:
        if not variables['post_etch_reflectivity_directory'].get():
            showerror('Error', 'No Post-Etch Reflectivity Directory Has Been Selected.')
            test = False
    except:
        pass
    if not variables['pre_etch_material_code']:
        showerror('Error', 'No Pre-Etch Material Code Has Been Selected.')
        test = False
    if not variables['post_etch_material_code']:
        showerror('Error', 'No Post-Etch Material Code Has Been Selected.')
        test = False
    try:
        if not variables['results_directory'].get():
            showerror('Error', 'No Results Directory Has Been Selected.')
            test = False
    except:
        pass
    if variables['pre_etch_reflectivity_directory'] == variables['post_etch_reflectivity_directory']:
        showerror('Error', 'Both File Directories Are The Same')
        test = False
    if test:    
        run(variables['pre_etch_reflectivity_directory'], variables['post_etch_reflectivity_directory'], variables['results_directory'], variables['pre_etch_material_code'], variables['post_etch_material_code'])


variables = {
    'pre_etch_reflectivity_directory': StringVar(),
    'post_etch_reflectivity_directory': StringVar(),
    'results_directory': StringVar(),
    'pre_etch_material_code': StringVar(),
    'post_etch_material_code': StringVar()
}

variables['pre_etch_material_code'] = Combobox(mat_codes_frame, textvariable=variables['pre_etch_material_code'], postcommand=get_list_of_material_codes, width=45).grid(row=2, column=1, pady=10)


variables['post_etch_material_code'] = Combobox(mat_codes_frame, textvariable=variables['pre_etch_material_code'], postcommand=get_list_of_material_codes, width=45).grid(row=3, column=1, pady=10)


pre_etch_ref_path = Label(paths_frame, text='Pre-Etch Reflectivity Path:')
post_etch_ref_path = Label(paths_frame, text='Post-Etch Reflectivity Path:')

pre_etch_ref_path_entry = Entry(paths_frame, width=50)
post_etch_ref_path_entry = Entry(paths_frame, width=50)

pre_etch_ref_path_entry_button = Button(paths_frame, text='Open...', command=pre_open)
post_etch_ref_path_entry_button = Button(paths_frame, text='Open...', command=post_open)


pre_etch_mat_code = Label(mat_codes_frame, text='Pre-Etch Material Code:')
post_etch_mat_code = Label(mat_codes_frame, text='Post-Etch Material Code:')

results_dir_path = Label(res_dir_frame, text='Results Directory Path:')
results_dir_path_entry = Entry(res_dir_frame, width=50)
results_dir_path_button = Button(res_dir_frame, text='Open...', command=results_dir_open)

run_button = Button(root, text='Run', command=run_function)
close_button = Button(root, text='Close', command=root.destroy)


pre_etch_ref_path.grid(row=0, column=0)
post_etch_ref_path.grid(row=1, column=0)
pre_etch_ref_path_entry.grid(row=0, column=1)
post_etch_ref_path_entry.grid(row=1, column=1)
pre_etch_ref_path_entry_button.grid(row=0, column=3, padx=10, pady=10)
post_etch_ref_path_entry_button.grid(row=1, column=3, padx=10, pady=10)
pre_etch_mat_code.grid(row=2, column=0, sticky=W)
post_etch_mat_code.grid(row=3, column=0, sticky=W)
results_dir_path.grid(row=4, column=0)
results_dir_path_entry.grid(row=4, column=1)
results_dir_path_button.grid(row=4, column=3, padx=10, pady=10)
run_button.grid(row=3, column=0, sticky=SE, ipadx=50, pady=10, padx=10)
close_button.grid(row=3, column=0, sticky=SW, ipadx=50, pady=10, padx=10)

root.mainloop()