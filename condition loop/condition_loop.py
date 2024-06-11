
"""
universal string and its count of characters
"""

# l = str(input("Please enter the string: "))
# k={}
#
# for x in l:
#     a=l.count(x)
#     k[x] = a
# print(k)
    # if x in k:
    #     print(f" the occurance of {x} is {a}")

"""# stone paper scissor"""
# import random
# l=["stone","paper","scissor"]
# k_r = 0
# o_r = 0
#
# for i in range(5):
#     k = str(input("please select your value: "))
#     o = random.choice(l)
#
#     print("The computer value is",o)
#     if o=="stone" and k=="paper":
#         print("you won")
#         k_r = k_r + 1
#     elif o=="stone" and k=="stone":
#         print("draw")
#     elif o=="stone" and k=="scissor":
#         print("you lost")
#         o_r = o_r+1
#     elif o=="paper" and k=="stone":
#         print("you lost")
#         o_r = o_r + 1
#     elif o=="paper" and k=="paper":
#         print("draw")
#     elif o=="paper" and k=="scissor":
#         print("you won")
#         k_r = k_r + 1
#     elif o=="scissor" and k=="stone":
#         print("you won")
#         k_r = k_r + 1
#     elif o=="scissor" and k=="paper":
#         print("you lost")
#         o_r = o_r + 1
#     elif o=="scissor" and k=="scissor":
#         print("draw")
#     else:
#         print("wrong input")
# if k_r>o_r:
#     print(f" you score{k_r},computer score{o_r}. you won the competition")
# elif k_r==o_r:
#     print(f"you score{k_r},computer score{o_r}. competition draw")
# else:
#     print(f"you score{k_r},computer score{o_r}.you lost the competition")


# factorial
# def fun(n):
#     if n==1:
#         return n
#     else:
#         return n * fun(n-1)
# l= int(input("Enter the number: "))
# if l <=0:
#     print("please enter positive value")
# else:
#     print("output is ",fun(l))

# fibonacci
# def fun(n):
#     if n<=1:
#         return n
#     else:
#         return fun(n-1) + fun(n-2)
# l= int(input("Enter the number: "))
# if l <=0:
#     print("please enter positive value")
# else:
#     print("output is ")
#     for i in range(l):
#         print(fun(i))

# n = int(input("please enter the numbers of raws "))
# k=1
# for i in range(n+1):
#
#     for j in range(i):
#         print(k,end=" ")
#         k = k+1
#     print()


"""
1) user input a character

	a->"you have enter a"
	
	b->"you have enter b"
	
	c->"you have enter c"
	
	->Invalid character


2)user input a number

	positive number
		odd number
			perform addition with an integer constant
	
		even number
			perform multiplication with an floating point constant
	
	negative number
		odd number
			perform subtraction with an integer constant
		
		even number
			perform division with an floating point constant

3)user input marks

	90 to 100->A grade
	
	80 to 90->B grade
	
	60 to 80->C grade
	
	40 to 60->D grade
	
	< 40     ->Fail
	
	>100 	->Invalid Marks
"""






# 1
# n = input("enter the character ")
# if type(n) is str:
#     print("you have entered ",n)
# else:
#     print("invalid syntax ")

# 2
# n = int(input("Enter the number: "))
# k=2
# f=2.50
# if n>0:
#     if n%2==0:
#         print("positive even ",n*f)
#     else:
#         print("positive odd",n+k)
# elif n<0:
#     if n%2==0:
#         print("negative even ",n/f)
#     else:
#         print("negative odd",n-k)

# 3
# n= int(input("please enter student's marks "))
# if n in range(90,101):
#     print("grade A")
# elif n in range(80,90):
#     print("grade B")
# elif n in range(60,80):
#     print("grade C")
# elif n in range(40,60):
#     print("grade D")
# elif n<40:
#     print("fail")
# elif n>100:
#     print("invalid marks")

# 4
# n=int(input("please enter the number "))
# f=1
# while n>=1:
#     f = f*n
#     n = n-1
# print(f)

l= "mango"
k=[]
for i in l:
    if i=="g":
        break
    else:
        k.append(i)
print(k)

