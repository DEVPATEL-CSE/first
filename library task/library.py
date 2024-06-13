# user will input the name of book you have to print no of books and books name

# manual
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

l.addbooks(m)
print(l.showbooks())

"""

# auto

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
"""

# modfied where user can borrow back the entered books


class library:
    def __init__(self):
        self.nobooks = 0
        self.books = []

    def addbooks(self, book):
        self.books.append(book)
        self.nobooks = len(self.books)

    def borrow(self, b):
        self.books.remove(b)
        self.nobooks = len(self.books)

    def showbooks(self):
        return f"no of books are: {self.nobooks} and books are{self.books:}"


l = library()
q = 1
for w in range(q):
    n = int(input("Enter the number of books you want to enter: "))
    for i in range(1, n+1):
        m = input(f"enter book{i} name: ")
        l.addbooks(m)
    print(l.showbooks())

    choice = input("do you want to borrow books(yes/no) ")
    if choice == "yes":
        k = int(input("Enter the number of books you want to borrow: "))
        for j in range(1, k+1):
            p = input(f"enter book{j} name: ")
            l.borrow(p)
        print(l.showbooks())
    elif choice == "no":
        break
