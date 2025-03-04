import xlwings as xw


for i in range(1, 10):
    app=xw.App(visible=False, add_book=False)
    workbook=app.books.add()
    workbook.save(r'test'+str(i)+'.xlsx')
    workbook.close()
    app.quit()