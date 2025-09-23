from py7zr import *
with SevenZipFile('test.7z','a') as my7:
    my7.write('file.svg')
    print('added one file')