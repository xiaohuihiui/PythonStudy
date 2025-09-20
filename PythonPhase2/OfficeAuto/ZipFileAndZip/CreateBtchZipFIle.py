import os
import zipfile

os.getcwd()
for outer in os.listdir('.\\'):
    print(outer)
    with zipfile.ZipFile(outer+'.zip', 'a',) as zip:
        zip.write(outer)
        print(outer)


