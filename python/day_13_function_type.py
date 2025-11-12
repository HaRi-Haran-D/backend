#global Variable
#global variable means that can be declare outside the function or the   throughout the entire program.
'''
a=50

def var1():
    a=20
    print(a)
var1()

def var2():
    print(a)
var2()


gst = 0.18
def shop(amount):
    gst = 0.12
    print(f'Total amount with {gst}% is {amount+(amount*gst)}')
shop(79)


score=0
def foot(points):
    global score
    score+=points
    print(score)
foot(45)
foot(70)
foot(10)
'''


'''
def deposit(balance,amount):
    amount += balance
    print(f'Your account has been credited with {balance} and the balance {amount}')
    
    def withdraw(amount):
        if balance < amount:
            print('Insufficiant Balance')
        else:
            balance -= amount
            print(f'Your account has been debited with {amount} and the available balance {balance}')
    def checkbalance():
        print(amount)
deposit(100,23)
'''

#print statement display the value(result) to user. does nothing. it cant be stored. it does not do
#return it does not show result to the user. passes value to the another function. return keyword can be stored in variable. it stops the function when executed
'''
def add(a,b):
    c=a+b
    return c
p=add(3,5)
print(p)

def std():
    name = 'HaRi'
    city = 'Chennai'
    return (name,city)
name,city = std()
print(name)
print(city)

print(std())
'''
'''
# 1.
arry=[[1,2,3],[4,5,6],[7,8,9]]
arr = []

for i in arry:
    arry.index(i)
    arr.append(arry)
    for j in arr:
        arr.index(j)
        arry.append(arr)
print(arry)

#2. check the third highest value in a list
value = [45,18,84,47,91,218]

#3. calculator progran using return keyword
#a,b(input)(choices(+,-,*,/,%)
'''
def factorial(n):
    if n < 0:
        return 'negative value'
    else:
        return n*factorial(n-1)

num=5
result=factorial(num)
print(result)
