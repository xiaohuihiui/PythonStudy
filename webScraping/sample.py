import requests
import re

# html=requests.get('http://exercise.kingname.info/exercise_requests_get.html').content.decode()
# print(html)
# title=re.search('<title>(.*?)<',html,re.S).group(1)
# content=re.findall('<p>(.*?)<',html,re.S)
# content_str='\n'.join(content)
# print(f'title:{title}')
# print(f'content:{content_str}')

data = {'name': 'kingname', 'password': '1234567'}
# formatdata=requests.post('http://exercise.kingname.info/exercise_requests_post', data=data)
formatdata = requests.post('http://exercise.kingname.info/exercise_requests_post', json=data)
print(formatdata.content.decode())