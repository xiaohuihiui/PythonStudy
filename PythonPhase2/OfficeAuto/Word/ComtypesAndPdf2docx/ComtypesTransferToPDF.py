from PyPDF2 import PdfFileWriter
from comtypes.client import CreateObject

word=CreateObject('Word.Application')
word_path='sample.docx'
pdf_path='sample.pdf'
doc=word.Documents.Open(word_path)
doc.SaveAs(pdf_path,FileFormat=PdfFileWriter())
doc.Close()
word.Quit()
