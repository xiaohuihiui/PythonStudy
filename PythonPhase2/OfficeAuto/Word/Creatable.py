from docx import Document
doc=Document()
list1=[['1','2','3'],
       ['1','2','3'],
       ['1','2','3'],
       ['1','2','3'],
       ['1','2','3'],]

table=doc.add_table(rows=5, cols=5)
for i in range(5):
    cell_list=table.rows[i].cells
    for j in range(3):
        cell_list[j].text=list1[i][j]
doc.save('output.docx')