# 
def result1():
    # re.delete("0.0", END)
    print(v.get())
    if v.get() == 0:  #  “” 
        str="：\n，，。，，。"
    elif v.get() == 1: #  “” 
        str="：\n，，，，。"
    elif v.get() == 2:  #  “” 
        str="：\n，，。，，，，，，。"
    else:  #  “” 
        str="：\n，，，。"
    re.config(text=str)

from tkinter import *

win = Tk()
win.title("")
# 
str1 = ["", "", "", "","noway"]
Label(win, text="", font="14").pack(anchor=W)
text = Label(win, text="，？", font="14").pack(anchor=W)
v = IntVar()
for i in range(len(str1)):  # 
    # text，value
    # indicatoron，selectcolor
    radio = Radiobutton(win, text=str1[i], variable=v, value=i, font="12", indicatoron=0, selectcolor="#EEFFFF")
    radio.pack(side=TOP, fill=X, padx=20, pady=3)

# 
button = Button(win, text="", command=result1, font="14", bg="#4CC6E3").pack(side=TOP, fill=X, padx=40, pady=20)

# Label
re = Label(win, font="14", height="10", width="40", justify="left", wraplength=320)
re.pack(side=TOP, pady=10)
win.mainloop()