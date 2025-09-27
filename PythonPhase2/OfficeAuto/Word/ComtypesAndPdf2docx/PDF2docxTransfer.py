from pdf2docx import Converter

word_path='sample.docx'
pdf_path='sample.pdf'
cv=Converter(pdf_path)
cv.convert(word_path,start=0,end=10)
cv.close()