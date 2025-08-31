from tkinter import *
win=Tk()
win.title("")
win.configure(bg="#EEF3C3") # 
img=PhotoImage(file="gwc.png") # 
# Label,compound
Label(win,text="",bg="#EEF3C3").grid(row=3,column=0,columnspan=2)
Label(win,text="",font="-font-14-bg-#EEF3C3").grid(row=4,column=0,sticky=E,pady=10)
Label(win,width=1,bg="#D25EED",relief="groove").grid(row=4,column=1,pady=10)
Label(win,text="",width=20,relief="groove",bg="#B6ABBD").grid(row=4,column=0, columnspan=2,pady=5)
game=Label(win,image=img,text="",compound="bottom",font=" 20 bold",
           fg="#D25EED",bg="#EEF3C3")
game.grid(row=2,column=0,columnspan=2)
# 


win.mainloop()