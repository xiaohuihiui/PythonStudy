from docx import Document
doc=Document('one.docx')
for paragraph in doc.paragraphs:
    for run in paragraph.runs:
        run.font.bold=True
        run.bold.italic=True
        run.font.underline=True
        run.font.strike=True
        run.font.shadow=True
        run.font.color.rgb=0xFFFFFF
doc.save('output.docx')
