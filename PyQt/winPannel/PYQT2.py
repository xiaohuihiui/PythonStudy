from tkinter import *
from tkinter.ttk import *
root=Tk()
root.title("title")
style=Style()
style.configure("TButton", background="red")
btn=Button(root,text="Click me",style="TButton")
btn.pack(pady=20)
root.mainloop()