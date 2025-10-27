import urllib.request
url=r'https://news.web.nhk/newsweb/pl/news-nwa-latest-nationwide'
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'Referer': 'https://news.web.nhk/newsweb/pl/news-nwa-latest-nationwide',
    'Connection': 'keep-alive'
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
