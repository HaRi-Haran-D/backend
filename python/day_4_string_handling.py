#String handling


#indexing

#acessing the individual memory values of a given string
#indexing means the memory value always start from 0
#while accessing [](square bracket) is used
#even the empty spaces will also considered as an account
str1='machine learning'
print(str1[0])
#'m' is printed
print(str1[7])
#' ' is printed

#travesing means the values starts from left to right
#backtraversing means values starts from right to left
print(str1[-1])
#'g' is printed

#slicing
#means it will return the value from start to end
#partition/dividing/spiltting
#slicing 1 value must added at the end-rule
course = 'artificial inteligence'
print(course[0:6])
#'artifi' is printed

print(course[11:16])
#'intel' is printed

#backteraversing
print(course[-8:-12])
#' ' is printed

print(course[-11:16])
#'intel' is printed

#ranging - will give us either the start value or end value
app_name = 'whatsapp'
print(app_name[2:])
#'atsapp' is printed

print(app_name[:2])
#'wh' is printed


#decision making statement: DMS
#types: if statement, if-else statement, if elif else

#if statement

employee = 'admin'
if(employee == 'admin' or employee == 'hr'):
    print('welcome')

if(employee == 'hr'):
    print('Hello HR')
elif(employee == 'admin'):
    print('Hello Admin')

#if-else statement

num = 18
if(num%2 == 0):
    print(num, ' is even no')
else:
    print(num, 'is odd no')

#if-elif else
temp = 32
if(temp>30):
    print('temp is too hot')
elif(temp<22):
    print('moderate temp')
elif(temp<12):
    print('cold climate')
elif(temp>=0):
    print('freeze')


a = int(input('enter a number for A'))
b = int(input('enter a number for B'))
c = int(input('enter a number for C'))
if(a>b) and (a>c):
    print('A =',a, 'is greater')
elif(b>a) and (b>c):
    print('B =',b,'is greater')
elif(c>a) and (c>b):
    print('C =',c,'is greater')
else:
    print('all equal')
    


