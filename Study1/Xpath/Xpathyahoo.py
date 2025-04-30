import lxml.html
import requests
import lxml

source=requests.get('https://news.yahoo.co.jp/topics/top-picks').content
selector=lxml.html.fromstring(source)
infor=selector.xpath('//div[@class="sc-3ls169-0 dHAJpi"]/text()')
for result in infor:
    print(result)