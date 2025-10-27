import requests
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get('https://yahoo.co.jp', headers=headers)
print(response.text)
print(response.headers)
print(response.cookies)
print(response.encoding)
print(response.connection)
dataauth=('a','b')
proxies={'http':'http://127.0.0.1:8080','https':'http://127.0.4.1:8080'}
cert=('/value/value.cert','/value/key')
response = requests.get('https://yahoo.co.jp',files={'file':open('test.jpg','rb')},auth=dataauth,timeout=10,allow_redirects=False,proxies={'http':'http://127.0.0.1:8080'},verify=False,stream=False,cert=None,headers={'User-Agent': 'Mozilla/5.0'})
print(response.text)
