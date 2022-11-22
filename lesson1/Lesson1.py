
a = float(input("x= "))
b = float(input("y= "))
su = a+b
difference = a-b
mult = a*b
expon = a**b
modul = a % b
proc = a//b
print(su, difference, mult, expon, modul, proc)

x = (17/2*3)+2
print(x)
x = 2+(17/2*3)
print(x)
x = (19 % 4)+(15/2*3)
print(x)
x = (15+6)-(10*4)
print(x)
x = (17/2) % 2*(3**3)
print(x)

import math
x = float(input("x= "))
y = float(input("y= "))
x = math.fabs(x)
y = math.fabs(y)
summ = (x-y)/(1+x*y)
print(summ)

string = "aaaaaBccBddBeeBffBggB"
print(string[5::3])

string_one = "AAAABBBBCCCCDDDDFFFF"
str_a = string_one[0:4]
str_b = string_one[4:8]
str_c = string_one[8:12]
str_d = string_one[12:16]
print(str_a, str_b, str_c, str_d)
print(str_a+str_b+str_c+str_d)


string_two = "PYTHON"
print(string_two[::-1])

print(len(string_one))
print(string_one[-5])
