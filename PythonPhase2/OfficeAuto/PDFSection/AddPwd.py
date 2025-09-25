from PyPDF2 import PdfReader, PdfWriter


readers=PdfReader('sample2.pdf')

writer=PdfWriter()
content=readers.getPage(0).get_contents()
writer.encrypt('1234')
writer.write(content.get(1))
