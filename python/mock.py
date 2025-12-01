#1. Person Class with Age Calculation
#Write a Python program to create a person class. Include attributes like name, country and
#date of birth. Implement a method to determine the person's age.

'''class Person:
    date=2025
    def __init__(self,name,country,dob):
        self.name = name
        self.country = country
        self.dob = dob
    def display(self):
        self.date-=self.dob
        print(f'Your Name: {self.name} your country {self.country} your age {self.date}')
a=Person('Hari','India',1999)
a.display()
              
#2. Program to append elements to the list.
list1=[1,2,3,4,5]
list2=[6,7,8]
list1+=list2
print(list1)

#3. Program to extend the list.
a=[1,'as','bin',43,6]
b=['in',12,34]
a+=b
print(a)
'''

'''
#4. Program to insert an element at the specific position.
list1=[1,2,3,4,5]
value=5
list2=[]

for i in list1:
    if i < 4:
        list2.append(list1[i-1])
    elif i == 4:
        list2.append(i)
    else:
        list2.append(i)
print(list2)
'''

'''
#5. Python program to create a calculator class. Include methods for basic arithmetic operations
class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)
        
    def sub(self):
        print(self.a-self.b)

    def multi(self):
        print(self.a*self.b)

    def div(self):
        if self.a <=0 or self.b <= 0:
            print("Invalid")
        else:
            print(self.a/self.b)
a=Calc(15,5)
a.add()
a.sub()
a.multi()
a.div()

#6. .Write a Python program to create a class that represents a shape. Include methods to
#    calculate its area and perimeter. Implement subclasses for different shapes like circle,
#    triangle, and square.

class Shape:
    
class Circle(Shape):

class Triangle(Shape):

class Square(Shape):
'''
#7.

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price
        print(f"{name} added to cart.")

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"{name} removed from cart.")
        else:
            print(f"{name} not found in cart.")

    def total_price(self):
        total = sum(self.items.values())
        return total

cart = ShoppingCart()

cart.add_item("Shirt", 2)
cart.add_item("Jeans", 3)
cart.add_item("Shoes", 4)

cart.remove_item("Jeans")

print("Total Price:", cart.total_price())
