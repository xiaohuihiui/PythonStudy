import os
import pandas as pd
import xlwings as xl
file_path='D:\\studybook\\PC\\excelFile'
file_list=os.listdir(file_path)
app =xl.App(visible=True,add_book=False)
wb=app.books.open(file_path+ "\\customerInfo.xlsx")
sht=wb.sheets('No')
dataName=sht.range('A1').expand('down').value
dataCode=sht.range('B1').expand('down').value

wb2=app.books.open(file_path+ "\\form.xlsx")
sht2=wb2.sheets('No')
data2=sht2.range('A1').options(pd.DataFrame,header=1,index=False,expand='table').value
for i  in range(5):
 dataNum=dataName.index(data2['name'][i])
 sht2.range('B'+str(i+2)).value=dataCode[dataNum]
 sht2.autofit()
 print(dataCode[dataNum])
wb2.save()
wb.close()
wb2.close()
app.quit() 