class Error(Exception):
    pass


class HDFC:
    def __init__(self):
        self.__max_transaction = 3
        self.__max_amount = 20000
        self.__transactions = 0
        self.__amount_withdrawn = 0

    def withdraw(self, amount):
        if self.__transactions >= self.__max_transaction:
            raise Error("Max transaction limit exceeded")
        if self.__amount_withdrawn + amount >= self.__max_amount:
            raise Error("Max amount limit exceeded")

        self.__transactions += 1
        self.__amount_withdrawn += amount
        print(
            f"Withdrawal successful from HDFC. Remaining transaction limit: {self.__max_transaction - self.__transactions}, Remaining amount limit: {self.__max_amount - self.__amount_withdrawn}")


class Axis:
    def __init__(self):
        self.__max_transaction = 5
        self.__max_amount = 30000
        self.__transactions = 0
        self.__amount_withdrawn = 0

    def withdraw(self, amount):
        if self.__transactions >= self.__max_transaction:
            raise Error("Max transaction limit exceeded")
        if self.__amount_withdrawn + amount >= self.__max_amount:
            raise Error("Max amount limit exceeded")

        self.__transactions += 1
        self.__amount_withdrawn += amount
        print(
            f"Withdrawal successful from AXIS. Remaining transaction limit:"
            f" {self.__max_transaction - self.__transactions}, Remaining amount limit: {self.__max_amount - self.__amount_withdrawn}")


class ATM:
    def input_amount(self):
        while True:
            n = input("Enter 1 for HDFC or 2 for AXIS: ")
            if n == "1":
                bank = HDFC()
                break
            elif n == "2":
                bank = Axis()
                break
            else:
                print("Invalid choice. Please enter 1 for HDFC or 2 for AXIS.")

        while True:
            try:
                a = int(input("Enter amount to withdraw"))
                bank.withdraw(a)
            except Error as e:
                print(e)
                break

            c = input("Do you want to make another transaction? (yes/no): ")
            if c != "yes":
                print("Thank you for using services. Goodbye!")
                return


atm = ATM()
atm.input_amount()
