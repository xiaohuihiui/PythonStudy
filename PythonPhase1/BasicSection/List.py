from xmlrpc.client import escape

list=["a","b","c","d"]
list2=["e","f","g","h"]
# print(list)##insert value
# list.insert(0,"aa")
# print(list)
# list.append("bb")##insert value by end
# print(list)
# list[1]="cc" #change value
# print(list)
# list.remove('cc')#delete list value
# print(list)
# list.pop(1)#delete list value
# print(list)
# list.reverse()
# print(list)
# b=list.copy()
# print(b)
# print(list+list2)
# print(list*2)
#--------------------------------------------------------------------------------
# list escape
# print(list[0:13])
# print(list[0:])
# print(list[:])
# print(list[::-1])
# print(list[::2])
# print(list[1::2])
# print(list[-1::2])
# list3=[]
# for item in range(10):
#     list3.append(item*2)
# print(list3)

# list4=[i**2 for i in range(10)]
# print(list4)

for index,item in enumerate(list):
    print(index,item)