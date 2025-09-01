
# 
def col():
 arr=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    # , color1+color2, color1+color3
 color1="#"
 for i in range(6):
    color1 += arr[random.randint(0, 15)]
 return color1

        # Label
def color1():
 a = col()
 for i in box1:
    i.config(bg=a)

        # Label
def color2(event):
 a = col()
 for i in box2:
    i.config(bg=a)

from tkinter import *
import random
win=Tk()
win.geometry("330x200")
box1=[]
box2=[]

# Label
for i in range(8):
    for j in range(2):
        label=Label(win,width=5, height=1,relief="groove")
        label.grid(row=j, column=i)
        if (i+j)%2==0:
            box1.append(label)
        else:
            box2.append(label)

btn=Button(win,text="",command=color1)
btn.grid(row=9,column=0,columnspan=8)
btn.bind("<Button-1>",color2,add="+")  # 

win.mainloop()