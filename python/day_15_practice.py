#1. define an outer function that accepts 2 parameter with the help of inner function calculate the product of x and y
'''
def product(x,y):
    def inner(a,b):
        return a*b
    c=inner(x,y)
    return c
print(product(9,4))
'''

#2. generate a python list all the even numbers btwn 4 - 30 using function
'''
def even(a,b):
    for i in range(a,b+1):
        if i%2==0:
            print(i)
even(4,30)
'''
#3. create a function using keyword argument
'''
def greet(name,location,age):
    print(f'Iam {name} from {location} and Iam {age} old')

greet(age= 25, name = 'HaRi', location = 'Ambattur')
'''
#4. define a global variable and modify the value
'''
num = 5
def change():
    global num
    num +=10
change()

print(num)
'''
#5. create a lambda function that square the value
'''
value = [12,32,4,34,14,23,10,3]
m = list(map(lambda n:n*n,value))
print(m)
'''
#6. use a lambda function with a map function to double each element in a list
'''
value = [12,32,4,34,14,23,10,3]
m = list(map(lambda n:n*2,value))
print(m)
'''
#7. generate an unpacked argument value using function

def func(*name):
    for i in name:
        print('Hello',i)

func('Hari','JK','Yuvi')

#8. call a function using positional and keyword arguments







