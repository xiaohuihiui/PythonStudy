from py7zr import SevenZipFile
with SevenZipFile('test2.7z','w',password='1234') as my7:
    my7.write('file.svg')
    print('added one file')