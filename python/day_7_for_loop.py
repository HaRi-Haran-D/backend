#For Loop
#loop - iteration
#repeated
#start value and end value

#for syntax
#for(initialization,condition,increment/decrement)

#range numerical values
#test conditin(>,<,<=,>=)
#increment/decrement
#++ adds 1 value,-- removes 1 value

name = "Python"
for j in name:
    print(j)
    
for i in range(2,20,2):
    print(i)

sum = 0
for i in range(0,10):
    sum = sum + i
    print(sum)

#nested for loop
for i in range(1,6):
    for j in range(0,i):
        print(' * ')
    print()

#row printing is i
#column printing is j
#
for i in range(1,6):
    for j in range(0,i):
        print('*')
    print()


