x1=350
step=2
op=1 #
bar=1 #

def move1():
    global bar
    bar=1
    global x1
    global fish
    global op
    if(x1>=350):  #
        op=-1
        canvas.delete(fish)
        fish = canvas.create_image(x1, 50, image=fish1)

    if(x1<=8):  #
        op=1
        canvas.delete(fish)
        fish = canvas.create_image(x1, 50, image=fish2)

    x1=x1+op*step
    canvas.coords(fish, (x1,50))

def move_fish():  #
    while bar:
        move1()  #
        time.sleep(0.1)  #
        win.update()  #
def catch_fish():
    canvas.coords(cat, (150, 50))
    global bar
    bar = 0  # 
    if abs(x1-50)<=160 and abs(x1-50)>=40:  #
        showinfo("", "，")
    else:
        showinfo("", "，")


from tkinter import *
from tkinter.messagebox import *
import time
win = Tk()
win.title("")
win.geometry("400x400")
canvas = Canvas(win, width=400, height=320, relief="solid", bg="#E7D2BB")
cat1=PhotoImage(file="cat.png")
fish1=PhotoImage(file="cat.png")
fish2=PhotoImage(file="cat.png")
fish=canvas.create_image(350,50,image=fish1) #
cat=canvas.create_image(150,250,image=cat1) #
canvas.grid(row=0,column=0, columnspan=2)
btn=Button(win,text="",command=move_fish).grid(row=1,column=0)
Button(win,text="",command=catch_fish).grid(row=1,column=1)
win.mainloop()