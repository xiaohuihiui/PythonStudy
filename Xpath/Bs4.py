from bs4 import BeautifulSoup
import requests


html=requests.get('http://exercise.kingname.info/exercise_bs_1.html').content.decode()
soup=BeautifulSoup(html, "lxml")
info=soup.find(class_='test')
print(type(info))
print(info)




