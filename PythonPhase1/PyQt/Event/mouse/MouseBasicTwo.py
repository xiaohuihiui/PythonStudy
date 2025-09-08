from tkinter import *
import random
num=1  # 
#  (A) 
inde=random.randint(0, 99)
# 
def panduan(event):
    global num
    num+=1  # 1
    level.config(text=""+str(num)+"")
    # A
    inde = random.randint(1, 100)
    # 
    colorBox=col()
    for i in squareBox:
        i.config(bg=colorBox[0])
    squareBox[inde].config(bg=colorBox[1])
    # A
    squareBox[inde].bind("<Button-1>",panduan)

def col():
    arr=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    # , color1+color2, color1+color3A
    color1=""
    color2=""
    color3=""

    for i in range(4):
        color1+=arr[random.randint(0,15)]
    for i in range(2):
        color2+=arr[random.randint(0,15)]
    for i in range(2):
        color3+=arr[random.randint(0,15)]

    colorArr = [] # 2
    colorArr.append("#"+color1+color2)
    colorArr.append("#"+color1+color3)
    return colorArr




win = Tk()
win.geometry("270x270")
win.resizable(0,0)
sqareBox=[] # 
colorBox=col()
for i in range(10): # i
    for j in range(10): # j
        label=Label(win,width=3,height=1,bg=colorBox[0],relief="groove")
        sqareBox.append(label) # 
        label.grid(row=i,column=j)
sqareBox[inde].config(bg=colorBox[1])
sqareBox[inde].bind("<Button-1>",panduan) # 
level=Label(win,text="1",font=14)
level.grid(row=11,column=0,columnspan=10,pady=10)
win.mainloop()