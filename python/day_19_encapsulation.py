'''
class Park:
    def __init__(self,swings,benches):
        self.swings=swings
        self.benches=benches
    def display(self):
        print(f'Swings: {self.swings} and Benches: {self.benches}')
p=Park(2,5)
p.display()
print(p.swings)

p1=Park(4,8)
p1.display()
print(p1.benches)
'''
#private access specifiers can acces variables and methods only within class
#declaration of private variable
'''
class Park:
    def __init__(self):
        self.swing=10
        self.benches=12
        self.__entry_fee=50
        self.__security_code='Pass123'
    def use_swing(self):
        print('swing count',self.swing)
    def use_balance(self):
        print('bench count',self.benches)
    def show(self):
        print('Entry fee:',self.__entry_fee)#private variable
        print('Security code',self.__security_code)#private variable

p=Park()
p.use_swing()
p.use_balance()
p.show()#this is not private method
print(p._Park__entry_fee)#accessing private variable value
'''

'''
class Institute:
    def __init__(self):
        self.companyName="SLA"
        self.branches="KK Nagar and Navalur"
        self.__std_count_kknagar=103
        self.__std_count_navalur=123
    def branch(self):
        print(f'Institute Name: {self.companyName} and Branches {self.branches}')
    def count(self):
        print(f'Students count in KK Nagar {self.__std_count_kknagar}')
        print(f'Students count in KK Nagar {self.__std_count_navalur}')

n=Institute()
n.branch()
n.count()
print(n._Institute__std_count_kknagar)
print(n._Institute__std_count_navalur)
'''
'''
class Employee:
    def __init__(self):
        self.name="Hari"
        self._salary=25000
    def details(self):
        print('Employee Name:',self.name)

class Salary(Employee):
    def full_detail(self):
        print(f'Employee Name:{self.name} and his salary {self._salary}')

n=Salary()
n.details()
n.full_detail()
print(n._salary)
'''

#data abstraction
#abstraction means taking necessary action and hides the unwanted program implemention is called as data abstraction

#abstract method
#somtimes we don't know about the implementation, still we can declare a method such type of method is called as abstract method that is abstract has only declaration no implementation
#in python we declare abstract with help of @abstractmethod
#@abstractmethod module is present inside the abc module
#import abc module

#abstract class
#abstract class sometimes implementation of a class is not completion is partially implememted classes are abstract class
#import ABC module
#every abstract class in python should be accessed with the help of child class ABC module
#ABC - Abstract Base Class

from abc import ABC,abstractmethod
class Sample(ABC):
    @abstractmethod
    def f1(self):
        print('Abstract Method')
    def f2(self):
        print('Child method')

class Child(Sample):
    def f1(self):
        super().f1()

p=Child()
p.f1()
p.f2()


#polymorphism
#it means 
#Types
#operator overloading
#operator overriding
#method overloading
#method overriding








        
