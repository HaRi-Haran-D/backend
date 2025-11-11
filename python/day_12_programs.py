'''
#1. Print even numbers between 1 and 20.
even=[]
for i in range(1,21):
    if i % 2 == 0:
        even.append(i)
print(even)

#2. Print the multiplication table of a given number

n = int(input("Enter a Number: "))

for i in range(1,11):
    print(f'{n}*{i}={i*n}')

#3. Print the square of numbers from 1 to 10.

for i in range(1,11):
    print(i*i)

#4. Count how many even numbers are in a given list.

list1 = [1,2,3,4,5,6,7,8,9,10,12,24]
count=0
for i in list1:
    if i %2 == 0:
        count+=1
print(count)

#5. Print each character in a string (Python fullstack)

course = "Python fullstack"

for i in course:
    print(i)


#6.

for i in range(0,6):
    for j in range(1,i):
        print(j,end='')
    print()


#7. Print numbers in reverse, from 10 to 1.

for i in range(10,0,-1):
    print(i)
'''

#8. print pyramid

for i in range(6,0,-1):
    for j in range(1,i):
        print(' ',end='')
    print('*'*(13-2*i))






