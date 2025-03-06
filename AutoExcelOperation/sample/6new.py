import os
import pandas
import xlwings as  xa

app=xa.App(visible=True,add_book=False)
file_path=r'D:\studybook\PC\3_excel\practise\python'
files=os.listdir(file_path)
for file in files:
    print(file)
    ws=app.books.open(file_path + '\\'+ file)
    sheet_name=ws.sheets
    list_name=[]
    for i in sheet_name:
      list_name.append(i.name)  
    if 'new customer2' not in list_name:  
     ws.sheets.add('new customer2')
     ws.save(file_path + '\\'+ file)
     ws.close()
    app.quit() 