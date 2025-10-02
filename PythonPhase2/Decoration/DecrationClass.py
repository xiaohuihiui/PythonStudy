def aa(innerClass):
    class myclass:
        def __init__(self,z=0):

            self.z=0
            self.wrapper=myclass()
        def position(self):
            print('dsd')
            self.wrapper.position()
            print(self.z)
    return innerClass
@aa
class coordiation:
    def __init__(self,x=100,y=100):
        self.x=x
        self.y=y
    def position(self):
        print(self.x)
        print(self.y)

if __name__ == '__main__':
    cc = coordiation()
    cc.position()