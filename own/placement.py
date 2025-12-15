# print name in all possible combinations
'''
from itertools import permutations
name=input('enter name:')
name_combinations=permutations([i for i in name],len(name))
print('all possible combinations of',name,'is:')
print('---------------------------------------')
c=0
for j in name_combinations:
    c+=1
    print(j)
print("Total number of combinations:",c)
'''
# name pyramid
'''
name = input("Enter Name:")
a=len(name)
for i in range(1,a+1):
    for j1 in range(a+1,i,-1):
        print('',end=' ')
    for j in range(0,i):
        print(name[j],end=' ')
    print()
'''

# count character frequency in a name
'''
name=input('enter name:')
from collections import Counter
data=Counter(name)
print('character frequency distribution of',name,'is:')
print(str(data))
'''
# remove vowels from a name
'''
name=input('enter name:')
print(name)
for i in name:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        print('',end='')
    else:
        print(i,end='')
'''
# remove vowels from a name/string
'''
class Solution(object):
   def removeVowels(self, s):
      s = s.replace("a","")
      s = s.replace("e","")
      s = s.replace("i","")
      s = s.replace("o","")
      s = s.replace("u","")
      return s
obj = Solution()
print(obj.removeVowels(input("Enter String :")))
'''
# counting vowels
'''
n = input("Enter String ")
lc = n.lower()
#apple
vc = {}
for v in "aeiou":
    c = lc.count(v)
    vc[v] = c #1,1 : vc['a':1,'e':1]

counts = vc.values()
total = sum(counts)
print("total vowels in string" ,total)

'''

# matrix multiplication
'''
X = [ [1,2],[3,4]] # 2x2

Y = [ [1,2],[3,4]] # 2x2

result = [ [0,0],[0,0] ]


for i in range( len(X) ):
    for k in range(len(Y[0])):
        for j in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
  
for r in result:
   print(r)
'''
# armstrong numbers
#153 , 1+125+27 = 153
'''
num = (input('enter number:'))
a=int(num[0])**3
b=int(num[1])**3
c=int(num[2])**3
data=str(a+b+c)
print(num)
print(data)
if num==data:
    print(num,'is armstrong')
else:
    print(num,'is not armstrong')
'''
# palindrome

'''
name=input('enter word:')
if name==name[::-1]:
    print(name,'is palindrome')
else:
    print(name,'is not palindrome')
 
'''
# Factorial Program
'''
num = int(input('enter number:'))
def fact(num):
    if num<1:
        return 1
    else:
        return num*fact(num-1)
print(fact(num))
'''
# prime numbers
'''

number = int(input("Enter any number: "))

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
              break
    else:
        print(number, "is a prime number")

else:
    print(number, "is not a prime number")

'''
# counting number of words in a string/name
'''
test_string = input("Enter String :")

print ("The original string is : " + test_string)
res = len(test_string.split())
print ("The number of words in string are : " + str(res))

'''
# pgm to shutdown computer
'''
import os 
  
shutdown = input("Do you wish to shutdown your computer ? (yes / no): ") 
  
if shutdown == 'no': 
    exit() 
else: 
    os.system("shutdown /s /t 1")
'''


# anagrams
'''
s1=input("Enter first string:")
s2=input("Enter second string:")
if(sorted(s1)==sorted(s2)):
      print("The strings are anagrams.")
else:
      print("The strings aren't anagrams.")
'''

# swapping of two words
'''
n='Softlogic'
n1='SLA'
print("Before swapping")
print("name 1",n)
print("Name 2",n1)
print("After swapping")
c=n
n=n1
n1=c
print("name 1:",n)
print("name 2:",n1)

'''

#Amicable
'''
n=int(input("n=")) # 24
l1=[]
n1=int(input("n1=")) # 35
l2=[]
for x in range(1,n): # 24 , 24%1 ==0 yes
    if(n%x)==0:
        l1.append(x)
#print(sum([x]))
for y in range(1,n1):
    if(n1%y)==0:
        l2.append(y)

#print("List-1:(220):",l1)
#print("List-2:(284):",l2)

#print("Added Elements (220)are:",sum(l1))
#print("Added Elements (284)are:",sum(l2))
a=sum(l1)
b=sum(l2)

if(n==b)and(n1==a):
    print(n,n1,"is amicable pairs")
else:
    print("Oops")
'''
#---------------------------------------

'''
str1 = input("Enter First String :")
str2 = input("Enter Second String :")  
   
print("Strings before swapping: " + str1 + " " + str2)
   
str1 = str1 + str2 
 
str2 = str1[0 : (len(str1) - len(str2))]
  
str1 = str1[len(str2):]
   
print("Strings after swapping: " + str1 + " " + str2)
'''
# finding most occured element

'''
list1 = [50, 20, 51, 50, 17, 45, 48, 19, 50]
print("Given List:\n",list1)
res = max(set(list1), key = list1.count)
print("Most Ocuured Element:\n",res)
'''

# sorting words/name in a sentence
'''
my_str = input("Enter String : ")
words = [word.lower() for word in my_str.split()]

words.sort()
print(words)

print("The sorted words are:")
for word in words:
   print(word)
'''
# lcm

'''
def lcm(x, y):  
          if x > y:  
              greater = x  
          else:  
              greater = y  
          while(True):  
              if((greater % x == 0) and (greater % y == 0)):  
                  lcm = greater  
                  break  
              greater += 1  
          return lcm  
num1 = 12  
num2 = 20  
print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))
'''
# hcf
'''
def hcf(x, y):  
        if x > y:  
            smaller = y  
        else:  
            smaller = x  
      for i in range(1,smaller + 1):  
            if((x % i == 0) and (y % i == 0)):  
               hcf = i  
      return hcf  
  
    num1 =24  
    num2 =54 
    print("The H.C.M of", num1,"and", num2,"is", hcf(num1, num2))
'''
# matrix transpose

'''
X = [[1,2] , [4,5] , [7,8]]  
  
result = [[0,0,0] , [0,0,0]]  
  
    # iterate through rows  
for i in range(len(X)):  
    for j in range(len(X[0])):
        result[j][i] = X[i][j]  

for r in result:  
    print(r)
'''
# bubble sort
'''
def bubblesort(list):

    # Swap the elements to arrange in order
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp


list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)
'''

# continuous alphabet pattern
'''
def  contalpha(n): 
      
    # initializing value corresponding to 'A'  
    # ASCII value 
    num = 65
    for i in range(0, n):
       for j in range(0, i+1): 
          ch = chr(num) 
          print(ch, end=" ") 
          num = num +1
    print(" ") 

contalpha(3)
'''

