import xlrd
workbook = xlrd.open_workbook('test.xls')
sheet=workbook.sheets()[0]
count=sheet.nrows
print(count)
row=sheet.ncols
print(row)
try:
    row_value=sheet.row_values(0)
    print(row_value)
    column_value=sheet.col_values(0)
    print(column_value)
    cell=sheet.cell(0,0).value
    print(cell)
    cell=sheet.cell(3,0).value
    print(cell)
except Exception as e:
    print(e)