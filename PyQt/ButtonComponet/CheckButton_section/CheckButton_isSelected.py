def result1():
    sel = ""
    for i in range(len(str1)):

        if (check[i].get() == 1):
            sel = sel + str1[i] + " "

    re.config(text=sel)


from tkinter import *

win = Tk()
win.title("ad")

str1 = ["fd", "fd", "dw", "fd"]

text = Label(win, text="", font="14").grid(row=0, column=0,
                                                                                                     columnspan=6)

check = []
for i in range(len(str1)):
    v = IntVar()
    checkbox = Checkbutton(win, text=str1[i],
                           variable=v,
                           font="12",
                           selectcolor="#00ffff", padx=5)

    checkbox.grid(row=1, column=i)
    check.append(v)

button = Button(win, text="submit", command=result1, font="14", bg="#EFB4DE").grid(row=3, column=0, pady=6, columnspan=6)

re = Label(win, font="12", height="5", width="50", bg="#cfcfcf")
re.grid(row=4, columnspan=5)
win.mainloop()