#Set = {} unordered and immutable, but Add/Remove Ok, No Duplicates are accepted

fruit = {"Apple","Orange","Banana","Coconut"}
print(fruit)
print("Pineapple" in fruit)

#add - is used to add an element into the set
fruit.add("Pineapple")
print(fruit)

#remove - is used to remove an element in the set
fruit.remove("Pineapple")
print(fruit)

#pop - is used to delete the first(random because the values are alternative everytime) element of the set
fruit.pop()
print(fruit)

#clear - is to clear every element of the set
fruit.clear()
print(fruit)

#Tuple = () ordered and unchangeable. duplicates are accepted and faster

fruit = ("Apple","Orange","Banana","Coconut")

print(fruit.index("Banana"))

print(fruit.count("Coconut"))
