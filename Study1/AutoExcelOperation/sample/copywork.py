import os
import xlwings as  xw
app=xw.App(visible=True,add_book=False)
file_path=r'D:\studybook\PC\3_excel\practise\python'
file_list=os.listdir(file_path)
print(file_list)
wobook1=app.books.open('d:\\studybook\\PC\\3_excel\\practise\\same.xlsx')
sheets=wobook1.sheets['bb']
copy=sheets.range('B2:F20').expand('table').value
for i in file_list:
    if os.path.splitext(i)[1]=='.xlsx' or os.path.splitext(i)[1]=='.xls':
        wobook2=app.books.open(file_path+'\\'+i)
        sheets2=wobook2.sheets
        for x in sheets2:
            if x.name=='Sheet1':
                wobook2.sheets[x.name].range('B12').value=copy
        wobook2.save()
    wobook2.close()
wobook1.close()                
app.quit()       