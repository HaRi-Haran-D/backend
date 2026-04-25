"""
class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name, self.age)

obj = Student("Hari", 23)
obj.show()
"""

"""
class Car():
    def __init__(self, wheels, mileage, airbags):
        self.wheels = wheels
        self.mileage = mileage
        self.airbags = airbags
    def moveforward(self):
        return f"Car is moving forward"

    def movebackward(self):
        return f"Car is moving backward"

    def show(self):
        print(self.wheels, self.mileage, self.airbags)
obj = Car(wheels=10, mileage=20, airbags=5)
print(obj.moveforward())
print(obj.movebackward())
print(obj.show())

obj1 = Car(wheels=10, mileage=30, airbags=5)
print(obj1.moveforward())
print(obj1.movebackward())
print(obj1.show())
"""
"""
class Bank():
    def __init__(self, name, balance, acc_no):
        self.name = name
        self.balance = balance
        self.acc_no = acc_no

    def show(self):
        print(self.name)

c1 = Bank(name = "Hari", balance = 100, acc_no = "6764")
c1.show()
"""


class Person():
    def __init__(self,name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"

    def show(self):
        message = self.greet()
        return (message, "Welcome")

obj = Person("Hari")
print(obj.show())