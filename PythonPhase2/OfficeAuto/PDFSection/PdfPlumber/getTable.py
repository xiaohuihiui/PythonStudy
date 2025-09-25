import pdfplumber

pdf=pdfplumber.open(r'C:\studybook\Language\BookShots_20250920_121328.pdf')
page=pdf.pages[75]
#for row in page.extract_tables():
for row in page.extract_table():
    print(row)
    print(row[0])