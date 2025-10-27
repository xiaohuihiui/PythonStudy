import urllib.request
import urllib.parse
url = r'https://qq.ip138.com/weather/search.asp'
headers = {
'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
 'Referer':'https://qq.ip138.com/weather/search.asp',
 'Connection':'keep-alive'
}

data=urllib.parse.urlencode({'k':'湖南','Submit':'提交'}).encode('utf-8')

request = urllib.request.Request(url,headers=headers,data=data)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
