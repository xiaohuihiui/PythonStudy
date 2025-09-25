from  PyPDF2 import *

mer1=PdfFileMerger()
pdf1=PdfReader('sample1.pdf')
mer1.merge(position=1,fileobj=pdf1,page_number=1)
mer1.merge(position=2,fileobj=pdf1,page_number=2)
mer1.write('mer1.pdf')
pdf2=PdfReader('sample2.pdf')
print(pdf2.metadata.author)
 