import urllib.request
response=urllib.request.urlopen('http://www.yahoo.co.jp')
print(response.read().decode('utf-8'))