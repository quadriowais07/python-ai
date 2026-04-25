"""
### ------ Dictionary --------
### Represent data in key value pair
### It is mutable (can modify data)
### Unordered (<3.7), ordered (3.7+)
"""


d1 = {"num1": 200, "num2": 100}
print(d1)
# {'num1': 200, 'num2': 100}

d2 = dict(num1=200, num2=100)
print(d2)
# {'num1': 200, 'num2': 100}

d3 = dict([("num1",200),("num2",100)])
print(d3)
# {'num1': 200, 'num2': 100}

d4 = {}
print(d4)
# {}

d1 = {"num1":100,"num2":200}
# access the data
print(d1["num1"])
# 100

# print(d1["num3"]) --- Gives error. Not safe reading
# KeyError: 'num3'

print(d1.get("num3")) # Does not give error
# None

d1["num3"] = 300
d1["num1"] = 1000
d1.update({"num2":2000,"num3":3000})
print(d1)
# {'num1': 1000, 'num2': 2000, 'num3': 3000}


# delete
del d1["num1"]
print(d1)
# {'num2': 2000, 'num3': 3000}

print(d1.pop("num2")) # delete and return value
# 2000

d1.popitem()
print(d1)
# {}

d1 = {"num1": 200, "num2": 100}
d1.clear()
print(d1)
# {}

d1 = {"num1": 200, "num2": 100}
for k in d1:
    print(k)
# num1
# num2

for v in d1.values():
    print(v)
# 200
# 100

for k,v in d1.items():
    print(f"Key: {k}, Value: {v}")
# Key: num1, Value: 200
# Key: num2, Value: 100

print(d1.keys())
# dict_keys(['num1', 'num2'])

print(d1.values())
# dict_values([200, 100])

print(d1.items())
# dict_items([('num1', 200), ('num2', 100)])

d1 = {x:x*x for x in range(5)}
print(d1)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

d1 = {x:x*x for x in range(5) if x%2 == 0}
print(d1)
# {0: 0, 2: 4, 4: 16}

students = {
    "s1": {"name": "std1", "marks": 90},
    "s2": {"name": "std2", "marks": 80}
}
print(students["s1"]["marks"])
# 90

d1 = {
    "num1": 100
}
d2 = d1.copy() # deep / ref copy
d1["num1"] = 1000
print(d1)
# {'num1': 1000}
print(d2)
# {'num1': 100}

d2 = d1 # shallow copy
print(d1)
# {'num1': 1000}
print(d2)
# {'num1': 1000}

# keys names allowed (int, float, string, tuple)
# keys not allowed (list, dict)
d1 = {
    10: "Hello",
    10.1: "Welcome",
    10.1: "Bye",
    "str1": "Python",
    (1,2): "Dict",
    True: "Hi",
    None: "Hello"
}
print(d1)
# {10: 'Hello', 10.1: 'Bye', 'str1': 'Python', (1, 2): 'Dict', True: 'Hi', None: 'Hello'}


# d1 = {
#     [10,20]: "Hello" --- List is not allowed for keys
# }
# TypeError: unhashable type: 'list'

str = "aabbcc"
freq = {}
for ch in str:
    # get fun returns None if value is not present
    # instead of None, return 0
    # 1 is added to returned value 0
    freq[ch] = freq.get(ch,0) + 1

print(freq)
# {'a': 2, 'b': 2, 'c': 2}

d1 = {"a": 3, "b": 1, "c": 2}
print( sorted(d1.items(), key=lambda x: x[1]) )
# [('b', 1), ('c', 2), ('a', 3)]




