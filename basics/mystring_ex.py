# strings
# collection of characters
# ' ' (single quotes), " " (double quotes), """ """ (triple quotes)

str1 = 'Hello"s world'
str2 = "Double's quotes hello world"
str3 = """
    Hello World
        This is triple quotes sentence
        hello...
"""

print(str1) # Hello"s world
print(str2) # Double's quotes hello world
print(str3)
#
#    Hello World
#        This is triple quotes sentence
#        hello...
#

str = "hello"

# print single character
print(str[0]) # h

# print multiple characters in single print statement
print(str[0], str[1]) # h e

# print characters from end of string
print(str[-1]) # o 

# slice operation: print character range, giving start and end index
print(str[0:2]) # he

# slice operation: print character range, from 0th index to a given / specific index
print(str[:2]) # he

# slice operation: print character range, from given / specific index to last index
print(str[2:]) # llo

# reverse a string
print(str[::-1]) # olleh --- reverse string from last position (-1)

print(str[::-3]) # oe --- reverse string from position (-3) ?????


# strings are immutable, meaning cannot be modified once initialized
str = "Python" 
# str[0] = "H" # assignment operation not possible as strings are immutable

str = "Python"
str1 = "p" + str[1:] # concatinate 
print(str1)
# python

str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)
# Hello World

print(str1 * 3)
# HelloHelloHello

print("Py" in "Python")
# True

print("java" in "Python")
# False

print("Java" not in "Python")
# True

# len(): no of characters in string
print(len("Python"))
# 6

print("HELLO".lower())
# hello

print("hello".upper())
# HELLO

print("hello".replace("h", "y"))
# yello

print("welcome to python".split(" "))
# ['welcome', 'to', 'python']

print(",".join(["welcome", "to", "python"]).replace(",", " "))
# welcome to python

str = "Python"
for ch in str:
    print(ch)
# P
# y
# t
# h
# o
# n

str = "Data Science"
msg = f"Welcome to {str}" # format
print(msg)
# Welcome to Data Science

print("Hello\nWorld")
# Hello
# World

print("Hello\tWorld")
# Hello   World

print("Welcome to \"Data Science\"")
# Welcome to "Data Science"

print('it\'s Data Science')
# it's Data Science

print("C:\\Python\\DataScience")
# C:\Python\DataScience

str = "Python"
new_str = str.replace("P", "Y")
print(str)
# Python

print(new_str)
# Yython

# Boolean
# True -- 1
# False -- 0
flag1 = True
print(flag1)
# True

flag2 = False
print(flag2)
# False

# True is treated as 1 in python
print(True + 1)
# 2

# False is treated as 0 in python
print(True + False)
# 0

age = 18
if age >= 18:
    print("Adult")
    # Adult
else:
    print("Minor")

print("Adult" if age >= 18 else "Minor")
# Adult

print("Adult" if age > 18 else "Minor")
# Minor

# None -- no value / Nothin / Empty but not zero
x = None
print(x)
# None

print(type(x))
# <class 'NoneType'>

# list: collection of elements
# representation: []
# Mutable, Hetrogeneous, Duplicates, Ordered (elements inserted in order are printed in same order, FIFO)
list1 = [10,50,20,30,40,10,"Hello",True,10.5,None]
print(list1)
# [10, 50, 20, 30, 40, 10, 'Hello', True, 10.5, None]

list2 = [10,20,30,40,50]
print(list2[0])
# 10

# access elements in reverse order
print(list2[-1])
# 50

list2[0]=1000
print(list2)
# [1000, 20, 30, 40, 50]

print(type(list2))
# <class 'list'>

# tuple: collection of elements
# representation: ()
# Immutable, Hetrogeneous, Duplicates, Ordered
t1 = (10,10,20,30,10,True,"Hello",10.5,None)
print(t1)
# (10, 10, 20, 30, 10, True, 'Hello', 10.5, None)

# t1[0] = 1000  --- not possible as tuple is immutable
print(type(t1))
# <class 'tuple'>

# Dictionary: represent data in key & value pair
# representation: {}
d1 = {
    "name": "data science",
    "sub": "Gen AI",
    "cloud": "MLops, LLOps"
}
print(d1["name"])
# data science

d1["sub"] = "Gen AI & Agentic AI"
print(d1)
# {'name': 'data science', 'sub': 'Gen AI & Agentic AI', 'cloud': 'MLops, LLOps'}

del d1["cloud"]
print(d1)
# {'name': 'data science', 'sub': 'Gen AI & Agentic AI'}

print(type(d1))
# <class 'dict'>

# set: collection of elements
# representation: {}
# no duplicates, no order
s1 = {1,1,2,3,1,2,3,None,None}
print(s1)
# {None, 1, 2, 3}

# print(s1[0]) --- does not work as order is not maintained in SET
print(type(s1))
# <class 'set'>

print(len(s1))
# 4

# int
# float
# str
# bool
# list
# tuple
# dict
# set
# None

