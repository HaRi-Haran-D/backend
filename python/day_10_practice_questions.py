#1. break a for loop in python with a list values[52,100] give the condition when the value is above 90
#terminate the condition
'''
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

#3. multiplication table any number using for loop
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
name = 'Si v a  C h a n d  r  u'
for i in name:
    if ' ' in i:
        print(end='true')
        continue
    print(i,end='')

#6.
for i in d:
    if i%2 == 0:
        continue
    print(i)
'''

#scenerio 1: What was the price on day3

stock_price = [290,305,320,301,292]

print(stock_price[2])#--> 320

print(stock_price[-3])#--> 320

print(stock_price[2:3])#--> 320


#2. on what day the price was 301

for i in range(len(stock_price)):
    if stock_price[i] == 301:
        print(f'On day {i} the price would be 301')
        break

#3. print all prices

for i in stock_price:
    print(i)

#4 insert new price 284 at index 1

stock_price.insert(1,284)
print(stock_price)

#5 delete element at index 1
stock_price.remove(305)
print(stock_price)


#lets say your expenses for every month are listed
jan = 2200
feb = 2350
mar = 2600
april = 2130
may = 2190
#in feb how many dollars you spent extra compare to jan
