def aa(fun):
     def ww(*args, **kwargs):
         print("start")
         fun(*args, **kwargs)
         print("done")
     return ww
@aa
def dd(x):
    a=[]
    for i in range(x):
        a.append(i)
    print(a)
@aa
def hh(n):
    print(n)

if __name__ == '__main__':
    dd(6)
    print()
    hh('apple')


