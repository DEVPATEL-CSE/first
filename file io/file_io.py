
                                                # practice

# f = open('txt1','r')
# text = f.read()
# print(text)
# f.close()

# f= open('txt1','w')
# text = f.write("the is the new line added by python file ")
# f.close()

# f= open('txt1','a')
# text = f.write(input("\nenter the content that you want: "))
# f.close()

# f = open('txt1','r')
# while True:
#     line = f.readlines()
#     print(line)
#     if not line:
#         break

# 11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111


"""
user will pass filename and file location as arguments

user will input no of lines

user will input data

write data in file

read data from file

count lines,words,with space chars & without space chars
"""




# name = input("Enter the file name: ")
# loction = input("Enter the loction: ")
#
# filepath = loction + name
# f = open(filepath,'w')
# n = int(input("please enter the number of lines: "))
# for i in range(1,n+1):
#     m = input(f" line {i} : ")
#     u = f.write(m + "\n")
#
# f.close()
#
# f= open(filepath,'r')
# line = f.read()
# print(line)
#
# f.close()
#
# l=0
#
# f= open(filepath,'r')
# for line in f:
#     l = l + 1
# print("Total number of line is - ",l)
# f.close()
#
# w=0
#
# f= open(filepath,'r')
# for line in f:
#     k = line.split()
#     w += len(k)
# print("Total number of words is - ",w)
# f.close()
#
# ws=0
# f= open(filepath,'r')
# for line in f:
#     for word in line:
#         for char in word:
#             ws = ws +1
# print("Total number of character with space is - ",ws)
# f.close()
#
# c = 0
# f= open(filepath,'r')
# for line in f:
#     j = line.split()
#     for words in j:
#         for characters in words:
#             c = c+1
# print("The total number of characters without space is - ",c)
# f.close()


#2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222


"""
user will pass filename and file location as arguments
----------------------------------------
user will input no of lines

user will input data

write data in demo.txt

read data from demo.txt
Hello C
Hello C++
Hello Java

linewise reverse write in dummy.txt
Hello Java
Hello C++
Hello C
-----------------------------------------
user will replace the word in dummy.txt

	user will input word to replace->Hello

	user will input word in replacement->Hi

data should be replace in dummy.txt
-----------------------------------------
"""




name = input("Enter the file name: ")
loction = input("Enter the loction: ")

filepath = loction + name
f = open(filepath,'w')
n = int(input("please enter the number of lines: "))
for i in range(1,n+1):
    m = input(f" line {i} : ")
    u = f.write(m + "\n")

f.close()

f= open(filepath,'r')
line = f.read()
print(line)

f.close()

f= open(filepath,'r')
lines = f.readlines()
lines.reverse()
f.close()
f = open('dummy','w')
for line in lines:
    f.write(line)
f.close()

f = open('dummy','r')
o = f.read()
print("Reverse: \n",o)
f.close()

old = input("Enter the old word")
new = input("Enter the new word")

f = open('dummy','r')
content = f.read()
latest_content = content.replace(old,new)
f.close()

f = open('dummy','w')
f.write(latest_content)
f.close()

f = open('dummy','r')
o = f.read()
print("Replace: \n",o)
f.close()