from PyPDF2 import PdfReader, PdfWriter
reader=PdfReader('sample.pdf',password='1234')
reader.decrypt('1234')