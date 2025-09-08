w=10 # ，w
x1 = 0 # 
y1 = 10
num=5 # 5
step=10 # 

# ，“”，
# 。：
def up1(event):
    # ，
    for index, ch in enumerate(snake):
        ind=len(snake)-index-1
        if ind==0: # 
            snake[ind].place(x=xx(snake[ind]),y=yy(snake[ind])-step)
        else: # 
            snake[ind].place(x=xx(snake[ind-1]),y=yy(snake[ind-1]))

def down1(event):
    # ，
    for index,ch in enumerate(snake):
        ind=len(snake)-index-1
        if ind==0:
            snake[ind].place(x=xx(snake[ind]),y=yy(snake[ind])+step)
        else:
            snake[ind].place(x=xx(snake[ind-1]),y=yy(snake[ind-1]))

def left1(event):
    # ，
    for index,ch in enumerate(snake):
        ind=len(snake)-index-1
        if ind==0:
            snake[ind].place(x=xx(snake[ind])-step, y=yy(snake[ind]))
        else:
            snake[ind].place(x=xx(snake[ind-1]),y=yy(snake[ind-1]))

def right1(event):
    # ，
    for index,ch in enumerate(snake):
        ind=len(snake)-index-1
        if ind==0:
            snake[ind].place(x=xx(snake[ind])+step,y=yy(snake[ind]))
        else:
            snake[ind].place(x=xx(snake[ind-1]),y=yy(snake[ind-1]))

def xx(moudle):
    # ，xx(moudle)yy(moudle)moudle
    return int(moudle.winfo_geometry().split("+")[1])

def yy(moudle):
    return int(moudle.winfo_geometry().split("+")[2])

# 
from tkinter import *
win = Tk()

# 
snake=[]
for i in range(num):
    item1 = Frame(width=10, height=10, bg="#86E7DD")
    snake.append(item1)
    item1.place(x=x1, y=y1+i*w)

snake[0].config(bg="#E7869D")
win.bind("<Up>",up1) # 
win.bind("<Down>",down1)
win.bind("<Left>",left1)
win.bind("<Right>",right1)
win.mainloop()