'''
2.4
class Flower:

    def __init__(self, name=None, petals=None, price=None):
        self.name = name
        self.petals = petals
        self.price = price

    def set_name(self, name):
        self.name = str(name)

    def set_number(self, petals):
        self.petals = int(petals)

    def set_price(self, price):
        self.price = float(price)

    def get_name(self):
        if self.name is None:
            return("It has not been setup")
        else:
            return self.name

    def get_number(self):
        if self.petals is None:
            return("It has not been setup")
        else:
            return self.petals

    def get_price(self):
        if self.price is None:l
            return ("It has not been setup")
        else:
            return self.price

Tulips = Flower('Tulip', 4, 9.99)
print(Tulips.get_number(),Tulips.get_price())

Rose = Flower()
Rose.set_name('Rose')、、、
print(Rose.get_name())

'''

#2.9


class Vector:
    def __init__(self, d):
        self.d = d
        #self.coords = d * [0]
        if type(d) is list:
            self.coords = d
        else:
            if type(d) is int:
                self.coords = d * [0]


    def __len__(self):
        return len(self.coords)

    def __setitem__(self, j, val):
        self.coords[j] = val

    def __getitem__(self, j):
        return self.coords[j]

    '''
    def set_vec(self, j, val):
        self.coords[j] = val
    '''

    def __sub__(self, other):
        if len(self) != len(other):
            return "dimensions must agree"
        else:
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] - other[j]
            return result

    def __add__(self, other):
        if len(self) != len(other):
            return "WRONG"
        else:
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i] + other[i]
            return result

    def __neg__(self):
        result = Vector(len(self))
        for k in range(len(self)):
            result[k] = 0 - self[k]
        return result

    def __str__(self):
        return '<' + str(self.coords)[1:-1] + '>'


a = Vector(4)
b = Vector(4)
a.coords = [1,2,3,4]
b.coords = [2,3,4,5]

d = a + [1,2,3,4]
print(d)
e = Vector([1,2,3,4]) + a
print(e)

print(a.__neg__())
print(a)
c = a-b
d = a+b
print(c)
print(d)

for j in b:
    print("PRINTING: %s"%j)













