from  tkinter import *
root=Tk()
root.title("Hello World")
root.geometry("300x300")

root.maxsize(500,500)
txt1="this is test one"
txt2="this is test 2"
txt3="this is test 3"
text4=Label(root,text=txt1,bg="yellow",foreground="red").pack(side=BOTTOM,padx=10,pady=10,ipady=10,ipadx=10,expand=1)
Label(root,text=txt2,bg="yellow",foreground="red").pack(side=BOTTOM,padx=10,pady=10,ipady=10,ipadx=10,anchor=S)
Label(root,text=txt3,bg="yellow",foreground="red").pack(side=BOTTOM,padx=10,pady=10,ipady=10,ipadx=10,fill=Y)
text4.place(width=300,height=100,x=50,y=100)
root.mainloop()
