#Write a Python program to get the sum of a non-negative integer using recursion


#Display numbers from -10 to -1 using for loop
for i in range(-10,0,1 ):
    print(i)

#Print all prime numbers within a range
n=[]
'''
for i in range(10,50):
    if i%2==0 or i%3==0 or i%5==0:
        continue
    else:
        n.append(i)
print(n)
'''

for i in range(1,50):
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            n.append(i)
print(n)


#print pyramind program
for i in range(1,6):
    for j in range(1,i):
