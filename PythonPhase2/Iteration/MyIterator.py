class MyIterator(object):
    def __init__(self, a=3, b=300):
        self.a = a
        self.b = b
    def __iter__(self):
        return self
    def __next__(self):
        if self.a and self.b !=1:
            self.a=self.a-1
            if self.a<=self.b:
                return self.b
            else:
                raise StopIteration
        else:
            raise StopIteration

if __name__ == '__main__':
    it = MyIterator()
    for x in it:
        print(x)