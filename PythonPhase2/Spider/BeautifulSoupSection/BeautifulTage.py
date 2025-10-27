from bs4 import BeautifulSoup
soup = BeautifulSoup('<a class="bold" length="fdd">Extremely body</a>',)
tag=soup.a
#infromation about tag
# print(type(tag))
# print(tag.name)
# print(tag['class'])
# print(tag['length'])
# print(tag.attrs)
#update tag
# tag['class']='verybold'
# tag['length']='fdd'
# tag['id']='E'
# print(tag)
#del tag
# del tag['class']
# del tag['length']
# print(tag)
print(tag.string)
print(type(tag.string))
tag.string.replace_with("No longer bold")
print(tag.string)


