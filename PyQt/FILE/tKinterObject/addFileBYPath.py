from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

b=""
#Create and save file
def sav():
    global b
    # Optional file formats
    filetype = [('Python Files', '*.py *.pyw'),('Text Files', '*.txt'),('All Files', '*.*')]
    b=asksaveasfile(defaultextension = '.py',filetypes = filetype,initialdir = 'D:\\code',
initialfile = 'Test',title = "Save As")

# Add content
def add1():
    global text
    a = text.get(0.0, END)
    print(len(a))
    if len(a) <= 1:
        showerror("Error", "Content cannot be empty")
    else:
        file = open(b.name, "w", encoding='utf-8')
        file.write(a)
        file.close()
        win.quit()
def edit1():
    if b == "":
        showerror("Error", "File does not exist, please create a file first")
    else:
        text.grid(row=2, column=0, columnspan=3)
win = Tk()
Button(win, text="Create File", command=sav).grid(row=0, column=0, padx=10)
Button(win, text="Edit Content", command=edit1).grid(row=0, column=1, padx=20, pady=10)
Button(win, text="Submit", command=add1).grid(row=0, column=2, padx=10)
text = Text(win, width=50, height=5)
win.mainloop()