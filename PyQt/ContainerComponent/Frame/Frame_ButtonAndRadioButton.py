def all():
    # for
    for index,item in enumerate(checkbox):
        item.set(True)

# 
def none():
    #
    for index,item in enumerate(checkbox):
        item.set(False)

# 
def inverse():
    # ，，，
    for index,item in enumerate(checkbox):
        if item.get()==False:
            item.set(True)
        else:
            item.set(False)


from tkinter import *


win = Tk()
frame1 = Frame(win, width=200, height=50,borderwidth=9,background="red") # ，
frame1.grid(row=0, column=0)
frame2 = Frame() # ，
frame2.grid(row=1, column=0)

# tkinter，
val = BooleanVar()
val.set(1)  # 2 ()

# 
radio1 = Radiobutton(frame1, value=0, variable=val, text="", command=all)
radio1.grid(row=0, column=0)
radio2 = Radiobutton(frame1, value=1, variable=val, text="", command=none)
radio2.grid(row=0, column=1)

radio3 = Radiobutton(frame1, value=2, variable=val, text="", command=inverse)
radio3.grid(row=0, column=3)

# 
fruits = ["", "", "", "", ""]
checkbox = [] # 

for index, item in enumerate(fruits):
    str = BooleanVar()
    str.set(False)
    Checkbutton(frame2, text=item, variable=str).grid(row=index+1, column=1) # 
    checkbox.append(str)

win.mainloop()