#Inheritance
#it allows a class to inherit attribute and methods from another class
#helps with code reusability and extensibility

class Animal:
    def __init__(self,name):
        self.name=name
        self.alive=True
    def eat(self):
        print(self.name,'is Eating')
    def sleep(self):
        print(self.name,'is sleeping')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Rat(Animal):
    pass

a=Dog('A')
b=Cat('B')
c=Rat('C')

a.eat()
a.sleep()
print(a.name)
print(a.alive)

print('')
print('*'*43)
print('')

b.eat()
b.sleep()
print(b.name)
print(b.alive)

print('')
print('*'*43)
print('')

c.eat()
c.sleep()
print(c.name)
print(c.alive)
