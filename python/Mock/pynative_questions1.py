# Given two integer numbers, write a Python program to return their product only if the product is
# equal to or lower than 1000. Otherwise, return their sum.
def number(num1, num2):
    if num1 * num2 > 1000:
        print("The result is ", num1 + num2)
    else:
        print("The result is ", num1 * num2)
number(20,30)
number(30,40)