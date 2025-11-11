name = input("Enter your Name: ")

#to find the length of the string
i = len(name)
print(i)

#to find the index value of a given character in the string
i = name.find("r")
print(i)

#to find the index value of a given character in string in reverse order
i = name.rfind("r")
#i = name.zfill
print(i)
#if a given character is doesnt exist in the string it returns -1

#to capitalize the first character of the string
i = name.capitalize()
print(i)

#to capitalize all the character of the string
i = name.upper()
print(i)

#to lower all the character of the string
i = name.lower()
print(i)

#to check the string is it only has integer or not(returns True or False)
i = name.isdigit()
print(i)

#to check the string is it only has alphabetical values or not
i = name.isalpha()
print(i)

#to check a mentioned characters is how many time present in the string
i = name.count("r")
print(i)

#to replace a mentioned character in the string
i = name.replace("h","n")
print(i)


#validate user input exercise
#username is no more than 12 characters
#useername must not contain spaces
#username must not contai digits

username = input("Enter your username: ")

if len(username)>12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print("logined")


#indexing - accessing elements of a sequence using [].
#           [start : end : step]

card_no = "1234-5678-9012-3456"
#start
print(card_no[0])#--> 1 is printed
print(card_no[:4])#--> 1234 is printed
print(card_no[5:9])#--> 5678 is printed

#end
print(card_no[5:])#--> 5678-9012-3456 is printed
print(card_no[-1])#--> 6 is printed
print(card_no[-4:])

#step
print(card_no[::2])#--> 13-6891-46 is printed
#it prints every 2nd character of the string

print(card_no[::3])#--> 146-136 is printed
    
