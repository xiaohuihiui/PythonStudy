from py7zr import  *

my7=SevenZipFile('Unzip.7z')
my1=my7.getnames()
print(my1)
