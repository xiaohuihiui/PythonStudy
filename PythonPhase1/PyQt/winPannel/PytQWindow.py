from  tkinter import *
root=Tk()
root.title("Hello World")
root.geometry("300x300")
root.configure(bg="yellow")
root.maxsize(500,500)
couptl="\n\n1231232ewqeqweqweqweqwewqerr\n\n"
txt=Label(root,text=couptl,bg="yellow",foreground="red",width=23,height=30,anchor="nw").pack()
root.mainloop()