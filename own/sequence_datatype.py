#collection - single "variable" used to store multiple values
#List = [] ordered and changeable. Duplicates are accepted

#List
fruit = ["Apple","Orange","Banana","Coconut"]
print(fruit)
#to access each element of the list
print(fruit[1])
#to access multiple element of the list
print(fruit[1:3])

for x in fruit:
    print(x)
print(help(fruit))

#to change the value of the mentioned index element
fruit[0]="Pineapple"
print(fruit)
#OR
#insert
fruit.insert(3,"Mango")
#append - is used to add element at the end of the list
fruit.append("Apple")
print(fruit)

#remove - is used to remave an element of the list
fruit.remove("Banana")
print(fruit)

#sort - is used to align the elements of the list in ascending order
fruit.sort()
print(fruit)

#reverse - is used to reverse the elements of the list
fruit.reverse()
print(fruit)
#OR
print(fruit[::-1])

#index - is used to find index value of the an element of the list
print(fruit.index("Apple"))

#clear - it is used to clear the entire elements of the list
fruit.clear()
print(fruit)


