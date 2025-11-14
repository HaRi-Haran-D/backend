#Function - A block of reusable code it is executed only when it is called.
#           place () after the function name to invoke it.

def hello(name):
    print("Hello",name)
    print("Hello World")
hello("Hari")

def greet(first_name,last_name,age):
    print('hello',first_name,last_name)
    print('your age is',age)
    print('have a nice day')
greet('hari','haran',25)




#using return statement - is used within functions to send python values/objects back to the caller.
        #these values/object are known as the functions return value.
        #is used to end a function
        #and send a result back to the caller
def add(a,b):
    return a+b

print(add(4,5))

def name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first +" "+last
print(name('hari','haran'))




#default arguments - a default value for certain parameters
            #default is used when that argument is omitted
            #make your functions more flexible, reduces no. of arguments
def total(price,discount=0,tax=0.05):
    return price*(1-discount)*(1+tax)
print(total(500))
print(total(500,0.2))

import time
def count(end,start=0):
    for i in range(start,end+1):
        print(i)
        time.sleep(1)
    print("Hello !")
count(10)




#keyword arguments - arguments preceded by an identifier when we pass them to a function
#           helps with readibility
#           the order of the arguments doesn't matter, unlike positional arguments
#           python knows the names of the arguments that our function recieves


def hello(first,middle,last):
    print("Hello",first,middle,last)

hello(last='bro',middle='hari',first='Mr.')




#arbitrary arguments - allows you to pass multiple non-key arguments
            #for one parameter we can pass multiple arguments
            # * unpacking operator
def 




#nested function calls - function calls inside other functions cells
#           innermost function cells are resolved first
#           returned value is used as arguments for the next outer function

num = input('Enter a number: ')
num=float(num)
num=abs(num)
num=round(num)
print(num)

#or
print(round(abs(float(input('Enter a number: ')))))




#scope - the region that a variable is recognized
#       a variable is only available from inside the region it is created
#       a global and locally scoped versions of a variable can be created

def name():
    name ='Hari'#this variable only available inside the function
    print(name)
name()




#args - parameter that will pack all arguments into a tuple
#       useful so that a function can accept a varying amount of arguments

def add(a,b,c):
    return a+b+c
print(add(1,2,3))











