#polymorphism
#operator overriding

class Box:
    def __init__(self,length):
        self.length=length

    def __add__(self,other):
        return Box(self.length + other.length)

b1=Box(10)
b2=Box(20)
b3=b1+b2
print(b3.length)

class Salary:
    def __init__(self,salary):
        self.salary=salary
    def __mul__(self,other):
        return Salary(self.salary * other.salary)
a1=Salary(10)
a2=Salary(28)
a3=a1*a2
print(a3.salary)

#Method Overriding
#it means it refers defining a method in a subclass with its same name as a method as a sub class
# this is said to run time poly we can always overwrite your parent class method when you have
# special or different   that is i as to change and exchange the parent class behaviours to change
# parent class behaviour

#to extend parent class behaviour
#to achieve runtime polymorphism

class Parent:
    def show(self):
        print('This is parent')
    def display(self):
        print('display parent')

class Child(Parent):
    def show(self):
        print('This is child')
    def display(self):
        super().display()
        print('display child')

a=Child()
a.show()
a.display()

#regular expression
#we are going to 












