from tkinter import *
import os,time

def show1():
    a=os.stat('test4.txt')
    text.insert(INSERT,'File size: '+str(a.st_size)+' bytes')
    text.insert(INSERT, '\nFile path: ' + os.path.abspath('test.txt'))
    text.insert(INSERT, '\nLast access time: ' + time.strftime('%Y-%m-%d %H:%M:%S',
time.localtime(a.st_atime)))
    text.insert(INSERT, '\nLast modified time: ' + time.strftime('%Y-%m-%d %H:%M:%S',
time.localtime(a.st_mtime)))

win=Tk()
Button(win,text='Display Info',command=show1).pack(pady=10)
text=Text(win,font=14,width=60,height=10)
text.pack(padx=10)
win.mainloop()