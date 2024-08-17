#string format
st = "my name is {} I  am Studying in {} MY Hometown is {}".format("swayam","Dypcet","Kolhapur")
print(st)

a = 'hello kolhapur city '

print("All letters Capital : ",a.upper())

print("Splitting list : ",a.split())

print("first letter Capital of each word : ",a.title())

print("first letter capital of first word only : ",a.capitalize())

print(a.isalpha())

s ="                  hi                   "
print(s)
print(len(s))

print(s.strip())
print(len(s.strip()))

import copy as cp
b="  "
print(b)
b = cp.copy(a)
print(b)

print(b[::-1])
