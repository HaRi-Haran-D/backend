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
'''
# 1.
def Palindrome(str):
    if str == str[::-1]:
        print(True)
    else:
        print(False)
 
 # 2.       
def Palindrome(number):
    if number < 0:
        print(False)
    
    original_string = str(number)

    reversed_string = original_string[::-1]

    if original_string == reversed_string:
        print(True)
    else:
        print(False)

# 3.
def palindrome(number):
    print("original number", number)
    original_num = number
    
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")

Palindrome(str='545')
Palindrome(str='121')
Palindrome(str='125')
'''
# 10. Given two lists of numbers, write Python code to create a new list containing odd numbers
# from the first list and even numbers from the second list.
'''
def list(list1, list2):
    new_list = []
    for i in list1:
        if i%2 != 0:
            new_list += [i]
    for j in list2:
        if j % 2 == 0:
            new_list += [j]
    print(new_list)

list(list1 = [10, 20, 25, 30, 35],list2 = [40, 45, 60, 75, 90])
'''
# 11. For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a
# space separating the digits.
'''
# 1.
def string(stri):
    for i in range(len(stri),0,-1):
        print(stri[i-1], end=" ")
    print()
string(stri = '7536')

# 2.
number = 7536
print("Given number", number)
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end=" ")
'''
# 12. Calculate income tax for the given income by adhering to the rules below
'''
def tax(amt):
    tax_amt = 0
    if amt <= 0:
        print('Invalid amount')
    elif amt <= 10000:
        print(tax_amt)
    elif amt <= 20000:
        tax_amt += (amt-10000)*0.1
        print(tax_amt)
    elif amt > 20000:
        tax_amt +=  (10000*0.1) + ((amt-20000)*0.2)
        print(tax_amt)
    else:
        print('Invalid input')

tax(amt=10000)
tax(amt=20000)
tax(amt=45000)
'''
# 13. The multiplication table from 1 to 10 is a table that shows the products of numbers from 1 to 10.
'''
def table(num):
    for i in range(1,num+1):
        print(' ')
        for j in range(1,11):
            print(i * j, end= ' ')
table(10)
'''
# 14. Print a downward half-pyramid pattern of stars
'''
for i in range(5,0,-1):
    print('* '*i)
    print('',end='')

for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")
'''
# 15. Write a function called exponent(base, exp) that returns an int value of base raises to
# the power of exp.
def exponent(base, exp):
    for i in base:
        for j in exp:





