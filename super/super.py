# super for object and method

class parent:

    name = "dev"

    def parent_method(self):
        print("this is parent class method")


class child(parent):

    def child_method(self):

        super().parent_method()

        print(super().name)

        print("this is child class method")


c = child()
c.child_method()


# super for costructor

class A:

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"the name is {self.name}")


class B(A):

    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

    def show(self):
        print(f"the name is {self.name} and company is {self.company}")


a = A("dev")
a.show()
b = B("dev", "google")
b.show()
