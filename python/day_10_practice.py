'''
for i in range(10,1,-1):
    for j in range(0,i):
        print(i,end='*')
    print()
'''

'''
height = 5  # Number of rows

for i in range(height):
    spaces = ' ' * (height - i - 1)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)

space = " "
for i in range(6,1,-1):
    print(space*i,'*')
'''

'''
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end='')
    for j in range(0,i):
        print('*',end=' ')
    print()
'''

for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(' ',end='')
    for j in range(0,i):
        print('*',end=' ')
    print()


for i in range(1,6,2):
    for j in range(5,i,-1):
        print(' ',end='')
    for j in range(0,i):
        print('*',end=' ')
    print()
for i in range(5,0,-2):
    for j in range(5,i,-1):
        print(' ',end='')
    for j in range(0,i):
        print('*',end=' ')
    print()


