# class A:
#     def __init__(self, value):
#         self._value = value

#     def show(self):
#         print(f"value is {self._value}")

#     @property  # this is getter
#     def ten_value(self):
#         return 10 * self._value

#     @ten_value.setter
#     def ten_value(self, new_value):
#         self._value = new_value/10


# a = A(10)
# print(a._value)
# a.ten_value = 88  # changing ten_value
# print(a.ten_value)  # using function as a object () are not used
# a.show()

"""
Getter and setter are basically use to convert the function into object and then change the value
"""


class library:
    def __init__(self):
        self.nobooks = 0
        self.books = []

    def addbooks(self, book):
        self.books.append(book)
        self.nobooks = len(self.books)

    def showbooks(self):
        return f"no of books are: {self.nobooks} and books are{self.books:}"


l = library()
n = int(input("Enter the number of books you want to enter: "))
for i in range(1, n+1):
    m = input(f"enter book{i} name: ")
    l.addbooks(m)
print(l.showbooks())
