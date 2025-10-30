import xlrd
from xlutils import copy

write_book='test.xls'
wb = xlrd.open_workbook(write_book)
file=copy.copy(wb)
sheet=file.get_sheet('Sheet1')
sheet.write(0,3,"add new conte" )
file.save(write_book)
