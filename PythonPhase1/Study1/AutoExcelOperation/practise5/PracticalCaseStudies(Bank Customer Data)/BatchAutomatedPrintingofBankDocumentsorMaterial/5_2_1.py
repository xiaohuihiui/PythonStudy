import os
import pandas as pd
import xlwings as xl
file_path='D:\\studybook\\PC\\excelFile'
file_list=os.listdir(file_path)
app =xl.App(visible=True,add_book=False)
for f in file_list:
 if f.startswith('~$'):
    continue
 wb=app.books.open(file_path+ "\\" + f)
 print(file_path+ "\\" + f)
 sht=wb.sheets('data')
 dat_pd=sht.range('A1').options(pd.DataFrame,header=1,index=False,expand='table').value##main
 pd_sort=dat_pd[dat_pd['TYPE']=='dealy']
 new_wb=xl.books.add()
 new_sh=new_wb.sheets.add('delay')
 new_sh.range('A1').options(index=False).value=pd_sort
 new_sh.autofit()
 new_wb.save('D:\\studybook\\PC\\excelFile\\new.xlsx')
 new_wb.close()
 wb.close()
app.quit() 
