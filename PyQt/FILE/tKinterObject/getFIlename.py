# Display file content
def sav():
    b = askopenfile(title="Open File", filetypes=[("Text Files", "*.txt")])
    file = open(b.name, "r")
    text.insert(0.0, file.readlines())  # Add the file's content to the multi-line text box

from tkinter import *
from tkinter.filedialog import *

win = Tk()
Button(win, text="Open File", command=sav).pack(pady=10)
text = Text(win, width=50, height=5)
text.pack()
win.mainloop()