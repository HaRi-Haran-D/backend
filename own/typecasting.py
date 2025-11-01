#Typecasting - the process of converting a variable from one datatype to another
#               str(), int(), float(), bool()


name="Hari Haran"
age = 25
gpa = 3.2
isStudent= True

#String to Boolean
name = bool(name)
print(name)
    #True
#returns True because it has value in the variable
#if the variable doesn't have any value it returns false
#this is how it works for boolean

#Int to String
age=str(age)
print(age)
    #"25"

#Int to Float
age = float(age)
print(age)
    #25.0

#Float to Int
gpa=int(gpa)
print(gpa)
    #3


#input() - a function that prompts the user to enter data
#           Returns the entered data as a string

name = input("What is your Name?")
age = int(input("Enter your age?"))
#typecasting is used because the value stored as a string so we need to convert it to a integer for do
#mathmatical operations
age = age + 1
print(f"Hello {name}")
print(f"Now your age is {age}.")

#shopping cart

item = input("What would you like to have?")
price = float(input("What is the Price"))
qty = int(input("How many would you like to buy?"))

total = price * qty

print(f"You have bought {item} and the total price is {total}")





