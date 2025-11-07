#list comprehension print only start letter j
'''
names=['jammy','king','qujeen','john','academy','joseph']
j_names=[]
for i in names:
    if 'j' in i:
        j_names.append(i)

print(j_names)

#J_names[]

#in,not in =membership
#is,is not=identity 

#remove list values using del

a=['jammy','king','queen','john','joseph']
del a
print(a)

#remove item using del keyword

car={'name':'corolla','brand':'toyoto'}
del car['name']
del car['brand']
print(car)

#iterating a dict

person={'name':'anbu','country':'dfg','course':'python'}
print('key',':','value')
for key in person:
    print(key,':',person[key])

#find the length of dict:
print(len(person))


#Adding items to the dict:
employ={'id':105,'name':'sundar','tel':748596}
employ['weight']=45
employ.update({'height':5,'exp':8})
print(employ)


#default value in dict:
employ={'id':105,'name':'sundar','tel':748596}
employ.setdefault('age',25)
print(employ)

merging two dict using kwargs ()
a={'a':4,'b':44,'c':444}
b={'x':5,'y':55,'z':555}
c={*a,*b}
print(c)

i=1,7
j= 0,i

for i in range(1,6):
    for j in range(5,i,-1): #5-1,4-1
        print('*',end='')
    print()


#len()iteration 
name='alvina'
for i in range(len(name)):
    for j in range(i):
        print(name[j],end='')
    print()

print(len(name))


name='alvina'
for i in range(len(name)+1):
    for j in range(i):
        print(name[j],end='')
    print()

for i in range(0, 6 + 1):
    print(i)


for i in range(1,11):
    for j in range(10,i,-1):
        print('*',end=' ')
    print()




#count how many odd and even nos
for i in range(0,20,2):
    print(i)
'''
'''
#with condition
even=0
odd=0
for i in range(1,8+1):
    if (i%2==0):
        even +=1
    else:
        odd +=1
print('even count-',even)
print('odd count-',odd)

#positive and negative value
nums = [10, -4, 8, -2, 0, 5]
for n in nums:
    if n > 0:
        print(n, "is positive")
    elif n < 0:
        print(n, "is negative")
    else:
        print(n, "is zero")


#Find numbers greater than 50
numbers = [10, 55, 23, 75, 90, 45]
for n in numbers:
    if n > 50:
        print(n)
'''
#count how many students passed in a list:
marks = [90, 45, 67, 32, 80]
student_fail=[]

for i in marks:
    if marks.index(i)<50:
        student_fail.append(i)
print(student_fail)
'''
#Find vowels in a word='python'
give only vowels count
vowels='a','e','i','o','u'
#count vowels and consonants in a given string:'''
vowels=0
const=0
str='validations'
vowels=vowels+1
const=const+1

