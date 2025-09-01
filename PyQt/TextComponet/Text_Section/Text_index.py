from tkinter import *
win = Tk()
text = Text(win) # 
text.insert(INSERT, "I love python") # 
text.pack()
print(text.get(2.2, 2.6)) # 1317
win.mainloop()