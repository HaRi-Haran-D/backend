data = {}

name=input("Enter Your Name:")
s= lambda n:n.upper()
data['Name']=s(name)

age=int(input('Enter your age:'))
f = lambda n:n+2
data['Age']=f(age)

print(data)
