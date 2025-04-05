from bs4 import BeautifulSoup
import requests
import re


html=requests.get('http://exercise.kingname.info/exercise_bs_1.html').content.decode()
soup=BeautifulSoup(html, "lxml")
# info=soup.find(class_='test')
# print(type(info))
# print(info)
# info=soup.find(class_='useful')
# info2=info.find_all('li')
# for result in info2:
#     print(result.string)
# info=soup.find(class_='useful')
# #info2=info.find_all(text=re.compile('我需要'))
# info2=info.find_all(class_=re.compile('iam'))
# for result in info2:
#     print(result.string)    
info=soup.find(class_='useless')
info2=info.find_all('li')
for result in info2:
    print(result['class'])



