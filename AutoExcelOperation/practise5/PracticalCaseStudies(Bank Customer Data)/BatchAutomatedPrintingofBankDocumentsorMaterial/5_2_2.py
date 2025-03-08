import os
import pandas as pd
import xlwings as xl
file_path='D:\\studybook\\PC\\excelFile'
file_list=os.listdir(file_path)
app =xl.App(visible=True,add_book=False)
wb=app.books.open(file_path+ "\\cutomerNo.xlsx")
sht=wb.sheets('No')
data=sht.range('A1').expand('table').value

wb2=app.books.open(file_path+ "\\dataofBank.xlsx")
sht2=wb2.sheets('allData')
data2=sht2.range('A1').options(pd.DataFrame,header=1,index=False,expand='table').value
pd_data = pd.DataFrame()
for i  in data:#main
 data_sort=data2[data2['No']==i]#main
 pd_data = pd.concat([pd_data, data_sort])#main
 print(pd_data)
new_wb=xl.books.add() 
new_sh=new_wb.sheets.add('new')
new_sh.range('A1').options(index=False).value=pd_data
new_sh.autofit()
new_wb.save('D:\\studybook\\PC\\excelFile\\new2.xlsx')
new_wb.close()
wb.close()
wb2.close()
app.quit() 