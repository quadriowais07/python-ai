# oops - object oriented programming system
# class - collection of variables & functions
# class - keyword used to declare the class

class Test:
    def wish(self): # self represent current class object (Ex 'this' in java)
        print('welcome to oops!!')

t1 = Test() # creating the object
t1.wish()   # welcome to oops!!

class Test:
    # no param - no return type
    def add1(self):
        num1 = 200
        num2 = 100
        res = num1 + num2
        print(f"Addition: {res}")
    
    # no param - with return type
    def add2(self):
        num1 = 200
        num2 = 100
        res = num1 + num2
        return res
    
    # with param - no return type
    def add3(self, num1, num2):
        res = num1 + num2
        print(f'Addition: {res}')

    # with param - with return type
    def add4(self, num1, num2):
        res = num1 + num2
        return res

t1 = Test()
t1.add1()

x = t1.add2()
print(f'Addition: {x}')

t1.add3(200, 100)

y = t1.add4(200, 100)
print(f'Addition: {y}')


# instance variables
# __init__() called as constructor
# it will execute only once
# whenever we create object, automatically contructor will execute

class Test:
    def __init__(self): # class constructor
        self.num1 = 10
        self.num2 = 20

t1 = Test()
t2 = Test()

t1.num1 = 100
t1.num2 = 200

print(f't1 object data: {t1.num1}...{t1.num2}')
print(f't2 object data: {t2.num1}...{t2.num2}')


# class variables, shared to multiple objects
class Test:
    company = "TCS" # class variable (same variable shared to instances)

    def __init__(self, name):
        self.name = name

t1 = Test("Emp1")
print(f'name of the employee: {t1.name} and company name: {t1.company}')

t2 = Test("Emp2")
print(f'name of the employee: {t2.name} and company name: {t1.company}')

class Test:
    name = "TCS"

t1 = Test()
t2 = Test()
print(f'Name .. {t1.name}')
print(f'Name .. {t2.name}')

Test.name = "Oracle"
print(f'Name .. {t1.name}')
print(f'Name .. {t2.name}')


class Test:
    name = "Microsoft"

t1 = Test()
t2 = Test()

print(f'Name .. {t1.name}')
print(f'Name .. {t2.name}')

t1.name = "Google" # add instance variable to t1 object
print(f'Name .. {t1.name}')
print(f'Name .. {t2.name}')

# modify class variable using @classmethod decorator
class Test:
    company = "TCS"
    def __init__(self, name):
        self.name = name
    
    @classmethod # decorator - used to modify class variable
    def change_company(cls, new_company):
        cls.company = new_company

Test.change_company("Oracle")
t1 = Test("Google")
t2 = Test("Microsoft")
print(f'Company .. {Test.company}') # Oracle
print(f'Company .. {Test.company}') # Oracle

Test.change_company("Microsoft")
print(f'Company .. {Test.company}') # Microsoft
print(f'Company .. {Test.company}') # Microsoft


# first priority - object level
# next priority - class level
class Test:
    name = "hello" # class variable

    def __init__(self, name):
        self.name = name

t1 = Test("Sample1")
print(t1.name) # sample 1


# first priority - object level
# next priority - class level
class Test:
    name = "hello" # class variable

    def __init__(self, name):
        # self.name = name
        pass

t1 = Test("Sample1")
print(t1.name) # hello

# __ is used to declare the private variables
# Encapsulation
# private variable cannot be accessed outside class
# private variables unable to access with class object
class Test:
    def __init__(self):
        self.__amount = 50000 # __amount is private variable
    def display_amout(self):
        return self.__amount

t1 = Test()
# t1.__amount -- will throw error -- Test' object has no attribut
print(t1.display_amout())
print(t1._Test__amount) # accessing private variable from internal memory itself


class Parent:
    def test1(self):
        print("Parent..")

class Child(Parent):
    def test2(self):
        print("Child..")

p1 = Parent()
p1.test1()

c1 = Child()
c1.test1()
c1.test2()


# multi level inheritance
class Parent:
    def test1(self):
        print("Parent..")

class Child(Parent):
    def test2(self):
        print("Child...")

class Subchild(Child):
    def test3(self):
        print("Subchild....")

sc = Subchild()
sc.test1()
sc.test2()
sc.test3()


# Multiple inheritance
class Parent1:
    def test(self):
        print("Parent 1 ..")

class Parent2:
    def test(self):
        print("Parent 2 ..")

class Child(Parent1, Parent2):
    pass

obj = Child()
obj.test() # Parent 1 ..

class Parent1:
    pass

class Parent2:
    def test(self):
        print("Parent 2 ..")

class Child(Parent1, Parent2):
    pass

obj = Child()
obj.test() # Parent 2 ..


# polymorphism - behaves like many
# 2 types
# 1. Overloading 2. Overriding

