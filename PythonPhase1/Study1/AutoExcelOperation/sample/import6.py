import xlwings as xw
import os
path=r'D:\studybook\PC\3_excel\practise'
app=xw.App(visible=True,add_book=False)
path_file=os.listdir(path)
print(path)
for i  in path_file:
 if os.path.splitext(i)[1]=='.xlsx':
  print(i)
  work=app.books.open(path+'\\'+i)
  worksheet=work.sheets
  for i in worksheet:
    i.name=i.name.replace('sheet1','change')
  work.save()  
  app.quit()

