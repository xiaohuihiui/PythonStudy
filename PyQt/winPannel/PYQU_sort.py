from tkinter import *
win = Tk()
win.title("tkinter")

# 
txt1 = Label(win, text="", bg="#F1CC5C", font=14)
txt2 = Label(win, text="", bg="#A3F3C5", font=14)
txt3 = Label(win, text="", bg="#BCF5CF", font=14)
txt4 = Label(win, text="", bg="#C6D8CC", font=14)
txt5 = Label(win, text="", bg="#F1CC5C", font=14)
txt6 = Label(win, text="", bg="#A3F3C5", font=14)
txt7 = Label(win, text="", bg="#BCF5CF", font=14)
txt8 = Label(win, text="", bg="#C6D8CC", font=14)

txt1.pack(side="left", padx=10, ipadx=6, fill="y", expand=1)
# txt1
txt2.pack(side="left", padx=10, ipadx=6, fill="y", expand=1, before=txt1)

txt3.pack(side="left", padx=10, ipadx=6, fill="y", expand=1, before=txt2)
txt4.pack(side="left", padx=10, ipadx=6, fill="y", expand=1, before=txt3)
txt5.pack(side="left", padx=10, ipadx=6, fill="y", expand=1, before=txt4)
txt6.pack(side="left", padx=10, ipadx=6, fill="y", expand=1, before=txt5)
txt7.pack(side="left", padx=10, ipadx=6, fill="y", expand=1, before=txt6)
txt8.pack(side="left", padx=10, ipadx=6, fill="y", expand=1, before=txt7)

win.mainloop()
