import xlwt

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('Sheet1')
worksheet.write(0, 0, 1234.56,)
worksheet.write(1, 3, 'we just word')
workbook.save('test.xls')
