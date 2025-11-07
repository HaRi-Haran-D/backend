#Logical operators - evaluate multiple conditions(or,and,not)
#       or - at least one condition must be True
#       and - both condition must be True
#       not - inverts the condition(not false, not true)

#OR Operator
temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is still cancelled")
else:
    print("The outdoor event is still scheduled")
    
#AND Operator
temp = 25
is_sunny = True
if temp >= 25 and is_sunny:
    print("Its hot outside")
else:
    print("Its cold outside")

#NOT Operator
temp = 25
is_sunny = True
if temp >= 25 and not is_sunny:
    print("Its hot outside")
else:
    print("Its cold outside")
