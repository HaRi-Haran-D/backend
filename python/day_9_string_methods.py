#String inbuilt function
#string means sequences of characters which is enclosed in single or double quotes
#accepts alphanumeric values
#set of inbuild methods(string)

age = '31'
print(type(age))#--> str

name = "python"

#capitalize() - is used to change the first 
print(name.capitalize())#--> Python

#casefold() - is used to change all the uppercase values to lowercase
print(name.casefold())#--> python

#count() - is used to find the argument is how many present in the string
print(name.count('o'))#--> 1

#endswith() - is used to find the argument is present as the end value or not in the string and returns true or false
print(name.count('f'))

#expandtabs() - is used to change the space between the string by the given argument
tab = "demo\tclass"
print(tab.expandtabs(6))

#find() - is used to find the argument is present in the string or not
print(tab.find('s'))

#isalnum() - is used to find that all the charecters in the string is numbers or not
#print(name.isalnum())
#print(age.isalnum())

#identifier()
print(name.isidentifier)

name1 = 'my name'
print(name1.isidentifier())#--> False

print(name.isnumeric())#--> False
print(name.isprintable())#--> True
print(name.isspace())#False
print(name.istitle())#False

#upper() is used to find is all the characters of the string is upper or not
print(name.isupper())#False
name1 = "HARI"
print(name1.isupper())#True
print(name.islower())#True

#join()
print(name.join('123'))#--> 1python2python3


#format
#{placeholder}
#named
#numbered
#placeholder{}sen='my course name is {fname} and fee is {fees}'

#named
course = "my course name is {fname} and fee is {fees}".format(fname='Python',fees='30000')
print(course)#--> my course name is Python and fee is 30000

#numbered
course = "my course name is {0} and fee is {1}, course starts at {2}".format('Java',40000,'Saturday')
print(course)#--> my course name is Java and fee is 40000, course starts at Saturday

#empty
courses = "my course name is {} and fee is {}, course starts at {}".format('MERN',25000,'Monday')
print(course)#--> my course name is MERN and fee is 25000, course starts at Monday

#format_map: it hold dict values
mystr = {'stdname':'Hari','age':25,'city':'Chennai'}
text = 'Hello all Iam {stdname}, and my age is {age}, and Iam from {city}'
print(text.format_map(mystr))#--> Hello all Iam Hari, and my age is 25, and Iam from Chennai

#tuple values and dict values

tupl = ('mouse','monitor','keys')
x='sla'.join(tupl)
print(x)


dict1 = {'key1':'AB1','key2':'AB2'}
dicta = {'key1':'AB1','key2':'AB2','key3':45}

x = 'jj'.join(dict1.values())


