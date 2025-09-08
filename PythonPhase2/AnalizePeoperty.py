class Person:
    num=1    # Class attribute

    def __init__(self, str, n):    # Constructor function
        self.name = str    # Instance attribute
        self.age = n

    def SayHello(self):    # Member function
        print("Hello!")

    def PrintName(self):    # Member function
        print("Name: ", self.name, "Age: ", self.age)

    def PrintNum(self):    # Member function
        print(Person.num)    # Since it's a class attribute,
                             # you can write it without self.num

# Main program
P1 = Person("Xiaominjie", 42)
P2 = Person("Wanglin", 36)
P1.PrintName()
P2.PrintName()