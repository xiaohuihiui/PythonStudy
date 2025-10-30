import requests
url = r'http://www.csrc.gov.cn/pub/zjhapp/wz_1/wz_1_1/next_7797_1.json'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)
response.encoding='utf-8'
print(response.text)

