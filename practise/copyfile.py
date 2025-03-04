import os
import xlwings as  xw
app=xw.App(visible=True,add_book=False)
file_path=r'D:\studybook\PC\3_excel\practise\python'
file_list=os.listdir(file_path)
print(file_list)
wobook1=app.books.open('d:\\studybook\\PC\\3_excel\\practise\\same.xlsx')
sheets=wobook1.sheets
print(sheets)
for i in file_list:
    if os.path.splitext(i)[1]=='.xlsx' or os.path.splitext(i)[1]=='.xls':
        wobook2=app.books.open(file_path+'\\'+i)
        for x  in sheets:
             copy=x.range("A1").expand('table').value
             name1=x.name
             wobook2.sheets.add(name=name1,after=len(wobook2.sheets))
             wobook2.sheets[name1].range("A1").value=copy
             wobook2.save()
             wobook2.close()
    app.quit()