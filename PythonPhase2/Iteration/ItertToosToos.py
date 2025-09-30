import itertools
#ns=itertools.count(10)
#ns=itertools.cycle(['Alice', 'Bob', 'Charlie', 'David'])
ns=itertools.repeat(['Alice', 'Bob', 'Charlie', 'David'],5)
for n in ns:
    print(n)
    print('')