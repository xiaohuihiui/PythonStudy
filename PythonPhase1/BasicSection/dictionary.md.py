dic={1:2,2:3,3:4,4:5,5:6}
# print(dic[1])
# dic[6]=7
# print(dic)
# dic.setdefault(8,9)
# print(dic)
# dic.setdefault(1,3)
# print(dic)
# dic[1]=1
# print(dic)
# dele=dic.pop(1)
# print(dele)
# print(dic)
# for key,value in dic.items():
#     print(key,value)
# print("-------------------------------------")
# for key in dic.keys():
#     print(key)
# print("-------------------------------------------")
# for value in dic.values():
#     print(value)

#dictionary include dictionary
# a={"a":1,"b":2,"c":3,"d":4}
# b={"a":2,"b":3,"c":4,"d":5}
# c={"a":3,"b":4,"c":5,"d":6}
# info={"one":a,"two":b,"three":c}
# print(info)
# for key,value in info.items():
#     total=0
#     total+=sum(value.values())
#     print(key,total)
#dictionary include list
# a=[1,2,3,4]
# b=[5,6,7]
# c=[8,9,10]
# info={"one":a,"two":b,"three":c},
# print(info)
# for key,value in info.items():
#     total=0
#     total+=sum(value.values())
#     print(key,total)

# list include dictionary
a={"a":1,"b":2,"c":3,"d":4}
b={"a":2,"b":3,"c":4,"d":5}
c={"a":3,"b":4,"c":5,"d":6}
list=[a,b,c]
for name in list:
    print(name)


