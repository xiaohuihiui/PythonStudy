from docx import Document
doc=Document('one.docx')
for paragraph in doc.paragraphs:
    for run in paragraph.runs:
        print(run.text)