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

print(str[0]) # h
print(str[0], str[1]) # h e
print(str[-1]) # o
print(str[0:2]) # he
print(str[:2]) # he
print(str[2:]) # llo
print(str[::-1]) # olleh --- reverse string from last position (-1)
print(str[::-3]) # oe --- reverse string from position (-3) ?????


str = "Python" # strings are immutable, meaning cannot be modified once initialized
# str[0] = "H" # assignment operation not possible as strings are immutable

str = "Python"
str1 = "p" + str[1:] # concatinate 
print(str1)

str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)
print(str1 * 3)

print("Py" in "Python")
print("Java" not in "Python")

print(len("Python"))
print("HELLO".lower())
print("hello".upper())
print("hello".replace("h", "y"))
print("welcome to python".split(" "))
print(",".join(["welcome", "to", "python"]).replace(",", " "))


str = "Python"
for ch in str:
    print(ch)

str = "Data Science"
msg = f"Welcome to {str}" # format
print(msg)

print("Hello\nWorld")
print("Hello\tWorld")
print("Welcome to \"Data Science\"")
print('it\'s Data Science')
print("C:\\Python\\DataScience")

str = "Python"
new_str = str.replace("P", "Y")
print(str)
print(new_str)

# Boolean
# True -- 1
# False -- 0
flag1 = True
print(flag1)
flag2 = False
print(flag2)
print(True + 1)
print(True + False)

age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")

print("Adult" if age >= 18 else "Minor")
print("Adult" if age > 18 else "Minor")

# None -- no value / Nothin / Empty but not zero
x = None
print(x)
print(type(x))

# list
# collection of elements
# []
# Hetrogeneous
# Duplicates
# Ordered (elements inserted in order are printed in same order)
# mutable
list1 = [10,50,20,30,40,10,"Hello",True,10.5,None]
print(list1)
list2 = [10,20,30,40,50]
print(list2[0])
print(list2[-1])
list2[0]=1000
print(list2)
print(type(list2))

# tuple
# collection of elements
# ()
# Hetrogeneous
# Duplicates
# Ordered
# immutable
t1 = (10,10,20,30,10,True,"Hello",10.5,None)
print(t1)
# t1[0] = 1000  --- not possible as tuple is immutable
print(type(t1))

# Dictionary
# represent data in key & value pair
d1 = {
    "name": "data science",
    "sub": "Gen AI",
    "cloud": "MLops, LLOps"
}
print(d1["name"])
d1["sub"] = "Gen AI & Agentic AI"
print(d1)
del d1["cloud"]
print(d1)
print(type(d1))

# set
# collection of elements
# {}
# no duplicates
# no order
s1 = {1,1,2,3,1,2,3,None,None}
print(s1)
# print(s1[0]) --- does not work as order is not maintained in SET
print(type(s1))
print(len(s1))


# int
# float
# str
# bool
# list
# tuple
# dict
# set
# None

