
# 删除MySQL数据
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import pymysql
db = pymysql.connect(host="localhost",user="root",password="369852",database="mrsoft")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
def showinfo():

    cursor.execute("SELECT * FROM books")
    # 使用 fetchone()
    data = cursor.fetchall()
    row = cursor.rowcount #
    item_num=len(tree.get_children())
    if item_num>0:
        for item in tree.get_children():
            tree.delete(item)
    for i in range(row): #
        tree.insert("", END, values=data[i])
def dele():
    if tree.focus()=="":
        showerror("err","请选择要删除的数据")
    else:
        boo=askyesno("删除记录","删除后记录无法找回,确定要继续吗")
        if boo:
            db.ping(reconnect=True) # 如果数据库断开连接就重新进行连接
            a=tree.focus() # 获取已选中的行
            id_num = tree.item(a)["values"][0] # 表格中的第一列,即数据库中的数据的ID
            cursor.execute('DELETE FROM books WHERE id ='+str(id_num))
            showinfo()
            db.close() # 关闭数据库连接
win=Tk()
win.title("info")
tree=Treeview(win,columns=("num","name","category","price","publish_time"),show="headings",height=4)
tree.pack()
Button(win,text="delete",command=dele).pack()
tree.heading("num",text="num")
tree.heading("name",text="name")
tree.heading("category",text="category")
tree.heading("price",text="price")
tree.heading("publish_time",text="publish_time")
showinfo()
win.mainloop()
