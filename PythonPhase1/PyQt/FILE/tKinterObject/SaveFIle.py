def sav():
    # Optional file formats
    filetype = [('Python Files', '*.py *.pyw'), ('Text Files', '*.txt'), ('All Files', '*.*')]
    b = asksaveasfile(defaultextension='.py', filetypes=filetype,
                          initialdir='D:\\code', initialfile='Test', title="Save As")
    print(b)


from tkinter import *
from tkinter.filedialog import *

win = Tk()
Button(win, text="Save", command=sav).pack(pady=10)  # Save
win.mainloop()