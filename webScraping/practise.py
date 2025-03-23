import requests
import re
import os
from multiprocessing.dummy import Pool

url='http://www.kanunu8.com/book3/6879/'

def get_resource(url):
    """
    get resource form web
    url:resource location
    return:original resouce   
    """
    html=requests.get(url)
    return html.content.decode('gbk')

print(get_resource(url))



def get_top(html):

       """
    get each parc link and return a list form
    param_html:resource location
    return:each artical link   
    """
       