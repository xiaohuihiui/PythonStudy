from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import pymysql
# 打开数据库连接，参数1:主机名或IP；参数2:用户名；参数3:密码；参数4:数据库名称
db = pymysql.connect(host="localhost",user="root",password="369852",database="mrsoft")
cursor = db.cursor()


def showinfo1():
    cursor.execute('SELECT * FROM books') # 先获取所有数据
    data = cursor.fetchall()
    row = cursor.rowcount # 获取数据条数
    item_num = len(tree.get_children())
    if item_num > 0:
        for item in tree.get_children():
            tree.delete(item)
    # 遍历数据
    for i in range(row):
        tree.insert("", END, values=data[i]) # 将获取的数据显示在表格中
def addInfo():
    db.ping(reconnect=True) # 如果数据库断开连接就重新进行连接
    entry_text = []
    # print(data[0][3])
    for i in entry_box:
        if i.get()=="":
            showerror("错误","请完善信息")
            return False
        else:
            entry_text.append(i.get())
    # 向MySQL中增加数据
    cursor.execute("insert into books(name, category, price, publish_time) values (%s,%s,%s,%s)", entry_text)
    # 清空文本框中的内容
    for i in entry_box:
        i.delete(0,END)
    entry_text = []
    showinfo1()
win = Tk()
win.title("添加图书数据信息")
column_title=("num", "name", "category", "price", "publish_time")
column_heading=("序列", "书名", "类别", "价格", "出版时间")
entry_box=[]
for i in range(1,len(column_heading)):
    Label(win,text=column_heading[i]).grid(row=0,column=(i*2-2))
    entry=Entry(win)
    entry.grid(row=0, column=(i*2-1))
    entry_box.append(entry)
tree = Treeview(win, columns=column_title, show="headings", height=5)
tree.grid(row=1, column=0, columnspan=9)
for index in range(len(column_title)):
    tree.heading(column_title[index],text=column_heading[index])
    tree.column(column_title[index], width=160)

Button(win, text="添加", command=addInfo).grid(row=0, column=8)
showinfo1()
db.close() # 关闭数据库连接
win.mainloop()

