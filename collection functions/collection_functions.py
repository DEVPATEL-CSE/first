
# 111111111111111111111111111111111111111111

"""user input values in a variable like

a=1,a,2,b,3,4,55,asit,nimesh

str_list=[]

int_list=[]

store int values inside int_list as integer
    -perform min and max function

store string values inside str_list as string
    -perform reverse function """

# n = int(input("please enter the numbers of input: "))
# int_list=[]
# str_list=[]
# for i in range(n):
#     j = input("please enter the elements of list ")
#     if type(j) is str:
#         if j.isnumeric()==True:
#             int_list.append(int(j))
#         else:
#             str_list.append(j)
# print(int_list)
# print(str_list)
# print(f"min is {min(int_list)} and max is {max(int_list)}")
# print(f"revesed list {str_list[::-1]}")





# 2222222222222222222222222222222222222222222

"""student={
's1':{
    'rollno':input,
    'name':input,
    'marks':input,
    'grade':None,
},
's2':{
    'rollno':input,
    'name':input,
    'marks':input,
    'grade':None,
},
's3':{
    'rollno':input,
    'name':input,
    'marks':input,
    'grade':None,
},
's4':{
    'rollno':input,
    'name':input,
    'marks':input,
    'grade':None,
},
's5':{
    'rollno':input,
    'name':input,
    'marks':input,
    'grade':None,
}

}

create the data structure manually

input the data

---------------dynamic----------------------

find the grade and assign

90 to 100->A grade assign

80 to 90->B grade assign

60 to 80->C grade assign

40 to 60->D grade assign

<40->Fail

display the student dictionary"""







# l = {}
# nl = { }
# k = int(input("enter the number of student"))
# def decide(n):
#     if n>44:
#         print("vfvv")
# for i in  range(k):
#     key = f"s{k}"
#     value= nl = {
#     'rollno': int(input("roll no ")),
#     'name':str(input("namen")),
#     'marks':int(input("marks")),
#     'grade': decide(nl['marks']),
#     }
#     l[key] = value
# print(l)
# y={}
# l = {}
# nl = { }
# k = int(input("enter the number of student"))
# for i in  range(k):
#     # print(k)
#     key = f"s{k}"
#     value= nl = {
#     'rollno': int(input("roll no ")),
#     'name':str(input("namen")),
#     'marks':int(input("marks")),
#     }
#     l[key] = value
#     y.update(l)
# print(y)

# student = {}
#
# k = int(input("enter the number of students "))
# for i in range(1,k+1):
#     index = f"s{i}"
#     student[index]= {'rollno': int(input(f"Enter roll number for student {i}: ")),
#         'name': str(input(f"Enter name for student {i}: ")),
#         'marks': int(input(f"Enter marks for student {i}: ")),
#         'grade': None,}
# for key in student:
#     marks = student[key]['marks']
#     if marks >= 90:
#         student[key]['grade'] = 'A'
#     elif marks >= 80:
#         student[key]['grade'] = 'B'
#     elif marks >= 60:
#         student[key]['grade'] = 'C'
#     elif marks >= 40:
#         student[key]['grade'] = 'D'
#     else:
#         student[key]['grade'] = 'Fail'
#
# print(student)



# 3333333333333333333333333333333333333333333

"""user will decide no. of lists
2

user wil input no. of elements for each list
ls1=>5
ls2=>7

user will input element for each list
ls1=[1,11,43,56,43]
ls2=[1,32,3,4,5,6,7]

calculate(ls1)=>print the list

calculate(ls1,ls2)=>
concate both the lists=>
print maximum-minimum element
    56,1

calculate(ls1,ls2,ls3)=>
concate all the lists=>
print internal addition of all elements


calculate(n list)=>concate all the lists
lambda function
    print the square of every element and store in list
    find the odd number and store in list"""


# manually

# l1 = []
# l2 = []
# l3 = []
# a = int(input("enter the number of list "))
#
# if a == 1:
#     n = int(input("enter the number of elements for list1 "))
#
#     for i in range(1, n + 1):
#         j = int(input(f"enter element {i} "))
#         l1.append(j)
#
#     def calculate(lst):
#         print(lst)
#     calculate(l1)
#
# elif a == 2:
#     n = int(input("enter the number of elements for list1 "))
#
#     for i in range(1, n + 1):
#         j = int(input(f"enter element {i} "))
#         l1.append(j)
#
#     p = int(input("enter the number of elements for list2 "))
#     for k in range(1, p + 1):
#         e = int(input(f"enter element {k} "))
#         l2.append(e)
#
#
#     def calculate(lst1, lst2):
#         sum = lst1 + lst2
#         print(sum)
#         print(f"max {max(sum)} , min {min(sum)}")
#
#     calculate(l1,l2)
#
# elif a == 3:
#     n = int(input("enter the number of elements for list1 "))
#
#     for i in range(1, n + 1):
#         j = int(input(f"enter element {i} "))
#         l1.append(j)
#
#     p = int(input("enter the number of elements for list2 "))
#     for k in range(1, p + 1):
#         e = int(input(f"enter element {k} "))
#         l2.append(e)
#
#     r = int(input("enter the number of elements for list3 "))
#     for h in range(1, r + 1):
#         e = int(input(f"enter element {h} "))
#         l3.append(e)
#     def calculate(lst1 ,lst2,lst3):
#         sum1 = lst1+lst2+lst3
#         print(sum1)
#         print(f"sum is {sum(sum1)}")
#
#
#     calculate(l1, l2,l3)

#------------------------------------------------------------------------------------------------------
# auto





# n= int(input("enter the number of elements for list1 "))
#
# for i in range(1,n+1):
#
#     j = int(input(f"enter element {i} "))
#     l1.append(j)
#
# p= int(input("enter the number of elements for list2 "))
# for p in range(1,p+1):
#     e = int(input(f"enter element {p} "))
#     l2.append(e)



# def calculate(lst):
#     print(lst)
#
# def calculate(lst1,lst2):
#     sum=lst1+lst2
#     print(sum)
#     print(f"max {max(sum)} , min {min(sum)}")
#
# calculate(l1)
# calculate(l1,l2)

# n = int(input("Enter the number of empty lists: "))
#
# # Create multiple empty lists and assign them to variables dynamically
# for i in range(1, n+1):
#     globals()[f'list_{i}'] = []

# Example: Print the lists to verify they are created
# for i in range(1, n+1):
#     print(f'list_{i} = {globals()[f"list_{i}"]}')
#
# if n == 1:
#     n1 = int(input("enter the number of elements for list1 "))
#
#     for i in range(1, n1 + 1):
#         j = int(input(f"enter element {i} "))
#         globals()[f'list_{i}'].append(j)
#
#     def calculate(lst):
#         print(lst)
#     calculate([f'list_{i}'])

# N = int(input("Enter the number of empty lists: "))
#
# # Create multiple empty lists and assign them to variables dynamically
# for i in range(1, N+1):
#     globals()[f'list_{i}'] = []
#
# # Append elements to the lists
# for i in range(1, N+1):
#     num_elements = int(input(f"Enter the number of elements for list_{i}: "))
#     for j in range(num_elements):
#         element = input(f"Enter element {j+1} for list_{i}: ")
#         globals()[f'list_{i}'].append(element)
#
# if N == 1:
#     def calculate(n):
#         print(n)
#     calculate(globals()[f'list_{i}'])
# if N == 2:
#     def calculate(n1,n2):
#         sum1 = n1+n2
#         print(max(sum1),min(sum1))
#     calculate(globals()[f'list_{i}'],globals()[f'list_{i}'])




