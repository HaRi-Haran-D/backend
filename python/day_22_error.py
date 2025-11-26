#regex
#pattern matching process
#name: first letter should be caps, others should be small and no numbers should be entered
#name pattern: /^[A-Z][a-z]

#pattern: /d -digits
#phone



#error is recognized as a misbehaved part in the source code.
#errors can be dedected and found by the parser when it detects the incorrect statement
#interpreter inside pvm(python virtual machine)
#error is said to be an voilation statement
#when a certain statement or condition is not satisfied that time error occurs.

#exception:
#an unwanted or unexcepted event that disturbs the normal flow of program execution.
#2/0
#it shows zerodivisionerror
try:
    5/0
except:
    print('ZeroDivisionError:')
finally:
    print('Runs Successfully')
#error
#it cannot be identifed by the user.   it cannot be controlled.    it cannot be modified.
#it found by pvm.   interpreter(compilation)


#exception
#exception can be identified.   it can be controlled.   it can be modified.
#it was found object.   runtime(object: ArithmaticError, NameValue, ValueError, IndexError, ModuleNotFoundError)



#try
#we have to give a misbehaved part or found exception part
#except
#it contains the statement to perform(returns) an action against the found exception
#finally
#it does nothing whatever the code given print statement it just executes accordingly


class Base(Exception):
    pass
class Greater(Base):
    pass
class Lesser(Base):
    pass

value=200
try:
    num=int(input('Enter a Value:'))
    if num > value:
        raise Greater
    elif num < value:
        raise Lesser
    else:
        print('Both values are equal')
except Lesser as n:
    print(f'{num} is lesser than {value}')
except Greater as m:
    print(f'{num} is greater than {value}')
finally:
    print('Done')

#WORA
#Write Once Run Anywhere



