#Psuedocode
#The gui opens with 7 labels and corresponding ttk comboboxes. The labels are the days of the week, starting at monday and ending on sunday. The comboboxes are populated by a sqllite3 database called menu_items.db. It should grab the meals_and_ingredients table and populate with the meal column.
#Below this there should be 4 buttons: "Add a meal", "Edit a meal", "Generate Ingredients" and "close program"
#The funciton of the add a meal button should open up a new window where the user can enter the name of the new meal and the ingredients, these should then be saved to the database in the corresponding columns by a button at the bottom called "Add meal", once the add meal button is pressed, the new window should close
#The function of the "Edit a meal" button should open a new window with a label: "select what meal you would like to edit:" and next to the label a ttk combobox that is populated with the meal column from the meals_and_ingredients table. There should also be a button labeled "edit". This button will take the value in the combobox and open a new window with a label called "ingredients" and an editable text box populated with the data inside the ingredients column from the corresponding combobox meal selection. This new window will then have a button at the bottom that is labeled "save changes", where the ingredients value will be updated with the new text box values. This will also close all of the windows except the main window
#The function of the "Generate Ingredients" button grabs all of the combobox values in the main window and takes all of the meal values and outputs all of the corresponding ingredients for all selected values in a new window with tickboxes beside each ingredients list 
#The funtion of the "close program" button closes the main window

import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import *
from tkinter import messagebox

# Connect to the SQLite database
conn = sqlite3.connect('menu_items.db')
c = conn.cursor()

# Create the main window
root = tk.Tk()
root.title('Meal Planner')

# Create a dictionary to hold the comboboxes and their selected values
selected_meals = {}

# Create the labels and comboboxes for each day of the week
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for i, day in enumerate(days_of_week):
    # Create the label
    label = tk.Label(root, text=day)
    label.grid(row=i, column=0, padx=5, pady=5)

    # Create the combobox
    combo = ttk.Combobox(root, state='readonly')
    combo.grid(row=i, column=1, padx=5, pady=5)
    selected_meals[day] = combo

    # Populate the combobox with the meals from the database
    c.execute('SELECT meal FROM meals_and_ingredients')
    meals = [row[0] for row in c.fetchall()]
    meals.sort()
    combo['values'] = meals
    
    # Set the width of the combobox based on the longest meal name
    max_width = max(len(meal) for meal in meals)
    combo.config(width=max_width, justify='center')


# Function to handle adding a new meal
def add_meal():
    # Create the new window
    add_window = tk.Toplevel(root)
    add_window.title('Add a meal')

    # Create the entry fields for the new meal and ingredients
    meal_label = tk.Label(add_window, text='Meal:')
    meal_label.grid(row=0, column=0, padx=5, pady=5)
    meal_entry = tk.Entry(add_window)
    meal_entry.grid(row=0, column=1, padx=5, pady=5)

    ingredients_label = tk.Label(add_window, text='Ingredients:')
    ingredients_label.grid(row=1, column=0, padx=5, pady=5)
    ingredients_entry = tk.Text(add_window)
    ingredients_entry.grid(row=1, column=1, padx=5, pady=5)


    # Function to handle adding the new meal to the database
    def save_meal():
        meal = meal_entry.get()
        ingredients = ingredients_entry.get("1.0", END)
        c.execute('INSERT INTO meals_and_ingredients (meal, ingredients) VALUES (?, ?)', (meal, ingredients))
        conn.commit()
        add_window.destroy()

    # Create the button to save the new meal
    add_meal_button = tk.Button(add_window, text='Add meal', command=save_meal)
    add_meal_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

