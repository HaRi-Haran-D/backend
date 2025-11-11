#Set = {} unordered and immutable, but Add/Remove Ok, No Duplicates are accepted

fruit = {"Apple","Orange","Banana","Coconut"}
print(fruit)#--> {'Banana', 'Coconut', 'Orange', 'Apple'}
print("Pineapple" in fruit)#--> False

#add - is used to add an element into the set
fruit.add("Pineapple")#--> {'Pineapple', 'Orange', 'Coconut', 'Apple', 'Banana'}
print(fruit)

#remove - is used to remove an element in the set
fruit.remove("Pineapple")
print(fruit)#--> {'Orange', 'Coconut', 'Apple', 'Banana'}

#pop - is used to delete the first(random because the values are alternative everytime) element of the set
fruit.pop()
print(fruit)#--> {'Coconut', 'Apple', 'Banana'}

#clear - is to clear every element of the set
fruit.clear()
print(fruit)#--> set()

#Tuple = () ordered and unchangeable. duplicates are accepted and faster

fruit = ("Apple","Orange","Banana","Coconut")

print(fruit.index("Banana"))#--> 2

print(fruit.count("Coconut"))#--> 1
