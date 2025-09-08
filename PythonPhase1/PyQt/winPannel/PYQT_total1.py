from tkinter import *     # 
xin=Tk()
xin.geometry("350x150")   # 
xin.title("tkinter")   # 

t_x1=Label(xin, text="1", bg="#c4ffd1")
t_x2=Label(xin, text="2", bg="#ccffcc")
t_x3=Label(xin, text="3", bg="#bbd5cc")
t_x1.pack(fill="x", pady="20")  # fill='x'
# side
t_x2.pack(side="right", padx="10", pady="20", anchor="se")
t_x3.pack(side="right", padx="10", ipadx="6", pady="20", anchor="se")

xin.mainloop()
