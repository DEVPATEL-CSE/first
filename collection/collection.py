
"""
ls = [1, '2', 3, ['a', 'b', 'c'], 4, 5, 6,['Jai Hind'],['d', 'e', 'f'], 7, 'g', 8, 'h', [9, '10', 'i', 'j'],11,'aaditya']

output should be-

1
2
3
       a
       b
       c
4
5
6
       Jai Hind
       d
       e
       f
7
       g
8
       h
9
10
       i
       j
11
       aaditya
"""


# ls = [1, '2', 3, ['a', 'b', 'c'], 4, 5, 6,['Jai Hind'],['d', 'e', 'f'], 7, 'g', 8, 'h', [9, '10', 'i', 'j'],11,'aaditya']
# l = str(ls)
# # for i in ls:
# #     if isinstance(i,list):
# #         print(i)
# #     else:
# #         print(i)
#
#
# for i in l:
#     if type(i) is int:
#

#
# ls = [1, '2', 3, ['a', 'b', 'c'], 4, 5, 6,['Jai Hind'],['d', 'e', 'f'], 7, 'g', 8, 'h', [9, '10',['dev',1,"2","hello"], 'i', 'j'],11,'aaditya']
# for i in ls:
#     if type(i)==int:
#         print(i)
#     elif type(i)==str:
#         if i.isnumeric()==True:
#             print(i)
#         else:
#             print("       ",i)
#     else:
#         for j in i:
#             if type(j) == int:
#                 print(j)
#             elif type(j) == str:
#                 if j.isnumeric() == True:
#                     print(j)
#                 else:
#                     print("       ", j)
#             else:
#                 for z in j:
#                     if type(z)==int:
#                         print(z)
#                     elif type(z)==str:
#                         if z.isnumeric()==True:
#                             print(z)
#                         else:
#                             print("       ", z)



# 1
# n = int(input("Enter the number of raws: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("_",end="*")
#     print()

# 2
# n = int(input("ENTER THE NUMBER OF ROWS: "))
# k=1
# for i in range(1,n+1):
#     for j in range(1,k+1):
#         print("*",end="_")
#     print()
#     k=k+3

# n = int(input("enter the number of rows "))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# for i in range(n-1):
#     for j in range(i,n):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()
#
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*", end=" ")
#     for j in range(i,n-1):
#         print("*", end=" ")
#     print()


def grad(avg):
    if avg in range(90,101):
       return print("Grade A")
    elif avg in range(80,90):
       return print("Grade B")
    if avg in range(60,80):
       return print("Grade C")
    if avg in range(40,60):
       return print("Grade D")
    if avg in range(0,40):
       return print("Fail")