
# Exeption handling


# --------------------------------------waste----------------------------------------------
# print("Pleasse enter the details for sign up below: ")
# # fn= str(input("Enter first name: "))
# # ln= str(input("Enter last name: "))
# # dn= str(input("Enter user name: "))
# psw = input("enter the password")
# pw="Devpatel@10"
# try:
#     if len(psw) in range(8,17):
#         pass
#     # else:
#     #     print("minimum length is 8 andd maximum length is 16")
#     if psw.islower()==True:
#         pass
#     # else:
#     #     print("please enter atleast one lower case character")
#     if psw.isupper()==True:
#         pass
#     # else:
#     #     print("Please enter atleast one upper character")
#     if psw.isnumeric()==True:
#         pass
#     # else:
#     #     print("please enter atleast one digit")
#     if psw.isalnum()==True:
#         pass
#     # else:
#     #     print("please enter atleast one special character")
#     print("sign up sucessfull")
#
# except ValueError as e:
#     print("password citeria not matched", e)




# 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111



# class error(Exception):
#     pass
#
# class signup:
#     def __init__(self,firstname,lastname,username,password):
#         self.firstname=firstname
#         self.lastname=lastname
#         self.username=username
#         self.password=password
#
#     def checker(self):
#         if not len(self.password) in range(8,17):
#             raise error("please keep your password in range 8 to 16 ")
#         if not any(i.islower() for i in self.password):
#             raise error("atleast one lower character required")
#         if not  any(i.isupper() for i in self.password):
#             raise error("atleast one upper character required")
#         if not any(i.isnumeric() for i in self.password):
#             raise error("atleast one number required")
#         if not any(i.isalnum() for i in self.password):
#             raise error("atleast one special character required")
#
# while True:
#     try:
#         fn=str(input("enter username "))
#         ln=str(input("enter last name "))
#         un=str(input("enter user name "))
#         ps = input("enter password  ")
#         su=signup(fn,ln,un,ps)
#         su.checker()
#         print("password created succesfully")
#         break
#     except error as e:
#         print("please enter password again: ",e)




#22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222



class passwordCriteriaError(Exception):
    pass
class signup:
    def __init__(self,firstname,lastname,username,password):
        self.firstname=firstname
        self.lastname=lastname
        self.username=username
        self.password=password

    def checker(self):
        usn = self.username
        psw = self.password
        if not len(psw) in range(8, 17):
            raise passwordCriteriaError("minimum length is 8 andd maximum length is 16")
        # else:
        #     print("minimum length is 8 andd maximum length is 16")
        if not any(i.islower() for i in psw):
            raise passwordCriteriaError("please enter atleast one lower case character")
            pass
        # else:
        #     print("please enter atleast one lower case character")
        if not any(i.isupper() for i in psw):
            raise passwordCriteriaError("please enter atleast one upper character")
        # else:
        #     print("Please enter atleast one upper character")
        if not any(i.isnumeric() for i in psw):
            raise passwordCriteriaError("please enter atleast digit")
        # else:
        #     print("please enter atleast one digit")
        if not any(i.isalnum() for i in psw):
            raise passwordCriteriaError("please enter atleast one special character")
        # else:
        #     print("please enter atleast one special character")
class signin():
    def __init__(self,usern,pd):
        self.usern = usern
        self.pd = pd
    def logincheck(self,a,b,c,d):
        if not a==c:
            raise passwordCriteriaError("invalid username")
        if not  b==d:
            raise passwordCriteriaError("invalid password")



while True:
    try:
        fn= str(input("Enter first name: "))
        ln= str(input("Enter last name: "))
        un= str(input("Enter user name: "))
        ps = input("enter the password")
        su = signup(fn,ln,un,ps)

        su.checker()
        print("sign up sucessfull")
        # sun = str(input("enter username for sign in "))
        # sps = input("enter the password for sign in")
        # si= signin(sun,sps)
        # si.logincheck(sun,sps,un,ps)
        # print(f"welcome {fn} {ln}")
        break
    except passwordCriteriaError as  e:
        print("try again",e)

while True:
    try:
        sun = str(input("enter username for sign in "))
        sps = input("enter the password for sign in")
        si = signin(sun, sps)
        si.logincheck(sun, sps, un, ps)
        print(f"welcome {fn} {ln}")
        break

    except passwordCriteriaError as e:
        print(e)


