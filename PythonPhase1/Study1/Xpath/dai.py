import lxml.html
import requests
from bs4 import BeautifulSoup
import  re
import lxml
import csv

url='https://search.damai.cn/search.htm'
source=requests.get(url).content
selector=lxml.html.fromstring(source)
listitem=[]
itemlist=selector.xpath('//div[@class="search-factor"]/text()')
for item in  itemlist:
     name=item.xpath('path')
     price=item.xpath('path')
     place=item.xpath('path')
     time=item.xpath('path')
     description=item.xpath('path')
     url=item.xpath('path')
     total={'name':name[0] if name else '', 
            'price':price[0] if name else ''}
     listitem.append(total)

with open('result.csv','w',encoding='utf-8') as f:
     write=csv.DictWriter(f,fieldnames=['name',
                                         'name',
                                         'name',
                                         'name',
                                         'name',
                                         'name',])
     write.writeheader()
     write.writerows(listitem)