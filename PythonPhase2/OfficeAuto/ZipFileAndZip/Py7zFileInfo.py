from py7zr import *
my7 = SevenZipFile('test.7z')
my2 = my7.list()
for item in my2:
    print(item.filename,item.archivable,item.is_directory)
my7.close()


