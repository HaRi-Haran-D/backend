#OOP - Object Oriented Programming
'''
Python is a versatile programming language that supports various
programming styles, including OOP through the use of objects and classes.

An object is any entity that has attributes and behaviours.
'''

class Parrot:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def green(self):
        print(f'Parrots name is {self.name} and its age is {self.age}')

g=Parrot('goo',2)
g.green()

Class Car:
    def __init__(self,model,year,color,for_sale):
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale

car1 = Car('Audi',2025,'Black',True)


