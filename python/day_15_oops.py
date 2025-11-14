#oops - object oriented programming language
#real world things: business logic
#encapsulation
#parent - multiple inheritance
#data abstraction
#polymorphism - many ideas
#base classes and objects


#class

#a class is the internal datamodel references of itself
#it is a prototype to creating an object
#user defined structure to create an object
#prototype which allow creating new object with data model
#otherwise we can say class is a collection of
#1. states and behaviour
#2. data and function
#3. variables and members
#4. data variable and member function
#5. properties and methods

#how to declare a class in python
#class following name and the name first letter must be in uppercase


class Student:
    def __init__(self,name,city):
        self.name=name
        self.city=city
    def display(self):
        print('Iam',self.name)
        print('from',self.city)
obj1=Student('Hari','Ambattur')
#obj1 - object
#= operator obj=classname
#class(args)
obj1.display()
#accessing the object values
