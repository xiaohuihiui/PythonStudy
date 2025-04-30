import os
import pandas
import xlwings as xl
##memo
# Table 5-1  PrintOut() Function Parameters
#
# Parameter        Function
# --------------------------------------
# from             # Specifies the starting page for printing. If omitted, prints from the first page
# to               # Specifies the last page for printing. If omitted, prints to the last page
# copies           # Specifies the number of copies to print. If omitted, prints 1 copy
# preview          # Specifies whether to preview before printing. Set to True to show print preview; set to False (default) to print directly
# activeprinter    # Sets the name of the current printer
# printtofile      # Set to True to print to a file. If PrToFileName parameter is not specified, it will prompt the user to input the output filename
# collate          # Set to True to collate copies
# prtofilename     # Specifies the name of the file to print to when PrintToFile is set to True
# ignoreprintareas # Set to True to ignore print areas and print the entire document
##print excel file
file_path='D:\\studybook\\PC\\python\\PythonStudy\\AutoExcelOperation\\excelFile'

file_list=os.listdir(file_path)
print(file_list)
app =xl.App(visible=True,add_book=False)
for f in file_list:
 if f.startswith('~$'):
    continue
 wb=app.books.open(file_path+ "\\" + f) ##attention is "" not ''
 wb.api.PrintOut() ##main
 wb.close()
app.quit()



