#arbitrary arguments - allows you to pass multiple non-key arguments
        
#arbitrary positional argument
            #for one parameter we can pass multiple arguments
            # * unpacking operator

'''
def name(*names):
    for i in names:
        print("Hi",names)

name('hari','jk','yuvi')
'''
#arbitrary keyword argument
#**kwargs - allows you to pass multiple keyword arguments
def address(**route):
    for key,value in route.items():
        print(f'{key}: {value}')

address(street='6th Cross Street',city='Chennai',state='TN',pincode='53')

#Both arbitrary positional argument and arbitrary keyword argument
def label(*args,**kwargs):
    for i in args:
        print(i,end=' ')
    print()
    for j in kwargs.values():
        print(j, end=' ')

label('Hari','Jk','Yuvi',street='6th Cross Street',city='Chennai',state='TN',pincode='53')



#nested function calls - function calls inside other functions cells
#           innermost function cells are resolved first
#           returned value is used as arguments for the next outer function
'''
num = input('Enter a number: ')
num=float(num)
num=abs(num)
num=round(num)
print(num)

#or
print(round(abs(float(input('Enter a number: ')))))
'''
