from mimetypes import inited


class Complex:

    def __init__(self, realpart, imagpart):

        self.r = realpart

        self.i = imagpart
        self.b=realpart

x = Complex(3.0, -4.5)

print(x.r, x.i, x.b)

def __dir__(self):
    return self.__dict__.keys()
