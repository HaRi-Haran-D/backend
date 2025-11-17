#oops: class and object
#class name's first letter should be in uppercase
#class name must be meaningful
#class attribute must be unique
#for one class we can create multiple objects
#after class declaration we can declare class variable and instance variable
#class variable will be declared inside the class and outside the __init__ constructor function
#






'''
class Student:
    institute = 'SLA'
    def __init__(self,name,course):
        self.name=name
        self.course=course
    def show(self):
        print(f'Student Name: {self.name} and Course: {self.course} in {self.institute}')
obj1 = Student('Hari','Python')
obj2 = Student('Suriya','Mern')

obj1.show()
obj2.show()

print(obj1.name)#accessing individual value of instance variable
print(obj2.course)

print(Student.institute)#accessing class variable
'''

class Employee:
    def __init__(self,emp_id,name,department,salary,city):
        self.emp_id=emp_id
        self.name=name
        self.department=department
        self.salary=salary
        self.city=city
    def increment(self):
        new_salary = self.salary+(self.salary*0.07)
        return new_salary
    def display(self):
        print(f'{self.emp_id},{self.name},{self.department},{self.salary},{self.city}')
        print('Your current salary after increment',self.increment())

details1=Employee(1,'Hari','Store',15000,'OMR')
details2=Employee(1,'Vijay','Service',17000,'T.nagar')

details1.display()
details2.display()

#self keyword is the first parameter among the rest of the parameter
#it is not possible to give value to self keyword directly during program execution interpreter will pass the values
#self keyword is used to represent the instance of the class(object)
#self keyword is used to bind the attributes with the given arguments
#instead of self we can pass any name to it
#it is used in method definition and variable declaration
#self = to access the current object we use self keyword

class Institute:
    def __init__(key,name,place,trainer):
        key.name=name
        key.place=place
        key.trainer=trainer
    def display(key):
        print(f'Institute Name {key.name} in {key.place} and your trainer {key.trainer}')

sla1=Institute('softlogic','kk nagr','python-trainer')
sla1.display()

sla1=Institute('','kk nagr','python-trainer')
sla1.display()

#__init__()constructors:
#1. Constructor is a special method
#2. The name constructor is always ___init__()
#3. we are not required to call constructor explicitly.it will be executed
#4. it will be executed automatically when we create an object
#5. per object constructor will be executed only once
#6. main purpose of constructor is to declare and initialize instance variable
#7. __init__means initialization
#8. self refers to current object
#9. constructor should take one argument(self)to refer current object




