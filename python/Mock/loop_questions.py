arr = [5,3,8,1]

for i in range(len(arr)):
    for j in range(0,len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1], arr[j]
print(arr)



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
# Write a Python program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the following number
# If the number is greater than 500, then stop the loop
"""
num = [12, 75, 150, 180, 145, 525, 50]
for i in num:
    if i%5 == 0:
        if i > 150:
            if i > 500:
                break
            continue
        print(i)

#OR

for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    # check if number is divisible by 5
    elif item % 5 == 0:
        print(item)
"""

# 6. Count the total number of digits in a number using while loop
"""
num = 75869
count = 0
while num != 0:
    num = num // 10
    count = count + 1
print(count)
"""

# 7. Write a Python program to print the reverse number pattern using a for loop.
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
"""
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j, end=" ")
    print()
"""

# 8. Print list in reverse order using a loop
"""
list1 = [10, 20, 30, 40, 50]
for i in range(len(list1),0,-1):
    print(list1[i-1])
"""

# 9. Display numbers from -10 to -1 using for loop
"""
for i in range(-10,0,1):
    print(i)
"""

# 10. Display a message “Done” after the successful execution of the for loop
"""
for i in range(5):
    print(i)
else:
    print("End!")
"""

# 11. Print all prime numbers within a range
"""
def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

for i in range(25,51):
    if prime(i):
        print(i)
"""

# 12. Display Fibonacci series up to 10 terms
"""
num1=0
num2=1
for i in range(1,11):
    print(num1)
    result = num1 + num2
    num1=num2
    num2=result
"""

# 13. Find the factorial of a given number
"""
# Using Forloop
num = 5
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)

# Using Function
def fact(num):
    if num < 2:
        return 1
    else:
        return num*fact(num-1)

print(fact(6))
"""
# 14. Reverse a integer number

num = 76542
reverse_number = 0
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_number)



num = 2345
rev = 0
while num > 0:
    rem = num % 10
    rev = (rev * 10) + rem
    num = num // 10
print(rev)