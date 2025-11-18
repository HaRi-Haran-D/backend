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
