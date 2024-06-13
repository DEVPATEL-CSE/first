# without class method
"""class employee:

    compnay = "google"

    def show(self):
        print(f"name is {self.name} and company is {self.compnay}")

    def changeco(cls, new):
        cls.compnay = new


e = employee()
e.name = "dev"
e.show()
e.changeco("facebook")
e.show()
print(employee.compnay) #output - google because cls is instance in which new value is stored
"""

# with classmethod


class employee:

    compnay = "google"

    def show(self):
        print(f"name is {self.name} and company is {self.compnay}")

    @classmethod
    def changeco(cls, new):
        cls.compnay = new


e = employee()
e.name = "dev"
e.show()
e.changeco("facebook")
e.show()
# output - facebook because cls is class in which new value is stored
print(employee.compnay)
