# Query MySQL data
from tkinter import *
from tkinter.ttk import *
import pymysql
# Open database connection, parameters: 1: hostname or IP; 2: username; 3: password; 4: database name
db = pymysql.connect(host="localhost", user="root", password="369852", database="mrsoft")

# Use the cursor() method to create a cursor object
cursor = db.cursor()

db.ping(reconnect=True)  # If the database connection is disconnected, reconnect

# Use the execute() method to perform an SQL query
cursor.execute('SELECT * FROM books')

# First get all data
data = cursor.fetchall()

row = cursor.rowcount  # Get number of rows
def checkInfo():
    keyWords = {"Book Name": 1, "Serial": 2, "Price": 3, "Publish Time": 4} # A dictionary to store the column index corresponding to each title
    getInfo = val.get() # Get the column name
    mess = entry.get() # Get the keyword
    showinfo(keyWords[getInfo], mess)


def showinfo(kw, value):
    global label
    label.destroy() # Destroy the label widget
    item_num = len(tree.get_children())
    if item_num > 0: # Clear the content from the last query
        for item in tree.get_children():
            tree.delete(item)

    for i in range(row): # Loop through the data
        # Add data that matches the criteria to the table
        if data[i][int(kw)] == value:
            tree.insert("", END, values=data[i]) # Display the fetched data in the table

    if len(tree.get_children()) == 0: # If no query results are found, show a text prompt
        label = Label(win, text="Sorry, no information found", font=14)
        label.grid(row=1, column=0, columnspan=3)

db.close()  # Close the database connection

win = Tk()
win.title("Query Book Data Information")
val = StringVar()
val.set("Serial")
cb = Combobox(win, textvariable=val, values=("Book Name", "Price", "Serial", "Publish Time"))
cb.grid(pady=5, row=0, column=0)
entry = Entry(win)
entry.grid(row=0, column=1)
label = Label(win, text="Sorry, no information found", font=14)
Button(win, text="Query", command=checkInfo).grid(row=0, column=2)
tree = Treeview(win, columns=("num", "name", "category", "price", "publish_time"),
show="headings", height=5)
tree.grid(row=2, column=0, columnspan=3)
tree.heading("num", text="Serial")  # Set table heading
tree.column("num", width=40)
tree.heading("name", text="Book Name")
tree.column("name", width=60)
tree.heading("category", text="Serial")
tree.column("category", width=60)
tree.heading("price", text="Price")
tree.column("price", width=60)
tree.heading("publish_time", text="Publish Time")
tree.column("publish_time", width=120)

win.mainloop()

