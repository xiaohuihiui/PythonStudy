import xlwings as xw

namenames=['aa','bb','dd','dd','ee','ff','gg','hh','ii']

names=['aa','bb','cc','dd','ee']
for i in range(5):
    app=xw.App(visible=False, add_book=False)
    workbook=app.books.add()
    workbook.save(r'test'+names[i]+'.xlsx')
    workbook.close()
    app.quit()