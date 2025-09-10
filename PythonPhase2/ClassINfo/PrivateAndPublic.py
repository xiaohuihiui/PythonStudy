class Car:
    price = 100000  # Defines a class attribute

    def __init__(self, c, w):
        self.color = c  # Defines a public attribute 'color'
        self.__weight = w  # Defines a private attribute '__weight'

# Main program
car1 = Car("Red", 10.5)
car2 = Car("Blue", 11.8)

print(car1.color)  # Accesses the public attribute
print(car1._Car__weight)  # Accesses the private attribute using name mangling
print(car1.__weight)  # This will raise an AttributeError