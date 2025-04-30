import lxml
import lxml.html

source = '''
<html>
  <head>
    <title>测试</title>
  </head>
  <body>
    <div class="useful">
      <ul>
        <li class="info">infor1</li>
        <li class="info">information2</li>
        <li class="info">information3</li>
      </ul>
     </div>
     <div class="useless">
       <ul>
         <li class="info">garabe1</li>
         <li class="info">garabe2</li>
       </ul>
     </div>
  </body>
</html>
'''
selecot=lxml.html.fromstring(source)
#info_list=selecot.xpath('//div[@class="useful"]/ul/li/text()')
userful=selecot.xpath('//div[@class="useful"]')
info_list=userful[0].xpath('ul/li/text()')
print(info_list)