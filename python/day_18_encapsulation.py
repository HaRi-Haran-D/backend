#super()
#super method is used when you want the child class to use the parent class's variable and methods without rewriting the original code.
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def display1(self):
        print(f'Name: {self.name} Age: {self.age}')

class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
        
    def display2(self):
        super().display1()
        print(f'Rollno: {self.rollno} Mark: {self.marks}')

class Teacher(Person):
    def __init__(self,name,age,salary,subject):
        super().__init__(name,age)
        self.salary=salary
        self.subject=subject
    def display(self):
        super().display1()
        print(f'Salary: {self.salary} Subject: {subject}')

st=Student('Hari',25,123432,12)
st.display2()
'''

#Encapsulation
#encapsulation means rapping up of data and method in a single unit is called as encapsulation.
'''
class Student:
    def __init__(self,name,age,dept):#data member
        self.name = name
        self.age = age
        self.dept = dept
    def show(self):#member function
        #access the data member
        print(f'Name: {self.name} Age: {self.age}')
    def show1(self): #member function
        print(f'Name: {self.name} Dept: {self.dept}')
#data member access
s= Student('Hari',25,'BCA')
s.show()
s.show1()
'''

'''
data encapsulation allows to user to restrict the access variable and methods
directly and prevent accidental data modification bycreating private data
member and method within the class.

Types of Encapsulation
1. public access specifiers - they can able access any were inside the code
2. private access specifiers - they can be only access within the class
3. protected access specifiers - accessable within its class and its sub class
'''

#Public access specifiers
#if a member (either method or  
'''
class Test:
    def __init__(self):
        self.x=10 #instance variable (public)
    def m1(self):
        print('This is public method')
        #by default every method present in python class  instance variable
    def m2(self):
        print(self.x)
        self.m1()

p=Test()
p.m2()
#outside of the class also we can access a value
print(p.x)
p.m1()
#so, anywhere we can access instance variable
'''

'''
class Emp:
    def __init__(self):
        self.name='Hari'
        self.salary=20000
    def disp(self):
        print('Name: ',self.name)

d=Emp()
d.disp()
print(d.name)
'''

#Protected Access Specifiers
'''
protected members we can access within the class from anywhere but from outside of the class we
can access only in child classess or sub class.

we can declare members are protected explicitly by prefixing with single underscore symbol (_)
( __ ) leading underscore is private
'''

class Test:
    def __init__(self):
        self._x=10 #Protected Variable
        
    def m1(self):
        print(self._x)

class Subtest(Test):
    def m2(self):
        print(self._x)

t=Subtest()
t.m1()
t.m2()
print(t._x)




























