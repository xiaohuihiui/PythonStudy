from tkinter import *
step = 5
def up1(event):
    # ，
    if (yy(frame) <= 0):
        win.unbind("<Up>")
    else:
        frame.place(x=xx(frame), y=yy(frame) - step)

# ，
def down1(event):
    # ，
    if (yy(frame) >= 160):
        win.unbind("<Down>")
    else:
        frame.place(x=xx(frame), y=yy(frame) + step)

def left1(event):
    # ，
    if xx(frame) <= 0:
        win.unbind("<Left>")
    else:
        frame.place(x=xx(frame) - step, y=yy(frame))

def right1(event):
    # ，
    if xx(frame) >= 260:
        win.unbind("<Right>")
    else:
        frame.place(x=xx(frame) + step, y=yy(frame))

# ，xx(moudle)yy(moudle)moudle
def xx(module):
    return int(module.winfo_geometry().split("+")[1])

def yy(module):
    return int(module.winfo_geometry().split("+")[2])


win = Tk()
win.geometry("300x200")
win.resizable(0, 0)
frame = Frame(width=40, height=40, bg="#E2ABE5")
frame.place(x=0, y=0)
win.bind("<Up>", up1)  # 
win.bind("<Down>", down1)
win.bind("<Left>", left1)
win.bind("<Right>", right1)
win.mainloop()