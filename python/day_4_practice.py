#1. Traffic Light Simulator
value = str(input("Enter a color - Red/Yellow/Green")).lower()
if(value == 'red'):
    print("Stop")
elif(value == 'yellow'):
    print("Get Ready")
elif(value == 'green'):
    print("Go")
else:
    print("Invalid Color")

#2. Login System
username = 'admin'
password = 12345

if(username == 'admin' and password == 12345):
    print("Welcome Admin")
else:
    print("Invalid Password")

#3. FizzBuzz

integer = int(input('Enter a number: '))

if(integer % 3 == 0 and integer % 5 == 0):
    print('FizzBuzz')
elif(integer % 3 == 0):
    print('Fizz')
elif(integer % 5 == 0):
    print('Buzz')
else:
    print(integer)

#4. Display grade based on marks.(based on 90,80,70,60,others fail)

mark=int(input("Enter your mark: "))

if(mark<40):
    print('Fail')
elif(mark<=50):
    print('Below Average')
elif(mark<=60):
    print('Average')
elif(mark<=70):
    print('Good')
elif(mark<=80):
    print('Very Good')
elif(mark<=90):
    print('Excellent')
else:
    print('Invalid')
