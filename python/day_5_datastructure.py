'''
Datastructure/native datatypes
list
tuple
set
dict
'''
lista=['hello',232,3224,'python','game',23,45,97,'hari']

#index - index value starts from 0
print(lista[4])
#'game' was printed

#append - add value to the list at the end
#one value will be added at the end of the list[]
lista.append('end')
print(lista)
#['hello',232,3224,'python','game',23,45,97,'hari','end']


#count - is used to count the given value is how many times present in the list
#(or used to find any duplicate in the list)
lista.count(232)
print(lista.count(232))

#sort - is used to align the list values in ascending order
val=['ad']

val.sort()

#val = sort(reverse=True) #is used to align the list values in descending order


#tuple

t1=(1,2,34,'hbfa','hlsafdl','asf',42)

print(t1.index(42))
#6 is printed

t2=('ad','gd')
t3=t1+t2
print(t3)

print(t1*2)

print(t3*3)

print(t3.count(42))


#set

a={1,5,45,8,9,10}
print(a)


b ={1,3,5,6,9}
print(b)

#a.add()
