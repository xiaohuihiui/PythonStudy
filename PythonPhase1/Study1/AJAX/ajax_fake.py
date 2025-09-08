import json
import re
import requests
import lxml

import json
import requests
import re

url = 'http://exercise.kingname.info/exercise_ajax_2.html'
html = requests.get(url).content.decode()

code_json = re.search("secret = '(.*?)'", html, re.S).group(1)
code_dict = json.loads(code_json)
print(code_dict['code'])

# source='{"code": "\u884c\u52a8\u4ee3\u53f7\uff1a\u5929\u738b\u76d6\u5730\u864e"}'
# resource=json.loads(source)
# print(resource)