# Fucntion: Business logic (or) Block of statements
# "reuse" the business logic
# def is the keyword, used to declare the function

# Example - 1
def func_one():
    # Empty function by adding pass keyword.
    pass

# calling function
func_one()


# Example - 2
def func_one():
    print("welcome to functions !!!")
    # welcome to functions !!!

func_one()


# No parameters - no return type
def addtion():
    n1 = 200
    n2 = 100
    res = n1 + n2
    print(f"Addition: {res}")
    # Addition: 300

addtion()

# No parameters - with return type
def substraction():
    n1 = 200
    n2 = 100
    res = n1 - n2
    return res

x = substraction()
print(f"Substraction: {x}")
# Substraction: 100
print(type(substraction))
# <class 'function'>

# with parameters - no return type
def multiplication(n1, n2):
    res = n1 * n2
    print(f"Multiplication: {res}")
    # Multiplication: 20000

multiplication(200, 100)

# with parameter - with return type
def division(n1, n2):
    res = n1 / n2
    return res

x = division(200, 100)
print(f"Division: {x}")
# Division: 2.0

print("-------------recursion start----------")
def rec_fn(x):
    return 1 if x == 0 or x == 1 else x * rec_fn(x-1)

print(rec_fn(5))
# 120
print("-------------recursion end------------")


def db_conn(username, password, db_name):
    return "Oracle conn soon..!" if username == "scott" and password == "scott" and db_name == 'oracle' else "Connection error...!"

res = db_conn("scott", "tiger", "oracle")
print(res)
# Connection error...!

res = db_conn("scott", "scott", "oracle")
print(res)
# Oracle conn soon..!

def db_conn_2(username, password, db_name):
    if db_name == "oracle":
        if username=="scott" and password=="tiger":
            return "Oracle Connection soon"
    elif db_name == "mysql":
        if username == "admin" and password == "admin@123":
            return "MySQL connection soon"
    else:
        return "Conn Err"

conn = db_conn_2("scott","tiger","oracle")
print(conn)
# Oracle Connection soon

conn1 = db_conn_2("admin", "admin@123", "mysql")
print(conn1)
# MySQL connection soon


# Default arguments
def func_one(n1 = 200, n2 = 100):
    res = n1 + n2
    print(res)

func_one()
# 300
func_one(300)
# 400
func_one(300, 400)
# 700
# func_one(None, None) unsupported operand type(s) for +: 'NoneType' and 'NoneType'
func_one(True, False)
# 1
func_one(True)
# 101


def func_one(n1, n2):
    print(n1, n2)
    # 200 100

func_one(n2=100, n1=200)
# func_one(num1=100, num2=200) parameters name must match

# variable argument
# data stored in the form of tuple
def func_one(*param1):
    print( type(param1) )
    print( sum(param1) )

func_one(10)
# <class 'tuple'>
# 10

func_one(10,20,30,40,50)
# <class 'tuple'>
# 150

# function without name called as Lambda fn / Anonymous fn
# "lambda" is the keyword, is used to declare lambda / anonymous fn
# square is identifier used to hold anonymus fn
square = lambda num: num*num
print( square(10) )
# 100

check = lambda x: "Even" if x%2 == 0 else "Odd"
print( check(10) )
# Even
print( check(9) )
# Odd

# multiple variables in lambda
addtion = lambda num1, num2 : num1 + num2
print( addtion(200, 100) )
# 300

# map fn is used to manipulate every element
# map is immutable fn
# [10, 20, 30, 40] -----> [100, 200, 300, 400]
print("----------- map --------------")
nums = [10, 20, 30, 40, 50]
print(list(map ( lambda x: x*10, nums )))
# [100, 200, 300, 400, 500]
print(list(map ( lambda x: x*10 if x<30 else x, nums )))
[100, 200, 30, 40, 50]
print("----------- map --------------")

# filter function
# filter() - used to apply conditions
# filter is immutable fn
nums = [10, 15, 20, 25, 30]
print(list( filter( lambda num: num%10 == 0, nums)))
# [10, 20, 30]


# nested Lambda
multiply = lambda num1: (lambda num2: num1*num2)
print( multiply(10)(20) )
# 200
division = lambda num1: (lambda num2: num1/num2 if num2>0 else "Cannot divide by zero")
print( division(10)(20) )
# 0.5
print( division(10)(0) )
# Cannot divide by zero


# list - []; tuple - (); dict - {};
# sorted() is the predefined fn used to sort the list data
stds = [("std1", 90, 5),
        ("std2", 80, 4),
        ("std3", 99, 3),
        ("std4", 70, 2),
        ("std5", 98, 1)]
res = sorted(stds, key=lambda x: x[2])
print(res)
# [('std5', 98, 1), ('std4', 70, 2), ('std3', 99, 3), ('std2', 80, 4), ('std1', 90, 5)]
res = sorted(stds, key=lambda x: x[1])
print(res)
# [('std4', 70, 2), ('std2', 80, 4), ('std1', 90, 5), ('std5', 98, 1), ('std3', 99, 3)]
res = sorted(stds, key=lambda x: x[1], reverse=True)
print(res)
# [('std3', 99, 3), ('std5', 98, 1), ('std1', 90, 5), ('std2', 80, 4), ('std4', 70, 2)]

data = {"num1": 10,
        "num2": 40,
        "num3": 20,
        "num4": 30}
res = sorted(data.items(), key=lambda x: x[1])
print(res)
# [('num1', 10), ('num3', 20), ('num4', 30), ('num2', 40)]
res = sorted(data.items(), key=lambda x: x[1], reverse=True)
print(res)
# [('num2', 40), ('num4', 30), ('num3', 20), ('num1', 10)]

# max() - predefined fn; used to find highest element
nums = [5, 12, 8, 20]
print( max(nums, key=(lambda x: x)) )
# 20


func = lambda x: "High" if x > 80 else ( "Medium" if x > 50 else "Low" )
print(func(90))
# High
print(func(60))
# Medium

def students(**data): # {'name': 'std1', 'marks': 90}
    print(data)

students(     name="std1", marks=90    )
# {'name': 'std1', 'marks': 90}


