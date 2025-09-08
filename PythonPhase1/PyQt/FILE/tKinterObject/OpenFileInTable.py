from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *

def a():
    # Open file dialog; the return value is a tuple of filenames
    file = askopenfilenames(title="Select File")
    # Iterate through the tuple and add it to the treeview list
    for i, ch in enumerate(file):
        tree.insert("", index=END, text=i, values=(ch))

win = Tk()
win.title("Display Information of Selected Files")
Button(win, text="Select", command=a).pack(pady=5)  # Add button

tree = Treeview(win, columns=("path"))  # Add treeview list
tree.heading("#0", text="Serial Number")
tree.heading("path", text="Path")
tree.pack()
win.mainloop()