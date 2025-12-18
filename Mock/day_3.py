#1.
'''
intput = [1,0,5,6,0,3,0,0]
#intput.sort()
#print(intput)
n=[]
for i in range(0,len(intput)):
    if i < 3:
        n.append(intput[i])
print(n)
'''

#3.

for i in range(1,6):
    for j in range(i-1):
        print(" ",end='')
    for n in range(i,6):
        print(n,end=" ")
    print()

#2.
a=[1,2,3,4]
b=[3,4,5,6]
c=[]
for i in a:
    for j in b:
        if i == j:
            c.append(i)
print(c)
