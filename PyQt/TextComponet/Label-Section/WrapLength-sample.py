from tkinter import *
win = Tk()
win.configure(bg="#C9EDEB")       # 
win.maxsize(500, 500)             # 
couple = "：；："
txt = Label(win, text=couple, bg="#C9EDEB", font=14, wraplength=120, justify="left")
txt.pack(padx=20, pady=20)
win.mainloop()
