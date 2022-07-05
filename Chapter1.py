'''class MyInfo:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myinfo(self):
        print("My name is: " + self.name)
        print("My age is: " + str(self.age))

x = MyInfo("John", 30)
x.myinfo()
'''

'''
class CreditCard:
    def __init__(self, user, bank, acnt, lmt):
        self.user = user
        self.bank = bank
        self.acnt = acnt
        self.lmt = lmt
        self.balance = 0

    def get_user(self):
        return self.user
    def get_bank(self):
        return self.bank
    def get_acnt(self):
        return self.acnt
    def get_lmt(self):
        return self.lmt
    def get_balance(self):
        return self.balance

    def charge(self, price):
        if price + self.balance > self.lmt:
            return False
        else:
            self.balance += price
            return True

    def make_payment(self, amount):
        self.balance -= amount

# cc = CreditCard("John", "1st Banl", "123456", 1000)

if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard("John", "1st Banl", "123456", 1000))
    wallet.append(CreditCard("John1", "1st Banl", "1234567", 1000))
    wallet.append(CreditCard("John2", "1st Banl", "12345678", 1000))

    for val in range(1, 17):
        wallet[0].charge(1 * val)
        wallet[1].charge(1 * val)
        wallet[2].charge(1 * val)

    for c in range(3):
        print('user = ', wallet[c].get_user())
        print('bank = ', wallet[c].get_bank())
        print('account = ', wallet[c].get_acnt())
        print('lmt = ', wallet[c].get_lmt())
        print('balance = ', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('new balance = ', wallet[c].get_balance())
        print()
'''
'''
a = [1,2,4,6]
b = [2,2,2,2]
c = a + b
print(c)
'''
'''''
def sum_vector(vector1, vector2):

    if len(vector1) != len(vector2):
        return ('Error')
    else:
        result = [0] * len(vector1)
        for i in range(len(vector1)):
            result[i] = vector1[i] + vector2[i]
        return result

a = [1,3,5,6]
b = [0,2,4,5]
c = sum_vector(a, b)
print(c)

'''
'''
class Range:
    def __init__(self, start, stop, step = 1):
        self.start = start
        self.step = step
        self.stop = stop
        self.length = max(0,(stop-start)//step)

        if step == 0:
            raise ValueError('step cannot be 0')
#        if stop is None:
#            start, stop = 0, start

    def __len__(self):
        return self.length

    def __getitem__(self, i):
        if i < 0:
            i += len(self)
        if i >= self.length:
            raise IndexError('index out of range')
        return self.start + i * self.step

for k in Range(15,5,-2):
    print(k)

myRange = Range(15,5,-2)
a = myRange[-1]
print(a)

'''











