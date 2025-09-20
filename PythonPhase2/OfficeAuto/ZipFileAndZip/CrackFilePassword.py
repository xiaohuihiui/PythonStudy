from zipfile import ZipFile
import itertools
import os

os.chdir('D:\\test7\\demo7\\')
filename="text.zip"
# Create a decompression function with file name and password as parameters.
# And use the try...except statement to prevent the program from being interrupted by an error.
def uncompress(zip_name,pass_word):
    try:
        with ZipFile(zip_name) as myzip:
            myzip.extractall(pwd=pass_word.encode("utf-8"))
        return True
    except:
        return False

# chars is the set of possible password characters
#chars="abcdefghijklmnopqrstuvwxyz0123456789"
chars="01234" # Use a small character set for demonstration purposes
for code in itertools.permutations(chars,4):
    password= ''.join(code)
    print(password)
    result=uncompress(filename,password)
    if result==False:
        print('fail',password)
    else:
        print('success',password)
        break