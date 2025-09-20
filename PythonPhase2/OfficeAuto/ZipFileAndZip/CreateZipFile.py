import zipfile
from zipfile import *

with zipfile.ZipFile('test.zip', 'a',) as zip:
     zip.write('Unzip.py')
