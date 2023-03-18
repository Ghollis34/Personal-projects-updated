from audioop import add
from tkinter import *
from unittest import TestCase
from PIL import ImageTk, Image
import sqlite3 #This imports the sqlite3 database into the program

root = Tk()

#create a database or connect to one
conn = sqlite3.connect('address_book.db') #The value that is passed in here either selects a pre-existing database or makes a new one depending on whether or not one exists - saving it in the current directory that the program is in

#create a cursor
c = conn.cursor() #This is what the commands are executed with

#create a table

# c.execute("""CREATE TABLE addresses(
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode integer
# )
# """)

def update():
    #create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    #create a cursor
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute('''UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid''',
        {
            'first': f_name_editor.get(),
            'last': l_name_editor.get(),
            'address': address_editor.get(),
            'city': city_editor.get(),
            'state': state_editor.get(),
            'zipcode': zipcode_editor.get(),
            
            'oid': record_id
        })

    #commit changes
    conn.commit()

    #close connection
    conn.close()


    editor.destroy()


#create function to edit a record

def edit():
    global editor
    editor = Tk()
    editor.title('Edit a data entry')

    #create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    #create a cursor
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute('SELECT * FROM addresses WHERE oid = ' + record_id)#the * selects everything in the adresses table #The oid is the identifying id key for each record
    records = c.fetchall()#fetches all of the records, #fetchone or fetchany work
    #print(records)
    
    #create gloabl variables for text box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    #create text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10,0))#this adds 10 padding to the top
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    #create text box labels
    f_name_label = Label(editor, text='First Name:').grid(row=0, column=0, pady=(10,0))
    l_name_label = Label(editor, text='Last Name:').grid(row=1, column=0)
    address_label = Label(editor, text='Address:').grid(row=2, column=0)
    city_label = Label(editor, text='City:').grid(row=3, column=0)
    state_label = Label(editor, text='State:').grid(row=4, column=0)
    zipcode_label = Label(editor, text='Zipcode:').grid(row=5, column=0)

    #loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    #create a save button to save edited record
    edit_button = Button(editor, text='save record', command=update)
    edit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)
     


    #commit changes
    conn.commit()

    #close connection
    conn.close()

#create function to delete a record

def delete():
    #create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    #create a cursor
    c = conn.cursor()

    #delete a record
    c.execute('DELETE from addresses WHERE oid= ' + delete_box.get()) # this has to be concantinated on the end

    delete_box.delete(0, END)

    #commit changes
    conn.commit()

    #close connection
    conn.close()
   



#create submit function to the db
def submit():
    #inside of the function you have to connect to the db
    #create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    #create a cursor
    c = conn.cursor()

    #insert into table
    c.execute('INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)',
    {
        'f_name': f_name.get(),
        'l_name': l_name.get(),
        'address': address.get(),
        'city': city.get(),
        'state': state.get(),
        'zipcode': zipcode.get()
    })
    #commit changes
    conn.commit()

    #close connection
    conn.close()



    #clear the text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

#create query function
def query():
    #create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    #create a cursor
    c = conn.cursor()
    #query the database
    c.execute('SELECT *, oid FROM addresses')#the * selects everything in the adresses table #The oid is the identifying id key for each record
    records = c.fetchall()#fetches all of the records, #fetchone or fetchany work
    #print(records)
    #loop through results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t ' + str(record[6]) +' \n'
    
    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

    #commit changes
    conn.commit()

    #close connection
    conn.close()



#create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))#this adds 10 padding to the top
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)


#create text box labels
f_name_label = Label(root, text='First Name:').grid(row=0, column=0, pady=(10,0))
l_name_label = Label(root, text='Last Name:').grid(row=1, column=0)
address_label = Label(root, text='Address:').grid(row=2, column=0)
city_label = Label(root, text='City:').grid(row=3, column=0)
state_label = Label(root, text='State:').grid(row=4, column=0)
zipcode_label = Label(root, text='Zipcode:').grid(row=5, column=0)
delete_box_label = Label(root, text='ID number:').grid(row=9, column=0, pady=5)

#create submit button
submit_button = Button(root, text='Add record to database', command=submit).grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#create a query button
query_button = Button(root, text='show records', command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#create a delete button
delete_button = Button(root, text='delete record', command=delete)
delete_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#create an update button
edit_button = Button(root, text='edit record', command=edit)
edit_button.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

#commit changes
conn.commit()

#close connection
conn.close()

root.mainloop()