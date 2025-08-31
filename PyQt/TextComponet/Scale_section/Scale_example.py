from tkinter import *
num=0 # 
# , , 
def up1():
    global num
    if scale1.get() < 50:
        val = scale1.get() + 1
        scale1.set(val)
    num=val*5
    txt.config(text=" "+str(num))
# , , 
def down1():
    global num
    if scale1.get() > 0:
        val = scale1.get() - 1
        scale1.set(val)
    num = val * 5
    txt.config(text=" "+str(num))
# , 
def hit(widget):
    global num
    num=scale1.get()*5
    txt.config(text=" "+str(num))
win = Tk()
win.title("")
txt = Label(win,text="TA").pack(side="left")
# txt = Label(win,text="+0").pack(side="left")
# txt.pack(side=TOP)
btndown = Button(win, text="-", command=down1, width=2).pack(side="left")
# 0~50, 1
scale1 = Scale(win, from_=0, to=50, resolution=1, orient=HORIZONTAL, showvalue=0,
 command=hit,troughcolor="#22EBBB")
scale1.pack(side="left")
num = Entry(win)
btnup = Button(win, text="+", command=up1, width=2).pack(side="left")
win.mainloop()