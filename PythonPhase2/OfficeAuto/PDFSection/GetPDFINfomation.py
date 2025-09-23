from PyPDF2 import *
pdf1=PdfReader(r'C:\studybook\PC\IT.コンサルティング\BookShots_20250923_121650.pdf')
print(len(pdf1.pages))
key=pdf1.metadata
print(key.author)
print(key.title)
print(key.creation_date)
print(pdf1.page_layout)
print(pdf1.page_mode)
print(pdf1.outline)