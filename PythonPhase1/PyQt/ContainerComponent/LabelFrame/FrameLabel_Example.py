def duihuan():
    txt = entry.get()
    # ，，
    if len(txt) > 0:
        re.config(text="!")
    else:
        re.config(text="!")
    re.grid(row=4, column=2)

from tkinter import *

win = Tk()
win.geometry("270x220")
# ，“”
labelFrame = LabelFrame(win, text="", bg="#FFF5D7", padx=20, pady=10, font=14)
labelFrame.grid(row=0, ipadx=10, ipady=10, column=1)

img = PhotoImage(file="cat.png") # 
Label(labelFrame, image=img, bg="#FFF5D7").grid(row=1, column=2)
Label(labelFrame, text="：", bg="#FFF5D7").grid(row=2, column=1, pady=10)

entry = Entry(labelFrame)  # 
entry.grid(row=2, column=2, pady=10)

Button(labelFrame, text="", borderwidth=1, bg="#4EB1FF", command=duihuan).grid(row=3, column=2)

re = Label(labelFrame, bg="#FFF5D7", font=16, fg="red")
win.mainloop()