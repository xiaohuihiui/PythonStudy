def num(a):
    val = pswshow.get()
    if len(val) < 11:
        pswshow.delete(0, END)
        pswshow.insert(0, val + "a")


def back():
    val = pswshow.get()
    if len(val) >= 1:
        pswshow.delete(len(val) - 2, END)
        pswshow.config(text=val[0:len(val) - 2])

def enter():
    val = pswshow.get()
    win2 = Toplevel()
    if len(val) == 11:
        Label(win2, text="\n\n\nwaite\n\n\n").pack()
    else:
        Label(win2, text="\n\n\nnot\n\n\n").pack()



from tkinter import *

win = Tk()
win.title("input password")

# 
pswshow = Entry(win, relief="solid", justify="center")
# 
but1 = Button(win, text="1", command=lambda: num("1"))
but2 = Button(win, text="2", command=lambda: num("2"))
but3 = Button(win, text="3", command=lambda: num("3"))
but4 = Button(win, text="4", command=lambda: num("4"))
but5 = Button(win, text="5", command=lambda: num("5"))
but6 = Button(win, text="6", command=lambda: num("6"))
but7 = Button(win, text="7", command=lambda: num("7"))
but8 = Button(win, text="8", command=lambda: num("8"))
but9 = Button(win, text="9", command=lambda: num("9"))
back1 = PhotoImage(file="back.png")
but0 = Button(win, text="0", height="1", command=lambda: num("0"))
enter2 = PhotoImage(file='enter.png')
butback = Button(win, image=back1, command=back)
butok = Button(win, image=enter2, command=enter)
pswshow.grid(row=1, columnspan=3)

# 
but1.grid(row=5, sticky=W+E)
but2.grid(row=5, column=1, sticky=W+E)
but3.grid(row=5, column=2, sticky=W+E)
but4.grid(row=6, sticky=W+E)
but5.grid(row=6, column=1, sticky=W+E)
but6.grid(row=6, column=2, sticky=W+E)
but7.grid(row=7, sticky=W+E)
but8.grid(row=7, column=1, sticky=W+E)
but9.grid(row=7, column=2, sticky=W+E)
butback.grid(ipady=3,row=8, sticky=W+E)
but0.grid(row=8, column=1, sticky=W+E)
butok.grid(ipady=3,row=8, column=2, sticky=W+E)
win.mainloop()