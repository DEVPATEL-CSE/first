class math:

    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n
        print(self.num)

    @staticmethod
    def add(a, b):  # self is not required
        return a+b


a = math(4)

a.addtonum(3)

print(a.add(2, 3))  # call it via instance or class name

print(math.add(2, 3))
