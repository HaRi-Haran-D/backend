# 1. Find the largest element in a list
'''
n=[1,4,2,5,1]
largest=n[0]
for i in n:
    if i > largest:
        largest = i
print(largest)
'''

# 2. Find the smallest element in a list
'''
n=[1,4,2,5]
smallest=n[0]
for i in n:
    if i < smallest:
        smallest = i
print(smallest)
'''

# 3. Reverse a list
'''
n=[1,4,2,5,1]
rev=[]
for i in range(len(n),0,-1):
    rev+=[n[i-1]]
print(rev)
'''

# 4. Check if a list is sorted
'''
numbers = [1, 2, 3, 4, 5]
if numbers == sorted(numbers):
    print("List is sorted")
else:
    print("List is not sorted")
'''

# 5. Find the sum of elements in a list
'''
n = [1, 2, 3, 4, 5]
sum = 0
for i in n:
    sum += i
print(sum)
'''

# 6. Count even and odd numbers in a list
'''
n = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

def odd_or_even(n):
    odd = 0
    even = 0
    for i in n:
        if i % 2 == 0:
            even += 1
        elif i % 2 != 0:
            odd += 1
        else:
            pass
    return f'Odd: {odd}nos Even: {even}nos'
print(odd_or_even(n))
'''

# 7. Remove duplicate elements from a list
'''
n=[1,4,2,5,4,5,2,1]
f = set(n)
print(list(f))
'''

# 8. Rotate a list left by one position
'''
numbers = [1, 2, 3, 4, 5]
rotated = numbers[1:] + numbers[:1]
print(rotated)
'''

# 9. 


