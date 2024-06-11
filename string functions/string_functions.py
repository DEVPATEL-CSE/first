# l = [0, 1, 2, 3, 4, 5, 6]
# print(l[:])
# print(l[0:5])
# print(l[1:5])
# print(l[3:])
# print(l[:-2])
# print(l[::-1])

# even = []
# odd = []

# for i in l:
#     if l[i] % 2 == 0:
#         even = even.append(i)
#     else:
#         odd = odd.append(i)
# print(odd)
# print(even)


# from sklearn.cluster import k_means


# l = [0, 1, 2, 3, 4, 5, 6]
# even = []
# odd = []

# for i in l:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(odd)
# print(even)

# m = []
# for i in l:
#     if i >= 5:
#         m.append(i)
# print(m)

# sum = 0
# for i in l:
#     sum += i
# print(sum)
# print(l.sort())
# k = [2, 5, 2, 4, 6, 4, 25, 7, 88]
# k.sort()
# print(k)

# o = (2, 3, 4, 5, 5)
# print(type(o))
# j = list(o)
# print(type(j))


import json
from typing import List
l = {"name": "dev", "roll no": 99, "place": "ahmedabad"}
# print(l)
# # print(l.keys(), "is", l.values())
# print(l.values())
# print(l["name"])

# for key in l.keys():
#     print(f"{key} is {l[key]}")


# l1 = list(l.items())
# print(l1)

# l_keys = list(l.keys())
# print(type(l_keys))

# t_keys = tuple(l.keys())
# print(type(t_keys))

# l_value = list(l.values())
# print(type(l_value))

# t_value = tuple(l.values())
# print(type(t_value))


# my_json = open('json1.py', 'r')
# jsondata = my_json.read()
# obj = json.loads(jsondata)

# print(str(obj['firstName']))
# print(obj)
# print(type(obj))

# 1

s = "this is string example"
reversed_s = s[::-1]
print(reversed_s)

# 2

words = s.split()
rs = ' '.join(reversed(words))
print(rs)

# 3

s = 'this is string example'
l = s[0:4][0:2][::-1]+s[0:4][2:4][::-1]+" "+s[5:7][0:2][::-1]+" "+s[8:14][0:2][::-1]+s[8:14][2:4][::-1]+s[8:14][4:6][
    ::-1]+" "+s[15:23][:2][::-1]+s[15:23][2:4][::-1]+s[15:23][4:6][::-1]+s[15:23][-1]
print(l)

# pos1 = 0
# pos2 = 1
# j = converter(s, pos1, pos2)
# print(j)

# 4
jk = s.split()
fs = "*".join(jk)
print(fs)


# 5

original_string = "this is string example"


modified_string = original_string.replace(" is", " was")

print(modified_string)
