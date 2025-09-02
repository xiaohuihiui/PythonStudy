# Modify MySQL data (incomplete)
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import pymysql

num = 0  # The ID (serial number) of the currently modified item
x1 = ""  # The serial number of the double-clicked row
y1 = ""  # The serial number of the double-clicked column
val = ""  # The value of the double-clicked cell
iid = ""  # The ID of the double-clicked item

book_title = ["ID", "name", "category", "price", "publish_time"]
book_heading = ["Serial", "Name", "Category", "Price", "Publish Time"]

# Open database connection, parameters: 1: main machine name or IP; 2: username; 3: password; 4: database name
db = pymysql.connect(host="localhost", user="root", password="369852", database="mrsoft")

# Use the cursor() method to create a cursor object
cursor = db.cursor()


def showinfo1():
    # Use execute() method to execute SQL query
    cursor.execute("SELECT * FROM books")

    # Use fetchall() method to get all data
    data = cursor.fetchall()

    row = cursor.rowcount  # Get number of rows

    item_num = len(tree.get_children())
    if item_num > 0:
        for item in tree.get_children():
            tree.delete(item)

    for i in range(row):  # Loop through history data
        tree.insert("", END, values=data[i])  # Display the fetched data in the table
def modi():
    if entry.get() == "":
        showerror("Error", "Please add complete information")
        return False
    elif entry.get() == val:
        showinfo("Warning", "Information not modified")
        return False
    else:
        info_id = tree.item(iid)["values"][0]  # The ID of the data to be modified
        info_it = book_title[int(y1.replace("#", "")) - 1]  # The item to be modified
        info_text = entry.get()  # The content to be modified
        cursor.execute("UPDATE books SET " + info_it + "=%s WHERE ID=%s", (info_text, info_id))
        entry.delete(0, END)
        showinfo1()  # Update the data in the table


def add1(event):
    global x1
    global y1
    global val
    global iid
    entry.delete(0, END)
    it = event.widget  # The item double-clicked
    iid = it.identify("item", event.x, event.y)
    x1 = it.identify("row", event.x, event.y)
    y1 = it.identify("column", event.x, event.y)
    val = it.item(iid)["values"][int(y1.replace("#", "")) - 1]
    entry.insert(INSERT, val)
    label.config(text=book_heading[int(y1.replace("#", "")) - 1] + ":")
win = Tk()
win.title("Modify Book Data Information")
frame = Frame(width=100, relief="groove")  # Place text box
label = Label(frame, text="Modify:")
label.grid(row=0, column=0)
entry = Entry(frame)
entry.grid(row=0, column=1)
Button(frame, text="Modify Content", command=modi).grid(row=0, column=2)
frame.grid(row=0, column=0)
tree = Treeview(win, columns=book_title, show="headings", height=5)
tree.grid(row=1, column=0, columnspan=9)

for it in range(len(book_heading)):
    tree.heading(book_title[it], text=book_heading[it])
    tree.column(book_title[it], width=120)

showinfo1()
tree.bind("<Double-Button-1>", add1)
win.mainloop()