# grid()
# row ，column 
from tkinter import *
xin=Tk()                        # 
xin.title("tkinter")   # 

Label(xin,text="1-1",bg="#FFFFF7").grid(row=0,column=0,padx=10)
Label(xin,text="1-2",bg="#FFFFF7").grid(row=0,column=1,padx=10)
Label(xin,text="1-3",bg="#FFFFF7").grid(row=0,column=2,padx=10)
Label(xin,text="2-1",bg="#AEFFF9").grid(row=1,column=0,padx=10)
Label(xin,text="2-2",bg="#AEFFF9").grid(row=1,column=1,padx=10)
Label(xin,text="2-3",bg="#AEFFF9").grid(row=1,column=2,padx=10)
Label(xin,text="3-1",bg="#AEFB8F").grid(row=2,column=0,padx=10)
Label(xin,text="3-2",bg="#AEFB8F").grid(row=2,column=1,padx=10)
Label(xin,text="3-3",bg="#AEFB8F").grid(row=2,column=2,padx=10)
Label(xin,text="4-1",bg="#F1CFFF").grid(row=3,column=0,padx=10)
Label(xin,text="4-2",bg="#F1CFFF").grid(row=3,column=1,padx=10)
Label(xin,text="4-3",bg="#F1CFFF").grid(row=3,column=2,padx=10)

xin.mainloop()
