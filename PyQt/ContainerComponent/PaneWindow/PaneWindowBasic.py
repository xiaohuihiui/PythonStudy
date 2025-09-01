# from tkinter import *
#
# panewindow = PanedWindow(sashrelief=SUNKEN, background="#1DF5DF", width=200)
# panewindow.pack()  # panewindow
# btn1 = Button(panewindow, text='')
# panewindow.add(btn1)
# btn2 = Button(panewindow, text='')
# panewindow.add(btn2)
# mainloop()

from tkinter import *

panewindow = PanedWindow(sashrelief=SUNKEN, background="#1DF5DF", width=200)
panewindow.pack()  # panewindow

btn1 = Button(panewindow, text="", state="disabled")
panewindow.add(btn1)

btn2 = Button(panewindow, text="", state="disabled")
panewindow.add(btn2)

mainloop()
