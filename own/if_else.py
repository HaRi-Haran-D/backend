age = int(input("Enter your age: "))

if age>=18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote.")


response = str(input("Would you like food? (Y/N):")).upper()

if response == 'Y':
    print('Have some food!')
elif response == 'N':
    print('No food for you')
else:
    print('Invalid')
