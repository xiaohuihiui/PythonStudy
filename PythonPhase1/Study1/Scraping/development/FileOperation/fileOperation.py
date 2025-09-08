import os
# file_path = r"D:\studybook\PC\python\PythonStudy\Scraping\development\FileOperation\text.txt" 
# with open(file_path,encoding='utf-8') as f:
#   content=f.read()
file_path2 = r"D:\studybook\PC\python\PythonStudy\Scraping\development\FileOperation\text2.txt" 
with open(file_path2,'w',encoding='utf-8') as f2:
  f2.write('hi')
  f2.writelines(['1','\n\n','2','\n\n','3'])
  f2.write('fff')
  f2.write('\n-----\n')
  f2.write('fff22')
  
