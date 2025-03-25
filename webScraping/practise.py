import requests
import re
import os
from multiprocessing.dummy import Pool

start_url='http://www.kanunu8.com/book3/6879/'

def get_resource(html):
    """
    get resource form web
    url:resource location
    return:original resouce   
    """
    html=requests.get(url)
    return html.content.decode('gbk')

print(get_resource(url))


def get_toc(html):
      
 toc_url_list=[]
 toc_block=re.findall('正文(.*?)</tbody>',html,re.S)
 toc_url=re.findall('href="(.*?)"',toc_block,re.S)
 for  url in toc_url:
     toc_url_list.append(start_url+url)
     print(toc_url_list)
 return toc_url_list


def get_article(html):




    
    return 



def get_top(html):

       """
    get each parc link and return a list form
    param_html:resource location
    return:each artical link   
    """
       