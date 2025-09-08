import lxml.html


html1 = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div id="test-1-k">content1</div>
    <div id="test-2-k">content12</div>
    <div id="testfault-k">content13</div>
    <div id="useless">empty</div>
</body>
</html>
'''
#selector=lxml.html.fromstring(html1)
#info=selector.xpath('//div[starts-with(@id,"test")]/text()')
#for detail in info:
   # print(detail)

html2 = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div id="abc-key-x">content1</div>
    <div id="123-key-000">content2</div>
    <div id="haha-key">content3</div>
    <div id="useless">black</div>
</body>
</html>
'''
#selector=lxml.html.fromstring(html2)
# info=selector.xpath('//div[contains(@id,"key")]/text()')
# for detail in info:
#     print(detail)



html3 = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div id="test3">
        aa
        <span id="tiger">
            bb
            <ul>cc
                <li>dd。</li>
            </ul>
            ee
        </span>
        ff。
    </div>
</body>
</html>
'''

selector=lxml.html.fromstring(html3)
# info=selector.xpath('//div[@id="test3"]/text()')
# for detail in info:
#     print(detail)
info=selector.xpath('//div[@id="test3"]')[0]
result=info.xpath('string(.)')
print(result)