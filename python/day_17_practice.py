#do a program with a vehicle as parent class and multiple child classes as car, truck and bicycle.
'''
class Vehicle:
    def n1(self):
        print('Vehicle')
class Car(Vehicle):
    def n2(self):
        print('Car')
class Truck(Vehicle):
    def n3(self):
        print('Truck')
class Bicycle(Vehicle):
    def n4(self):
        print('Bicycle')

m = Car()
n=Truck()
o=Bicycle()
m.n1()
m.n2()
n.n1()
n.n3()
o.n1()
o.n4()
'''
#create a base class with vehicle and multiple child classes as car and sports car(in the 3 classes a,b,c a is super class, b is the child class of a and c is the child class of b
'''
class Vehicle:
    def a(self):
        print('Grand Father')
class Car:
    def b(self):
        print('Father')
class Super_car(Vehicle,Car):
    def c(self):
        print('Son')
n=Super_car()
n.a()
n.b()
n.c()
'''
#one child class can inherit from multiple parent classes
'''
class Vehicle:
    def a(self):
        print('Monster Truck')
class Car:
    def b(self):
        print('BMW')
class Super_car(Vehicle,Car):
    def c(self):
        print('Lamborgini')
n=Super_car()
n.a()
n.b()
n.c()
'''
#create a parent class 1 as a person(name,age) parent class 2 as company(company_name,location) class 3 as employee(salary,skill)
class Person:
    def p(self,name,age):
        print(f'Your Name: {name} and you are {age} years old')
class Company(Person):
    def c(self,company_name,location):
        print(f'Your Company Name: {company_name} and it is located in {location}')
class Employee(Company):
    def e(self,salary,skill):
        print(f'Yours Salary {salary} and your skill is {skill}')

n=Employee()
n.p('Hari',25)
n.c('Infosys','Omr')
n.e(25000,'BackEnd')

#create a class name vehicle  seats, capacity,amount fair total value
