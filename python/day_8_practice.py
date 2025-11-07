#practical questions
'''
for i in range(0,5):
    for j in range(0,i):
        print(" * ", end='')
    print()

for i in range(1,6):
    for j in range(5,i,-1):
        print(' * ', end='')
    print()

#len() iteration
name='Monkey-D-Luffy '
for i in range(len(name)+1):
    for j in range(i):
        print(name[j],end='')
    print()


names = ['james','venkat','keshav','joseph','abi']
for i in names:
    print(i)

#to pop an item in the list
names.pop()
print(names)

#to remove an item 
#names.remove('james')
#print(names)
    
#to print values which has j in there values
j_names=[]
for i in names:
    if 'j' in i:
        j_names.append(i)
print(j_names)

#to remove the value j in the list
for i in names:
    if 'j' in names:
        i.replace('j','')
print(i)

car = {'name':'a6','brand':'audi'}
del car['name']
del car['brand']
print(car)

person = {'name':'hari','state':'chennai'}

for i in person:
    print(i,' : ',person[i])
    

#dict
#to set default value in dict

employ = {'id':12,'name':'Hari'}
'''


#count how many students passed in a list:

#method 1 to print the fail marks
marks = [90, 45, 67, 32, 80,20,25,78,12,34,23]
j=0
fail=[]

for i in range(len(marks)):
    if marks[i]<50:
        j = marks[i]
        fail.append(j)
print(f'Fail marks are: {fail}')

#method 2 to print the no. of fail students

pass_mark = 50
count = 0

for i in marks:
    if i <= pass_mark:
        count += 1

print(f'Total no. of fail students is {count}')

#Finding vowels in a word and counts

#word = str(input("Enter a word: "))
word = "Concentration"
vowels=['a','e','i','o','u','A','E','I','O','U']

#1.Find vowels in a word
j=[]
for i in word:
    if i in vowels:
        j.append(i)
        #j.sort()
print(j)

a=word
for i in word:
    if 'a' in i:
        a=a.replace('a','')
    elif 'e' in i:
        a=a.replace('e','')
    elif 'i' in i:
        a=a.replace('i','')
    elif 'o' in i:
        a=a.replace('o','')
    elif 'u' in i:
        a=a.replace('u','')
print(a)

'''
result = ""

for i in word:
    if i.lower() not in ['a', 'e', 'i', 'o', 'u']:
        result += i

print(result)
'''

#2. give only vowels count
count = 0
for i in word:
    if i in vowels:
        count+=1
print(count)


#3.count vowels and consonants in a given string:
word = "Concentration"
vowels=['a','e','i','o','u','A','E','I','O','U']
consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z',
             'B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
vowels_count = 0
consonant_count = 0
for i in word:
    if i in vowels:
        vowels_count+=1
    elif i in consonant:
        consonant_count+=1
    else:
        print('invalid')
print(f"Total no of Vowels in {word} is {vowels_count}")
print(f"Total no of Consonants in {word} is {consonant_count}")

