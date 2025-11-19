#Inheritance
#inheritance means the process of achieveing and accessing the functions and attributes of the base class from its different derived
    #class is called inheritance
#base class is parent class
#derived class is child class
#types of inheritance
#single inheritance
#multiple inheritance
#multilevel inheritance
#hierarchical inheritance

#single inheritance
#if a child class is inheriting the properties and attributes of a single parent class is called as single inheritance.
'''
class Library:
    def f1(self):
        print('Library')
        
class Science(Library):
    def f2(self):
        print('Library Science')

s=Science()
s.f1()
s.f2()
'''

#multiple inheritance
#if a child class inherits the properties and behaviour of more than one class is called multiple inheritance.
'''
class Library:
    def f1(self):
        print('Library 1')
class Science:
    def f2(self):
        print('Library 2')
class Shelter(Library,Science):
    def f3(self):
        print('Library 3')

s=Shelter()
s.f1()
s.f2()
s.f3()
'''

'''
class User:
    def __init__(self,name,password):
        self.name = name
        self.password = password
class Login(User):
    def input2(self,name1,password1):
        if self.name == name1 and self.password == password1:
            print('Login Successful')
        else:
            print('Login Failed')
        

n = Login('hari',1234)
n.input2('hari',1234)
'''

#multilevel inheritance
#if a child class will become a super class for another child class is called multi level inheritance.
'''
class Library:
    def f1(self):
        print('Grand')

class Shelter(Library):#child one
    def f2(self):
        print('Parent')
        
class Science(Shelter):#child 2 which access 
    def f3(self):
        print('Child')

a = Science()
a.f1()
a.f2()
a.f3()
'''
#hierarchical inheritance
#if multiple inheritance occurs within same child class base class is called as hierarchical inheritance 
'''
class Library:
    def f1(self):
        print('Parent')
class Shelter(Library):
    def f2(self):
        print('Child1')
class Science(Library):
    def f3(self):
        print('Child2')

m = Shelter()
m.f1()
m.f2()
n = Science()
n.f1()
n.f3()
'''

'''
Method:
    1. method name can be anything
    2. methods wont be executed automatically,we have to call explicitly.
    3. per object we can call method any no of times.
    4. we can write business logic based on our programming requirement.

constructor:
    1. means name should be _init_
    2. constructors will be called automatically whenever we are creating a object
    3. per object constructor will be executed only once.
    4. Inside const we have to write a code to declare and initialize.
'''


'''
in inheritance all members available in parent class are the default values in the child class, if the child class does not satisfy with the
parent class implementation, then the child classs is allowed to redefine the method by extending additional function in the child class is
said to be an method override that is when the child class method has same name same parameter and same return type(function) then
that method in the class is said to be override the method in the parent class.
'''

class Vehicle:
    def max_speed(self):
        print('Above 50')
class  Car:
    def max_speed(self):
        print('Above 80')

s=Car()
s.max_speed()

class Shapes:
    def draw(self):
        print('We can draw shapes')
class Square(Shapes):
    def draw(self):
        print('Redefining the parent class')

n=Square()
n.draw()






