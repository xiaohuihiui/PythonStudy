from PyPDF2 import *
merger = PdfMerger()
pdf1=PdfReader('')
pdf2=PdfReader('')
merger.append(pdf1)
merger.append(pdf2)
merger.write('file')