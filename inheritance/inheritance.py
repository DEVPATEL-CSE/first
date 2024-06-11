class alpha:
    def fun1(self):
        print("this is class A")

# class beta(alpha):
#     def fun2(self):
#         alpha.fun1(self)
#         print("this is class B")
# class chrlie(beta):
#     def fun3(self):
#         beta.fun2(self)
#         print("this is class C")
#
# # b= beta()
# # b.fun2()
# # b.fun1()
#
# c= chrlie()
# c.fun3()


"""
BankInfo
    fn
    ln
    gender
    address

BankAccount
    acno
    amount
    object_BankInfo

Saving
    minAmount = 10000
    rate=6%

Current
    minAmount = 5000
    rate=No

Main

    user will input data for BankInfo-C

    user will input data for BankAccount-C

    user will select Saving or Current

    validate the amount given by user- give 3 chances-F

    input months

    calculate the interest-F
"""

class BankInfo:
    def __init__(self, firstname, lastname, gender, address):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.address = address

class BankAccount(BankInfo):
    def __init__(self, firstname, lastname, gender, address, acno, amount):
        super().__init__(firstname, lastname, gender, address)
        self.acno = acno
        self.amount = amount

class saving(BankAccount):
    def __init__(self, firstname, lastname, gender, address, acno, amount):
        super().__init__(firstname, lastname, gender, address, acno, amount)
        self.minAmount = 10000
        self.rate = 0.06

    def valid(self):
        for i in range(3, 0, -1):
            if self.amount >= self.minAmount:
                break
            elif i>= 1:
                self.amount = int(input(f"Enter the amount again {i} trials are remaining: "))
            else:
                print("fail")
                return

        self.interest()

    def interest(self):
        self.m = int(input("Enter months: "))
        self.inter = (self.amount * self.rate * self.m) / 100
        print("Interest:", self.inter)

class current(BankAccount):
    def __init__(self, firstname, lastname, gender, address, acno, amount):
        super().__init__(firstname, lastname, gender, address, acno, amount)
        self.minAmount = 5000
        self.rate = 0

    def valid(self):
        for i in range(3, 0, -1):
            if self.amount >= self.minAmount:
                break
            elif i >= 1:
                self.amount = int(input(f"Enter the amount again {i} trials are remaining: "))
            else:
                print("fail")
                return

        self.interest()

    def interest(self):
        self.m = int(input("Enter months: "))
        self.inter = (self.amount * self.rate + self.m) / 100
        print("Interest:", self.inter)


class Main:
    fn = input("Enter your First Name: ")
    ln = input("Enter your Last Name: ")
    g = input("Enter Gender: ")
    ad = input("Enter Address: ")
    an = input("Enter your account number: ")
    am = int(input("Enter the amount: "))
    n = int(input("Enter 1 for saving or 2 for current account: "))
    if n == 1:
        s = saving(fn, ln, g, ad, an, am)
        s.valid()
    elif n == 2:
        c = current(fn, ln, g, ad, an, am)
        c.valid()
