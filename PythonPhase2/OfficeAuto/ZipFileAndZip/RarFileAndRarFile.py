from rarfile import *
with RarFile('Unzip.rar') as myrar:
    print(myrar.namelist())
    print(myrar.extract())
    #print(myrar.extractall())