import os
import pandas as pd
import xlwings as xl
file_path='D:\\studybook\\PC\\excelFile'
file_list=os.listdir(file_path)
app =xl.App(visible=True,add_book=False)
wb=app.books.open(file_path+ "\\amount.xlsx")
column=['amountfield','leaveamount']
datalist=[]
for i in wb.sheets:
 data=i.range("A1").options(pd.DataFrame,header=1,index=False,expand='table').value
 #if data is not None and 'payment' in data.columns:
    #data_row = data[data['payment'] == 'card']
    #datalist.append(data_row)  

combined_data = pd.concat(datalist, ignore_index=True)     
new_wb=xl.books.add() 
new_sh=new_wb.sheets.add('new')
new_sh.range('D:D').api.NumberFormat = 'YYYY/mm/dd'
new_sh.range('F:F').api.NumberFormat = '0.00'
new_sh.range('A1').options(pd.DataFrame,header=1,index=False,expand='table').value=combined_data
new_sh.autofit()
new_wb.save('D:\\studybook\\PC\\excelFile\\new4.xlsx')
new_wb.close()
wb.close()
new_wb.close()
app.quit() 