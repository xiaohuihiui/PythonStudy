from tkinter import *

win = Tk()
win.geometry("360x120")
box = Frame(width=100, height=100, relief="groove", borderwidth=9)  # 
box.grid(row=0, column=0, pady=10, padx=10) # 
txt = "，6，8，9，？" # 
Label(box, text=txt, wraplength=320, justify="left", font=14).grid(columnspan=4)

select = ["8", "6", "9", "0"]  # 
val = IntVar()  # val

for i in range(len(select)):
    # ，box
    Radiobutton(box, text=select[i], value=i, variable=val).grid(row=1, column=i)

win.mainloop()