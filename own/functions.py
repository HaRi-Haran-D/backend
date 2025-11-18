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











