# 1. Given two integer numbers, write a Python program to return their product only if the product is
# equal to or lower than 1000. Otherwise, return their sum.
'''
def number(num1, num2):
    if num1 * num2 > 1000:
        print("The result is ", num1 + num2)
    else:
        print("The result is ", num1 * num2)
number(20,30)
number(30,40)
'''

# 2.Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum
# of the current and previous number.
'''
prev = 0
for curr in range(0,10):
    sum = curr + prev
    print(f'Current Number {curr} Previous Number {prev} Sum: {sum}' )
    prev = curr
'''

# 3. Write a Python code to accept a string from the user and display characters present at an even
# index number.
'''
def even(stri):
    for i in range(len(stri)):
        if i%2==0:
            print(stri[i])
even("PYnative")
'''

# 4. Write a Python code to remove characters from a string from 0 to n and return a new string.
'''
def remove(word,num):
    if len(word) > num:
        n = word[num:]
        return n

print(remove("pynative", 4))
print(remove("pynative", 2))
'''

# 5. Write a code to return True if the list’s first and last numbers are the same. If the numbers
# are different, return False.
'''
#mine
def list(lst):
    # for i in range(len(lst)):
    if lst[0] == lst[-1]:
        print(True)
    else:
        print(False)

list([10, 20, 30, 40, 10])
list([75, 65, 35, 75, 30])
'''

# 6. Write a Python code to display numbers from a list divisible by 5
'''
list = [10, 20, 33, 46, 55]
for i in list:
    if i%5 == 0:
        print(i)
'''

# 7. Write a Python code to find how often the substring “Emma” appears in the given string.
'''
str = "Emma is good developer. Emma is a writer"
count = str.count("Emma")

print(count)
'''
'''
def count_emma(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + 4] == 'Emma'
    return count

count = count_emma("Emma is good developer. Emma is a writer")
print("Emma appeared ", count, "times")
'''

# 8. Print the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
'''
for i in range(1,6):
    print(i*str(i))
'''
'''
for num in range(6):
    for i in range(num):
        print (num, end=" ")
    print("\n")
'''
# 9. Write a Python code to check if the given number is a palindrome. A palindrome number
# reads the same forwards and backward. For example, 545 is a palindrome number.
str='545'
print(str[::-1])