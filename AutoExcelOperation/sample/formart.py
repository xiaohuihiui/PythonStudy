import os
import xlwings as  xw
app=xw.App(visible=True,add_book=False)
file_path=r'D:\studybook\PC\3_excel\practise\python'
file_list=os.listdir(file_path)
print(file_list)
for i in file_list:
    if os.path.splitext(i)[1]=='.xlsx' or os.path.splitext(i)[1]=='.xls':
        wobook2=app.books.open(file_path+'\\'+i)
        sheets2=wobook2.sheets
        for x in sheets2: 
          print(x.api)
          x.range('A1:A8').api.NumberFormat='hh:mm'
          x.range('A1:A8').color = (255, 255, 255)
          x.range('A1:A8').api.Interior.Color = 65535
        wobook2.save()
    wobook2.close()               
app.quit()       