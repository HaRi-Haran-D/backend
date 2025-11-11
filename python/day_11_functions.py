#Functions
#a block of code which is going to perform some specific task when a function is called it returns the
#processed output values

#function declaration is with the help of  def keyword.

#syntax
#function functionname(parameters(it can contain n nos of parameters)):
#   print()
#function call(arguments)

#parameters - dataholders or properties
#arguments - actual values
#for a function n no. of call can be given
#and also n no. of arguments
#arguments can be dynamic during the function call

def greet():
    print('Hello this is Python Code')

greet()

#Accepts function with parameter
#also accepts function with no parameter
#for a function 

def biodata(name,age,city,gender):
    print(f'Name : {name}')
    print(f'Age : {age}')
    print(f'City : {city}')
    print(f'Gender : {gender}')
biodata('Hari',25,'chennai','Male')
biodata('JK',26,'chennai','Male')

#Advantages
#memory optimization
#processed output value it returns
#reduces complexity

def add(a,b):
    c=a+b #expression operator
    return c
    
print(add(9,1))
print(add(10,23))


#function with return Keyword
#return memory value[terminate]
#in function we can pass dynamic arguments


#types of functions
#with parameter
#without parameter
#call by value
#call by reference










