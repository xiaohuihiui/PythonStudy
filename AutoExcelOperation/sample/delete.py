import os
import xlwings as  xw
app=xw.App(visible=True,add_book=False)
file_path=r'D:\studybook\PC\3_excel\practise\python'
file_list=os.listdir(file_path)
for file in file_list:
   ws=app.books.open(file_path+'\\'+file)
   sheet_name=ws.sheets
   for i in sheet_name:
      if i=='new customer':
         i.delete()
         ws.save() 
   app.quit()        
          