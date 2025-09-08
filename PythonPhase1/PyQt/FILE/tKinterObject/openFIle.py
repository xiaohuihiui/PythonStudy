from tkinter import *
from tkinter.filedialog import *

def a():
    # Open file dialog
    bb = askopenfilename(title="Select File", filetype=[("PNG format image file", "*.png")])

win = Tk()
Button(win, text="Select", command=a).pack() # Add button
win.mainloop()