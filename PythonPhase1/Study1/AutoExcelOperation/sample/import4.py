import xlwings as xw 
import os
path=r'D:\studybook\PC\3_excel\practise'
path_file=os.listdir(path)
print(path_file)
app=xw.App(visible=True,add_book=False)
for i in path_file:
 if os.path.splitext(i)[1]=='.xlsx':
  workbook=app.books.open(path+'\\'+i)