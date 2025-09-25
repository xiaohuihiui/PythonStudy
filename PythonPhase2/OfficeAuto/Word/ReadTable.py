from docx import Document
doc=Document('one.docx')
for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            print(cell.text)