import os
from zipfile import *
zipFile = ZipFile('file.zip')
name=zipFile.namelist()
info=zipFile.infolist()
print(name)
for item in info:
    print(item)


zipFile.close()