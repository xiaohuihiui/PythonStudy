import pdfplumber

pdf=pdfplumber.open(r'C:\studybook\Language\BookShots_20250920_121328.pdf')
info1=pdf.metadata
for key,value in info1.items():
    print(key,':',value)
page=pdf.pages[1]
print()
pdf.close()