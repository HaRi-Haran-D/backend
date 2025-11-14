Python 3.13.8 (tags/v3.13.8:a15ae61, Oct  7 2025, 12:34:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#DMS
user1=float(input('enter the value of user1'))
enter the value of user1
========= RESTART: C:/Python313/calculator.py ========
enter the value of user145
enter the value of user22
+,-,*,/,%+
addition value is 47.0

========= RESTART: C:/Python313/calculator.py ========
enter the value of user1:>
Traceback (most recent call last):
  File "C:/Python313/calculator.py", line 1, in <module>
    user1=float(input('enter the value of user1:'))
ValueError: could not convert string to float: '>'

========= RESTART: C:/Python313/calculator.py ========
enter the value of user1:1
enter the value of user2:2
+,-,*,/,% :=
invalid operator

========= RESTART: C:/Python313/calculator.py ========
['python', 45, 2.3, 18.2, 2.3, 45, 115, 'array', 'stack', 'queue', 'boolean', 6.3, 66]
lista=['python',45,2.3,18.2,2.3,45,115,'array','stack','queue', 'boolean', 6.3, 66]


print(lista)
['python', 45, 2.3, 18.2, 2.3, 45, 115, 'array', 'stack', 'queue', 'boolean', 6.3, 66]
#index
lista[0]
'python'
lista[5]
45
lista[10]
'boolean'
#list:inbuild methods
lista.append('mouse')
print(lista)
['python', 45, 2.3, 18.2, 2.3, 45, 115, 'array', 'stack', 'queue', 'boolean', 6.3, 66, 'mouse']
#one value will be added at the end of the list[]


lista.copy()
['python', 45, 2.3, 18.2, 2.3, 45, 115, 'array', 'stack', 'queue', 'boolean', 6.3, 66, 'mouse']
lista.count(45)
2
lista.count('mouse')
1
lista.count(6.3)
1
#duplicates count
lista.extend([881,92,6,6.3,45,'square'])
lista
['python', 45, 2.3, 18.2, 2.3, 45, 115, 'array', 'stack', 'queue', 'boolean', 6.3, 66, 'mouse', 881, 92, 6, 6.3, 45, 'square']
lista.index('boolean')
10
lista.index(45)
1
lista.insert(10,True)
print(lista)
['python', 45, 2.3, 18.2, 2.3, 45, 115, 'array', 'stack', 'queue', True, 'boolean', 6.3, 66, 'mouse', 881, 92, 6, 6.3, 45, 'square']
lista.pop()
'square'
lista.pop()
45
lista.pop()
6.3
lista.remove(2.3)
print(lista)
['python', 45, 18.2, 2.3, 45, 115, 'array', 'stack', 'queue', True, 'boolean', 6.3, 66, 'mouse', 881, 92, 6]
lista.remove(2.3)
print(lista)
['python', 45, 18.2, 45, 115, 'array', 'stack', 'queue', True, 'boolean', 6.3, 66, 'mouse', 881, 92, 6]
lista.reverse()
print(lista)
[6, 92, 881, 'mouse', 66, 6.3, 'boolean', True, 'queue', 'stack', 'array', 115, 45, 18.2, 45, 'python']
lista.sort()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    lista.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
#sort(reverse=True)
val=['ab','ju','ty','cd','rr','bb']
val.sort()
print(val)
['ab', 'bb', 'cd', 'ju', 'rr', 'ty']
val.sort(reverse=True)
print(val)
['ty', 'rr', 'ju', 'cd', 'bb', 'ab']
val.clear()
print(val)
[]

========= RESTART: C:/Python313/calculator.py ========
number present

========= RESTART: C:/Python313/calculator.py ========
number present
11
45
12
18
20
24

========= RESTART: C:/Python313/calculator.py ========
no is not present

========= RESTART: C:/Python313/calculator.py ========
l
i
s
t
n
o
s
t1=(1,'hetro',12,2.5,12,'animal',2.5,155,1)
print(t1)
(1, 'hetro', 12, 2.5, 12, 'animal', 2.5, 155, 1)
t1.index(12)
2
t1.index(1)
0
t1.index('animal')
5
t2=('concat','list',45,2.5,97,154)
t3=t1+t2
print(t3)
(1, 'hetro', 12, 2.5, 12, 'animal', 2.5, 155, 1, 'concat', 'list', 45, 2.5, 97, 154)
print(t1*2)
(1, 'hetro', 12, 2.5, 12, 'animal', 2.5, 155, 1, 1, 'hetro', 12, 2.5, 12, 'animal', 2.5, 155, 1)
print(t3*2)
(1, 'hetro', 12, 2.5, 12, 'animal', 2.5, 155, 1, 'concat', 'list', 45, 2.5, 97, 154, 1, 'hetro', 12, 2.5, 12, 'animal', 2.5, 155, 1, 'concat', 'list', 45, 2.5, 97, 154)
t3.count(2.5)
3
a={1,5,8,9,10,12,2,3,4,5}
print(a)
{1, 2, 3, 4, 5, 8, 9, 10, 12}
a
{1, 2, 3, 4, 5, 8, 9, 10, 12}
b={1,2,3,4,5,6,7,8,9,10}
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b={1,2,3,7,8,9,10,4,5,6}
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a
{1, 2, 3, 4, 5, 8, 9, 10, 12}
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a.add(11)
a.difference(b)
{11, 12}
a.difference_update(b)

a
{11, 12}
a.add(5)
a.add(7)
a.add(8)
a.intersection(b)
{8, 5, 7}
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a
{5, 7, 8, 11, 12}
>>> a.intersection_update(b)
>>> a
{8, 5, 7}
>>> b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> a.add(9)
>>> a.add(1)
>>> print(a)
{1, 5, 7, 8, 9}
>>> b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> a.symmetric_difference(b)
{2, 3, 4, 6, 10}
>>> #symmetric means uncommon values in both the set a and v
#symmetric means uncommon values in both the set a and b

a.symmetric_difference_update(b)
a
{2, 3, 4, 6, 10}
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#union combines both the set a and b

a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
