# Display file content
def sav():
    b =askdirectory(title="select or create folder")

    text.insert(0.0, b)  # Add the file's content to the multi-line text box

from tkinter import *
from tkinter.filedialog import *

win = Tk()
Button(win, text="Open File", command=sav).pack(pady=10)
text = Text(win, width=50, height=5)
text.pack()
win.mainloop()