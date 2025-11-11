#functions in python
#python: functional + object oriented programming language
#structure of code which returns some processed output values

#types of functions
#recursive function
#userdefined function (explicit function)
#built-in function (implicit function)
#math function
#arbitary function
#default function
#keyword function


#syntax
#def keyword following functionname
    #body print
#outside the function (function call)

def greet():
    print("Hello World")
    print("Hello Hari")
greet()
greet()

#
def employ(empname,empid,empdesg):
    print("Emp Name: ",empname)
    print("Emp ID: ",empid)
    print("Emp Designation: ",empdesg)
    
employ("HaRi",1089,"Manager")

employ("Jk",124,"Devops")

#user defined arguments
    #arguments used in user defined functions:
    #positional arguments
    #userdefined function predefined function
def product():
    product_name = "Jaggery"
    quantity = 5
    price = 230
    quality = 100
    print("My product is ",product_name)
    print("No of pieces ",quantity)
    print("price is ",price)
    print("it is ",quality, "pure")

product()

#keyword arguments
    #parameter(are considered as keys)
    #syntax:(parameter:value)
def profile(name='Hari',degree='BCA',project='GreenCare',age=25):
    print('student name :',name)
    print('his degree is ',degree)
    print('project name is ',project)
    print('his age is ',age)

profile()
#output
''' student name : Hari
    his degree is  BCA
    project name is  GreenCare
    his age is  25 '''

profile(age=15,name='vk')
#we change the position of the arguments
#output
''' student name : vk
    his degree is  BCA
    project name is  GreenCare
    his age is  15 '''

#positional arguments
    #we cannot change the position of the arguments
def car(car_name='Benz',car_type='ev',car_model='a-series'):
    print('the name of the car is',car_name)
    print('the car type is ',car_type)
    print('car model is ',car_model)
car()
#output
''' the name of the car is Benz
    the car type is  ev
    car model is  a-series '''
    
car('BMW','petrol','f-series')
#output
''' the name of the car is BMW
    the car type is  petrol
    car model is  f-series '''


#arbitary arguments:/variable length arguments
#for one parameter we can pass multiple arguments
def blessings(*persons):
    for i in persons:
        print('stay blessed',i)

        
blessings('a','b','c','r','y','j','m','r','p','o','u')















