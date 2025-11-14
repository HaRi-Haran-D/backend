#a recursion means nested function a function that calls itself
#recursion works like a code that breaks into smaller piece of code during execution
#syntax:
'''
function functionname(parameter):
if (base condition):
return n #stop calling itself
else:
return(modified arguments)
function call
'''

#lambda function
    #lambda means nameless function
    #we will not use def keyword for lambda
    #inline function
    #lambda means anonynmous/ unknown function
    #in build function map(), filter(), reduce(): module(itertools)
    #we will not use return keyword here
    #in one word we can say lambda as a quick, one-line code

#syntax
#lambda arguments : expression

s = 'python'

s1=lambda x:x.upper()
print(s1(s))#here we are passing s as an args for lambda function

s1=lambda r:r.capitalize()
print(s1(s))

got =lambda a,b,c : a if a>b and c>b else b if b>c else c
print(got(10,20,30))


#map()
n=[11,12,13,14,15,16,17,18,19,20]

m=list(map(lambda a:a*5,n))
print(m)


#filter()
n = [23,35,65,12,34,67,89,123]
m=list(filter(lambda a:a%2!=0,n))
print(m)


#reduce()
from functools import reduce
n = [23,35,65,12,34,67,89,123,234,12,45]
m = reduce(lambda a,b:a+b,n)
print(m)

#oops
#principles
#class and object
#self, init constructor
#encapsulation
#public, private, protected
#abstraction
#single, multiple, multilevel, heirarchical
#polymorphism
#operator, overloading, overriding
#method overriding, method overloading is not supported in python








#sum of n natural numbers
#call by value
#call by reference

    




