# "." kin...me
# "*"
# "?"
# "\"
# "\d"
#"()"
import re
#findall
# content = 'is：1234567，is：' \
# '33445566， is：888888，' \
# 'is：999abc999，ee'
# password_list = re.findall('：(.*?)，', content)
# name_list = re.findall('ps(.*?)，', content)
# print('{}'.format(password_list))
# print('{}'.format(name_list))


# big_string_mutil = '''
#  i am  kingname,password:123
#  45678, '''
# password_findall_no_flag = re.findall('password:(.*?),', big_string_mutil)
# password_findall_flag = re.findall('password:(.*?),', big_string_mutil, re.S)
# print('not use flag：{}'.format(password_findall_no_flag))
# print('use：{}'.format(password_findall_flag))

#search()
# content = 'my password is：1234567，QQ password is：33445566， cread card password is：888888，Github passsword is：999abc999，help　me to remember them'
# password_search = re.search('passsword is：(.*?)，', content)
# password_search_not_find = re.search('xxxxxxxx xx：(.*?)，', content)
# print(password_search)
# print(password_search.group())
# print(password_search.group(0))
# print(password_search.group(1))
# print(password_search_not_find)

# account_content = 'Account is:kingname, password is:12345678, QQAccount is:99999, password is:890abcd, credit card:000001, password is:654321, GithubAccount is:99999@qq.com, password is:7777love8888, remeber them'
# account_password = re.search('Account is:(.*?), password is:(.*?),', account_content)
# print('first content: {}'.format(account_password.group(1)))
# print('second content: {}'.format(account_password.group(2)))


# big_small_text = '''
# username:
# name: a
# name: b
# name: c
# notuse:
# name: d
# name: e
# '''
# user = re.findall('name: (.*?)\n', big_small_text)
# print(user)

# user_big = re.findall('username(.*?)notuse', big_small_text, re.S)
# print('user_big : {}'.format(user_big))

# user_useful = re.findall('name: (.*?)\n', user_big[0])
# print('username{}'.format(user_useful))


html = '''<div class="tail-info">client</div>
<div class="tail-info">2017-01-01 13:45:00</div>
'''

result_1 = re.findall('tail-info">(.*?)<', html)
result_2 = re.findall('tail-info">2017(.*?)<', html)
result_3 = re.findall('tail-info">(2017.*?)<', html)
print('result_1：{}'.format(result_1))
print('result_2：{}'.format(result_2))
print('result_3：{}'.format(result_3))
