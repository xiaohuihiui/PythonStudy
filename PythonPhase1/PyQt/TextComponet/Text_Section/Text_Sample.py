from platform import machine

i = 0 # ，0
def show():
    global i # 
    i += 1 # ，i1
    label.config(text="\t" + str(i) + "")
from tkinter import *
root = Tk() # 
text = Text(root, width=45, height=10, bg="#CAE1FF", relief="solid") # 
# photo = PhotoImage(file='gwc.png') # 
# text.image_create(END, image=photo) # text
text.insert(INSERT, ":\n") # 
text.pack() # ，，
bt = Button(root, text="", command=show, padx=10) # 
text.window_create("2.end", window=bt) # text
label = Label(root, padx=10, text="0") # Label
text.window_create("3.end", window=label) # Labeltext
root.mainloop()