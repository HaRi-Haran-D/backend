# 1. How do you append an element to an array?

"""
list = [1,2,3,5,6]

list+= [45]
print(list)
"""

# 2. How do you insert an element at a specific position?
"""
list = [5,23,7,2,9]
n=[]
for i in list:
    if list.index(i) == 2:
        n+=[10]
    else:
        n+=[i]
print(n)
"""

# 3. How do you remove an element from an array?
"""
list = [5,23,7,2,9]
n=[]
for i in list:
    if list.index(i) == 2:
        continue
    else:
        n+=[i]
print(n)
"""

# 4. How do you find the sum of all elements in an array?
"""
list = [10,34,56,23,78]
sum=0
for i in list:
    sum+=i
print(sum)
"""

# 5. How do you find the maximum and minimum elements in an array?
"""
#Maximum
list = [10,34,56,101,23,78,100]
large = list[0]
for i in list:
    if i > large:
        large = i
print(large)

#Minimum
mini = list[0]
for i in list:
    if i < mini:
        mini = i
print(mini)
"""

# 6. How do you reverse an array?
"""
list = [10,34,56,101,23,78,100]
n=[]
for i in range(len(list)-1,-1,-1):
   n+=[list[i]]
print(n)

#or

print(list[::-1])
"""
"""
user1 = [101, 102, 103, 104]
user2 = [103, 104, 105, 106]

both = list(set(user1) & set(user2))
print(both)
"""
n=[1,2,4,5,6,8,9,12]
nn=[]
for i in n:
    if i == :
        nn+=[i]
    else:
        nn+=[i+1]
print(nn)

