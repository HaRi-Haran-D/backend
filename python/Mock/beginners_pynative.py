# 1. Arithmetic Product and Conditional Logic
# Write a Python function that accepts two integer numbers. If the product of the two
# numbers is less than or equal to 1000, return their product; otherwise, return their sum.
"""
def product_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        add = num1 + num2
        return add
print(product_or_sum(20,30))
print(product_or_sum(40,30))
"""

# 2. Cumulative Sum of a Range
# Iterate through the first 10 numbers (0–9). In each iteration, print the current number,
# the previous number, and their sum.
"""
prev = 0
for i in range(0,10):
    add = i + prev
    print(i, prev, add)
    prev = i
"""
i = 23
if i > 2 :
    n = int((i**0.5)+1)
    for j in range(2,n):
        if i%j == 0:
            print(False)
    print(True)

"""
    if int((i**0.5)+1)% 2==0:
        print(False)
    else:
        print(True)
    """
