'''
#Reverse a list
list1=['df','qw','ty',32,34,12,67,'hk']
list2=[]
for i in range(len(list1)-1,-1,-1):
    list2.append(list1[i])
print(list2)


#palindrome
def pali(w):
    p=w[::-1]
    if p==w:
        print(f'{w} is a Palindrome')
    else:
        print(f'{w} is not a Palindrome')
pali('madam')
pali('denmark')
    


#add even numbers
def even(a,b):
    n=0
    for i in range(a,b):
        if i%2==0:
            n+=i
    return n

print(even(1,11))

#add odd numbers
def odd(a,b):
    n=0
    for i in range(a,b):
        if i%2 != 0:
            n+=i
    return n

print(odd(1,12))
'''

list3 = [1,2,3,4]
n=list3[2:]+list3[:2]
print(n)




