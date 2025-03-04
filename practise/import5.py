import xlwings as xw
import os
path=r'D:\studybook\PC\3_excel\practise\test1.xlsx'
path1=r'D:\studybook\PC\3_excel\practise\test3.xlsx'
app=xw.App(visible=True,add_book=False)
work=app.books.open(path)
sheet=work.sheets
for i in sheet:
 i.name=i.name.replace('a','b')
 work.save(path1)
 app.quit()