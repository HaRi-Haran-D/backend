user1 = float(input('Enter a Value'))
user2 = float(input('Enter a Value'))
operator = input('Enter any operator +, -, *, /, %')

if(operator == '+'):
    print(user1 + user2)
elif(operator == '-'):
    print(user1 - user2)
elif(operator == '*'):
    print(user1 * user2)
elif(operator == '/'):
    print(user1 / user2)
elif(operator == '%'):
    print(user1 % user2)
else:
    print('invalid operator')
