from tkinter import *

# ，
def add(from1, to1):
    # from1.curselection() 
    item1 = from1.get(from1.curselection())  # 
    to1.insert(END, item1)  # 
    from1.delete(from1.curselection())  # 

win = Tk()
win.title("")
win.geometry("250x200")
Label(win, text="").grid(row=0, column=0)
Label(win, text="").grid(row=0, column=2)

# 
val1 = StringVar()  # 
val1.set("   ")
val2 = StringVar()  # 
val2.set("   ")

# 
listbox1 = Listbox(win, bg="#FFF8DC", selectbackground="#D15FEE", selectmode="single", listvariable=val1, height=8, width=10)
listbox2 = Listbox(win, bg="#C1FFC1", selectbackground="#D15FEE", selectmode="single", listvariable=val2, height=8, width=10)

listbox1.grid(row=1, column=0, rowspan=2)
listbox2.grid(row=1, column=2, rowspan=2)

btn1 = Button(win, text=">>>", command=lambda: add(listbox1, listbox2))
btn1.grid(row=1, column=1, padx=10)
btn2 = Button(win, text="<<<", command=lambda: add(listbox2, listbox1))
btn2.grid(row=2, column=1, padx=10)

win.mainloop()