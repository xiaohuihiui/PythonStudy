import lxml.html
import requests
import lxml
import redis

client=redis.StrictRedis()
# client.lpush('chapter_6',123)
# value=client.lpop('chapter_6')
# print(value)

# source = requests.get('http://dongyeguiwu.zuopinj.com/5525').content
# selector = lxml.html.fromstring(source)

# url_list = selector.xpath('//div[@class="book_list"]/ul/li/a/@href')
# for url in url_list:
#     client.lpush('url_queue', url)
value=client.lpop('url_queue')
print(value)