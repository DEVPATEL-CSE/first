# operators
"""
ls=[0,8,4,12,2,12,4,9,1,3,5,13,3] = 13 elements
"""
"""
l=[]
n = int(input("Please enter the number of elements: "))
for i in range(1,n+1):
    m = int(input(f"Enter {i} element- "))
    l.append(m)
print(sum(l))

k=l[:6]
print(f"sublist is {k} and sum is {sum(k)}")
j=l[6:]
print(f"sublist is {j} and sum is {sum(j)}")
"""


# collection task1
"""
l = [1, '2', 3, ['a', 'b', 'c'], 4, 5, 6,['Jai Hind'],['d', 'e', 'f'], 7, 'g', 8, 'h', [9, '10', 'i', 'j'],11,'aaditya']
for i in l:
    if type(i) == int:
        print(i)
    elif type(i) == str:
        if i.isnumeric()==True:
            print(i)
        else:
            print(f"       {i}")
    elif type(i)== list:
        for j in i:
                if type(j) == int:
                    print(j)
                elif type(j) == str:
                    if j.isnumeric() == True:
                        print(j)
                    else:
                        print("       ", j)
"""


# collection task 2


"""
student={}
n = int(input("enter the number of students: "))
for i in range(1,n+1):
    key=f"s{i}"
    student[key]={
        'rollno': int(input(f"Enter {i} student rollno- ")),
        'name': input("Enter the name of student: "),
        'marks': int(input(f"Enter the marks of {i} student- ")),
        'grade': None,
    }


for keys in student:
    marks = student[keys]['marks']
    if marks in range(90,101):
        student[keys]['grade']='A'
    elif marks in range(80,90):
        student[keys]['grade']='B'
    elif marks in range(60,80):
        student[keys]['grade']='C'
    elif marks in range(40,60):
        student[keys]['grade']='D'
    elif marks in range(0,40):
        student[keys]['grade']='Fail'

print(student)
"""

# Exception handling
"""
user will input data for SignUp class-Constructor
    fn,ln,un,pwd

    pwd must fulfil below given criteria
        minmum 8 characters
        maximum 16 characters
        at least one lowercase
        at least one uppercase
        at least one digit
        at least one special character
    if not matched then print custom message with exception
    and give chance again till condition not satisfied

user will input data for SignIn class-Constructor
    un,pwd

    compare SignUp (un and pwd) with (SignIn un and pwd)
        loginCheck()-Function
        if not matched then print custom message with exception
        else print welcome message with fn and ln
"""

"""
class Error(Exception):
    pass

class signup:
    def __init__(self,firstname,lastname,username,password):
        self.firstname= firstname
        self.lastname= lastname
        self.username=username
        self.password= password

    def checker(self):
        p= self.password
        if not len(p) in range(8,17):
            raise Error("minimum length is 8 andd maximum length is 16 ")
        if not any(i.islower() for i in p):
            raise Error("please enter atlist one lower character")
        if not any(i.upper() for i in p):
            raise Error("please enter atlist one capital character")
        if not any(i.isnumeric() for i in p):
            raise Error("please enter atlist one number ")
        if not any(i.isalnum() for i in p):
            raise Error("please enter atlist one special character")
class signin:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def loginchecker(self,a,b,c,d):
        if not a==c:
            raise Error("invalid username")
        if not b==d:
            raise Error("invalid password")


while True:
    try:
        fn = input("Enter first name ")
        ln = input("Enter last name ")
        un = input("Enter user name ")
        ps = input("Enter password ")
        su = signup(fn, ln, un, ps)
        su.checker()
        print("sign up sucessfully ")
        f=input("Enter name for sign in ")
        psw=input("Enter password ")
        si=signin(f,psw)
        si.loginchecker(un,ps,f,psw)
        print(f"welcome {fn} {ln}")
        break
    except Error as e:
        print(e)
"""

# patterns

"""
1.
 *
 * *
 * * *
 * * * *
"""
n = int(input("ENTER THE NUMBER OF ROWS: "))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

"""
2.
* 
* * * 
* * * * * 
* * * * * * *
"""
# n = int(input("ENTER THE NUMBER OF ROWS: "))
# k=1
# for i in range(1,n+1):
#     for j in range(1,k+1):
#         print("*",end=" ")
#     print()
#     k=k+2

"""
3. 
* * * * 
* * * 
* * 
* 
"""
# n = int(input("ENTER THE NUMBER OF ROWS: "))
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()


"""
4.
        * 
      * * 
    * * * 
  * * * * 
"""
# n = int(input("ENTER THE NUMBER OF ROWS: "))
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

"""
5.
  * * * * 
    * * * 
      * * 
        * 
"""
# n = int(input("ENTER THE NUMBER OF ROWS: "))
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()
"""
6.
        * 
      * * * 
    * * * * * 
  * * * * * * * 
"""
# n = int(input("ENTER THE NUMBER OF ROWS: "))
# for i in range(n):
#     for j in range(i,n):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

"""
7. THALA FOR A REASON
              7 
            7 7 7 
          7 7 7 7 7 
        7 7 7 7 7 7 7 
      7 7 7 7 7 7 7 7 7 
    7 7 7 7 7 7 7 7 7 7 7 
  7 7 7 7 7 7 7 7 7 7 7 7 7 
    7 7 7 7 7 7 7 7 7 7 7 
      7 7 7 7 7 7 7 7 7 
        7 7 7 7 7 7 7 
          7 7 7 7 7 
            7 7 7 
              7 

"""
n = int(input("ENTER THE NUMBER OF ROWS: "))
for i in range(n-1):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i):
        print("7", end=" ")
    for j in range(i+1):
        print("7", end=" ")
    print()

for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("7", end=" ")
    for j in range(i,n-1):
        print("7", end=" ")
    print()