import os
import pandas as aw
file_path=r'D:\studybook\PC\3_excel\practise\python'
files=os.listdir(file_path)
for file in files:
 if file.startswith('~$'):
    continue
 new_name=file.replace('test','change')
 old_path=os.path.join(file_path,file)
 new_path=os.path.join(file_path,new_name)
 os.rename(old_path,new_path)



