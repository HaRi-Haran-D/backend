#1. break a for loop in python with a list values[52,100] give the condition when the value is above 90
#terminate the condition

value = [52,23,34,87,91,100,23,1001,342]
for i in value:
    if i >=90:
        break
    print(i)

#2. declare a name as jessica123 python

name = 'jessica123   python'
for i in name:
    if ' ' in i:
        continue
    print(i,end='')

#3. multiplication any number using for loop
n = 5
d=[]
for i in range(0,11):
    d.append(i*n)
    print(f'{n}*{i}={i*n}')
#4. square some list values

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = []
for i in list1:
    list2.append(i**2)
print(list2)

#5. if values has space in between the variable it should print true for space
name = 'Si v a  C h    a n    d  r  u'
for i in name:
    if ' ' in i:
        print(end='true')
        continue
    print(i,end='')

#6.
for i in d:
    if i%2==0:
        continue
    print(i)

