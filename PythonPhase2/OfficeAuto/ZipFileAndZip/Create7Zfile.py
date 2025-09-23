from py7zr import SevenZipFile
with SevenZipFile('test1.7z','w') as my7:
    my7.write('file.svg')
    print('added one file')