def edit_meal():
    edit_window = tk.Toplevel()
    edit_window.title("Edit Meal")
    edit_window.geometry("200x150")


    def get_meals():
        meals = []
        # select distinct meal names from the meals_and_ingredients table
        c.execute("SELECT DISTINCT meal FROM meals_and_ingredients")
        rows = c.fetchall()
        for row in rows:
            meals.append(row[0])
        meals.sort()
        return meals
    

    def get_ingredients(meal):
        # select ingredients for the specified meal
        c.execute("SELECT ingredients FROM meals_and_ingredients WHERE meal=?", (meal,))
        row = c.fetchone()
        if row is not None:
            return row[0]
        else:
            return ""

    def update_ingredients(meal, ingredients):
        # update ingredients for the specified meal
        c.execute("UPDATE meals_and_ingredients SET ingredients=? WHERE meal=?", (ingredients, meal))
        conn.commit()


    # create select meal label
    select_meal_label = tk.Label(edit_window, text="Select meal you would like to edit:")
    select_meal_label.pack()

    meals = get_meals()
    max_width = max(len(meal) for meal in meals)  # get the longest meal name
    meal_cb = ttk.Combobox(edit_window, values=meals, state="readonly", width=max_width, justify='center')
    meal_cb.current(0)
    meal_cb.pack()
        

    def open_edit_ingredients():
        # create edit ingredients window
        edit_ingredients_window = tk.Toplevel()
        edit_ingredients_window.title("Edit Ingredients")
        

        # get the ingredients for the selected meal
        meal = meal_cb.get()
        ingredients = get_ingredients(meal)

        # create ingredients label
        ingredients_label = tk.Label(edit_ingredients_window, text="Ingredients:")
        ingredients_label.pack()

        # create ingredients text box
        ingredients_text = tk.Text(edit_ingredients_window)
        ingredients_text.insert(END, ingredients)
        ingredients_text.pack()
        

        def save_changes():
            new_ingredients = ingredients_text.get("1.0", END)
            update_ingredients(meal, new_ingredients)
            edit_ingredients_window.destroy()
            edit_window.destroy()

        # create save changes button
        save_changes_button = Button(edit_ingredients_window, text="Save Changes", command=save_changes)
        save_changes_button.pack()

    # create edit button
    edit_button = Button(edit_window, text="Edit", command=open_edit_ingredients)
    edit_button.pack()

    # show the edit window
    edit_window.mainloop()

def generate_ingredients():
    # Create a new window
    window = tk.Toplevel()
    window.title("Ingredients")

    # Retrieve ingredients from the database and store them in a list
    ingredients = {}
    for day, combo in selected_meals.items():
        meal = combo.get()
        if meal:
            c.execute('SELECT ingredients FROM meals_and_ingredients WHERE meal=?', (meal,))
            result = c.fetchone()
            if result:
                new_ingredients = result[0].split(',')
                for ingredient in [i.strip() for i in new_ingredients if i.strip()]:
                    if ingredient not in ingredients:
                        ingredients[ingredient] = 1
                    else:
                        ingredients[ingredient] += 1

    # Sort the ingredients alphabetically
    sorted_ingredients = sorted(ingredients.items())

    # Create a text widget and add the sorted ingredients to it
    text = tk.Text(window, width=50, height=len(sorted_ingredients))
    for ingredient, count in sorted_ingredients:
        if count > 1:
            text.insert(tk.END, f"- {ingredient} x {count}\n")
        else:
            text.insert(tk.END, f"- {ingredient}\n")
    text.pack()





# Create the buttons
add_button = tk.Button(root, text='Add a meal', command=add_meal)
add_button.grid(row=len(days_of_week), column=0, padx=5, pady=5)

edit_button = tk.Button(root, text='Edit a meal', command=edit_meal)
edit_button.grid(row=len(days_of_week), column=1, padx=5, pady=5)

generate_button = tk.Button(root, text='Generate Ingredients', command=generate_ingredients)
generate_button.grid(row=len(days_of_week), column=2, padx=5, pady=5)

close_button = tk.Button(root, text='Close program', command=root.quit)
close_button.grid(row=len(days_of_week)+1, column=1, padx=5, pady=5)

root.mainloop()