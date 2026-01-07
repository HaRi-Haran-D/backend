# 1. Print first 10 natural numbers using while loop
"""
num=1
while num <= 10:
    print(num)
    num+=1
"""

# 2. Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
'''

# 3. Calculate sum of all numbers from 1 to a given number
'''
def add(num):
    sum=0
    for i in range(1, num+1):
        sum+=i
    print(sum)
add(10)
'''

# 4. Print multiplication table of a given number
'''
def multi_table(num):
    for i in range(1,11):
        print(f'{num} * {i} = {num * i}')
multi_table(11)
'''

# 5. Display numbers from a list using a loop









