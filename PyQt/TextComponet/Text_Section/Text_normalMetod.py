# |                 |                                        |
# | ------------------ | ---------------------------------------- |
# | `delete()`         |  Text                            |
# | `get()`            |                                    |
# | `mark_set()`       |                                      |
# | `search()`         |                                      |
# | `edit_undo()`      |                                      |
# | `edit_separator()` | 。，，。 |
from tkinter import *
root = Tk() # 
def undo1(event):
    text.edit_undo() # 
def redo1(event):
    text.edit_redo() # 
def callback(event):
    text.edit_separator() # , 
text = Text(root, width=50, height=30, undo=True, autoseparators=False) # 
text.pack()
# 
text.insert(INSERT, ', <Ctrl+Z><Ctrl+Y>:\n\n')
text.bind('<Key>', callback) # ，
text.bind('<Control-Z>', undo1) # <Ctrl+Z>
text.bind('<Control-Y>', redo1) # <Ctrl+Y>
root.mainloop()