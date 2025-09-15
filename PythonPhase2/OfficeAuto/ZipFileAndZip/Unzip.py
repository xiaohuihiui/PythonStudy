import os
from zipfile import *
with ZipFile('file.zip') as myzip:
    print(myzip.namelist())
    myzip.extractall()