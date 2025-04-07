import requests

html='https://exercise.kingname.info/ajax_1_backend'

source1=requests.post(html,json={'name':'aa','age':24}).content.decode()
source2=requests.post(html,json={'name':'bb','age':25}).content.decode()
print(source1)
print(source2)