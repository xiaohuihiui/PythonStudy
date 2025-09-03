with open('test.txt', 'r') as f:
    print(f.readlines())
    f.seek(9)
    print(f.readlines())
    print(f.read(5))
