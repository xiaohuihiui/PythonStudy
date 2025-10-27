import requests
response = requests.get('http://www.yahoo.co.jp')
print(response.text)
print(response.status_code)
print(response.headers)
print(response.cookies)
print(response.content)
