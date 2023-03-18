from audioop import add
from glob import glob
from optparse import Option
from tkinter import *
#from PIL import ImageTk, Image
import ctypes
import sqlite3
from tkinter.scrolledtext import ScrolledText


root = Tk()
root.title('Weekly Menu')
ctypes.windll.shcore.SetProcessDpiAwareness(1)
root.tk.call('tk', 'scaling', 2.0)
#root.iconbitmap('C:/Users/gholl/Downloads/food.ico')
root.geometry('1280x720')

conn = sqlite3.connect('menu_items.db')

c = conn.cursor()

# c.execute('''CREATE TABLE meals_and_ingredients(
#     meal text,
#     ingredients blob
# )
# ''')

#placeholder optionmenu variables and holders
monday_var = StringVar()
tuesday_var = StringVar()
wednesday_var = StringVar()
thursday_var = StringVar()
friday_var = StringVar()
saturday_var = StringVar()
sunday_var = StringVar()
#all_ingredients = str(monday_var.get()) + str(tuesday_var.get())
placeholder_options = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']

#TODO This needs to be done next
meals = StringVar()
c.execute('SELECT meal FROM meals_and_ingredients')
meals = c.fetchall



def add_meal_button_new():
    conn = sqlite3.connect('menu_items.db')
    c = conn.cursor()

    c.execute('INSERT INTO meals_and_ingredients VALUES (:meal, :ingredients)',
    {
        'meal': new_meal_entry.get(),
        'ingredients': new_ingredients_entry.get('1.0', 'end')
    })

    conn.commit()
    conn.close()

    new_meal_entry.delete(0, END)
    new_ingredients_entry.delete('1.0', END)


def add_meal_window():
    global add_new_meal
    global new_meal_entry
    global new_ingredients_entry
    add_new_meal = Tk()
    add_new_meal.title('Add a New Meal')

    new_meal_label = Label(add_new_meal, text='New Meal:')
    new_meal_label.grid(row=0, column=0)
    new_ingredients_label = Label(add_new_meal, text='Ingredients:')
    new_ingredients_label.grid(row=1, column=0)

    new_meal_entry = Entry(add_new_meal, width=30)
    new_meal_entry.grid(row=0, column=1, padx=20, pady=20)
    new_ingredients_entry = ScrolledText(add_new_meal)
    new_ingredients_entry.grid(row=1, column=1, padx=20, pady=20)
    
    add_new_meal_button = Button(add_new_meal, text='Add Meal', command=add_meal_button_new)
    add_new_meal_button.grid(row=2, column=0, columnspan=2, pady=20, ipadx=100)


def edit_meal():
    global edit_meal_window
    edit_meal_window = Tk()
    edit_meal_window.title('Edit Your Meals')
    select_meal_label = Label(edit_meal_window, text='Select What Meal You Would Like to Edit:')
    select_meal_label.grid(row=0, column=0, padx=20, pady=20)

    #create a database or connect to one
    conn = sqlite3.connect('menu_items.db')
    #create a cursor
    c = conn.cursor()
    #query the database
    c.execute('SELECT meal, oid FROM meals_and_ingredients')#the * selects everything in the adresses table #The oid is the identifying id key for each record
    records = c.fetchall()#fetches all of the records, #fetchone or fetchany work
    #print(records)
    #loop through results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + '\n ' + str(record[1]) + '\n ' #+ '\t ' + str(record[2]) +' \n'
    
    query_label = Label(edit_meal_window, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

    #commit changes
    conn.commit()

    #close connection
    conn.close()


def generate_ingredients():
    ingredients = Tk()
    ingredients.title('Ingredients List')
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    ingredients.tk.call('tk', 'scaling', 2.0)
    ingredients.iconbitmap('C:/Users/gholl/Downloads/food.ico')
    ingredients.geometry('1280x720')
    conn = sqlite3.connect('menu_items.db')
    #create a cursor
    c = conn.cursor()
    c.execute('SELECT ingredients FROM meals_and_ingredients')#the * selects everything in the adresses table #The oid is the identifying id key for each record
    records = c.fetchall()
    ingredients_list = ''
    for record in records:
        ingredients_list += str(record[0]) + '\n '
    ingredients_label = Label(ingredients, text=ingredients_list)
    ingredients_label.grid(row=0, column=0)
    conn.commit()

    #close connection
    conn.close()

def close_root():
    root.destroy()


#list of the days with dropdown menus of each of the meals

monday_label = Label(root, text='Monday:').grid(row=0, column=0, pady=(20,0), padx=20)
tuesday_label = Label(root, text='Tuesday:').grid(row=1, column=0, pady=(20,0), padx=20)
wednesday_label = Label(root, text='Wednesday:').grid(row=2, column=0, pady=(20,0), padx=20)
thursday_label = Label(root, text='Thursday:').grid(row=3, column=0, pady=(20,0), padx=20)
friday_label = Label(root, text='Friday:').grid(row=4, column=0, pady=(20,0), padx=20)
saturday_label = Label(root, text='Saturday:').grid(row=5, column=0, pady=(20,0), padx=20)
sunday_label = Label(root, text='Sunday:').grid(row=6, column=0, pady=(20,0), padx=20)

monday_dropdown = OptionMenu(root, meals, meals).grid(row=0, column=1)
tuesday_dropdown = OptionMenu(root, tuesday_var, *placeholder_options).grid(row=1, column=1)
wednesday_dropdown = OptionMenu(root, wednesday_var, *placeholder_options).grid(row=2, column=1)
thursday_dropdown = OptionMenu(root, thursday_var, *placeholder_options).grid(row=3, column=1)
friday_dropdown = OptionMenu(root, friday_var, *placeholder_options).grid(row=4, column=1)
saturday_dropdown = OptionMenu(root, saturday_var, *placeholder_options).grid(row=5, column=1)
sunday_dropdown = OptionMenu(root, sunday_var, *placeholder_options).grid(row=6, column=1)


#button to add a meal and add the ingredients, button to edit a meal and the ingredients including a delete function

add_meal_button = Button(root, text='Add A Meal', command=add_meal_window)
add_meal_button.grid(row=7, column=0, pady=(100,0), padx=50, ipadx=20)

edit_meal_button = Button(root, text='Edit A Meal', command=edit_meal)
edit_meal_button.grid(row=7, column=1, pady=(100,0), padx=50, ipadx=20)

generate_ingredients_button = Button(root, text='Generate Ingredients', command=generate_ingredients)
generate_ingredients_button.grid(row=7, column=2, pady=(100,0), padx=50, ipadx=20)

close_program_button = Button(root, text='Close Program', command=close_root)
close_program_button.grid(row=7, column=3, pady=(100,0), padx=50, ipadx=20)

conn.commit()
conn.close()
root.mainloop()