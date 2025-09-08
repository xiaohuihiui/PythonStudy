from tkinter import *
from tkinter.ttk import *
import pymysql


db = pymysql.connect(host="localhost", user="root", password="369852", database="mrsoft")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL 查询
cursor.execute("SELECT * FROM books")

# 使用 fetchall() 方法获取所有数据
data = cursor.fetchall()
row = cursor.rowcount

win = Tk()
win.title("查看图书数据信息")

tree = Treeview(win, columns=("num", "name", "category", "price", "publish_time"), show="headings")
tree.pack()

# 设置表格标题
tree.heading("num", text="num")
tree.heading("name", text="name")
tree.heading("category", text="category")
tree.heading("price", text="price")
tree.heading("publish_time", text="publish_time")

# 遍历数据
for i in range(row):

    tree.insert("", END, values=data[i])

db.close()
win.mainloop()