# Overriding
# Overriding parent class funcationality with child class functionality

class Parent:
    def db_conn(self):
        print("SQL connection soon..")

class Child(Parent):
    def db_conn(self):
        print("NoSQL connection soon..")

obj = Child()
obj.db_conn() # NoSQL connection soon..

obj = Parent()
obj.db_conn() # SQL connection soon..


# Overloading is not supported by Python
# Below example exhibits as overloading
class Test:
    def add(self, a, b=0, c=0):
        print(a+b+c)

obj = Test()
obj.add(10) # 10
obj.add(10,20) # 30
obj.add(10,20,30) # 60


class Test:
    def add(self, *args):
        print(type(args)) # <class 'tuple'>
        print(args) # (10, 20, 30)
        print(sum(args))

obj = Test()
obj.add(10, 20, 30) # 60
obj.add(10) # 10


# overloading
class Test:
    def add(self, num1=None, num2=None, num3=None):
        if num1 and num2 and num3:
            print(num1 + num2 + num3)
        elif num1 and num2:
            print(num1 + num2)
        elif num1:
            print(num1)
        else:
            print(0) # 0

obj = Test()
obj.add(10) # 10
obj.add(10, 20) # 30
obj.add(10, 20, 30) # 60
obj.add() # 0


class Test:
    def __init__(self, num1):
        self.num1 = num1
    
    def __add__(self1, self2): # add is predefind function. It starts with '__'
        return self1.num1 + self2.num1

n1 = Test(10)
n2 = Test(20)

print(n1 + n2) # 30


# prints the hashcode of object
class Test:
    pass

obj = Test()
print(obj) # <__main__.Test object at 0x0000022A6F559FA0>


# Dunder methods
# override the hashcode
class Test:
    def __str__(self):
        return "Welcome"

obj = Test()
print(obj) # Welcome


# abstract method
# abc - package
# ABC - class
# abstractmethod - decorator
from abc import ABC, abstractmethod
class Business(ABC):
    @abstractmethod
    def start_business(self):
        pass

class Friend(Business):
    def start_business(self):
        print("Initiate AI Startup company")

obj = Friend()
obj.start_business() # Initiate AI Startup company


# call parent fn from child fn
class Parent:
    # def test1(): -- static method
    # def test1(cls): -- class method
    # def test1(self): -- instance method
    def test1(self):
        print("hello")

class Child(Parent):
    def test2(self):
        super().test1()

obj = Child()
obj.test2()


# child class fn calling parent class fn
class Parent:
    def __init__(self, param1):
        self.param1 = param1

class Child(Parent):
    def __init__(self, param1, param2):
        super().__init__(param1)
        self.param2 = param2

obj = Child(200, 100)
print(obj.param1 + obj.param2) # 300


# static methods
# won't use "self" and "cls"
# declared inside the class with the help of decorator
# @staticmethod
# we will call with the help of class name
# to declare utility methods (general purpose methods)
# Ex. validations, ..

class Test:
    @staticmethod
    def greet():
        print('welcome to static method')

Test.greet() # welcome to static method

# even without decorator this is working, why?
# ChatGPT says it risky to not use decorator
# It will work but it is not a true static method
# python MAY pass self and make it a instance method


class MathUtils:
    @staticmethod
    def square(num1):
        # return num1*num1
        # return pow(num1, 2)
        return num1 ** 2
    
    @staticmethod
    def cube(num1):
        # return num1*num1*num1
        # return pow(num1, 3)
        return num1 ** 3
    

print(MathUtils.square(10)) # 100
print(MathUtils.cube(20)) # 



"""
                instance        class           static

self            yes             no              no
cls             no              yes             no
no keyword      no              no              yes
decorator       no              @classmethod    @staticmethod
access data     using obj       using class     using class

usecase         obj             share           common logic /
                related         data            utility logic /
                task            to all          helper logic
                                objects
"""


class Test:
    # class level variable
    company_name = "Oracle"

    # constructor
    def __init__(self, name):
        self.name = name
    
    # instance method
    def test(self):
        print(self.name)
    
    # class method
    @classmethod
    def change_company_name(cls, new_company_name):
        cls.company_name = new_company_name
    
    # static method
    @staticmethod
    def is_major(age):
        return age >= 18

obj = Test("emp1")
obj.test() # emp1

# Test.test() -- error: instance method not allowed to call by class name

print(Test.company_name) # Oracle
Test.change_company_name("Microsoft")
print(Test.company_name) # Microsoft

# it is possible to call class method using object in Python
# but this illegal. We should avoid this practice
# if instance method does not exist with this name,
# then it will the static method
obj.change_company_name("BCBSM")
print(Test.company_name) # BCBSM

print(Test.is_major(20)) # True


# class
# object
# instance
# cls
# static
# abstract
# inheritance
# polymorphism
# super

