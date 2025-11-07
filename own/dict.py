#dictionary - a collection of {key:value} pairs
#           ordered and changeable, No duplicates

capital = {"USA":"Washington D.C",
           "India":"New Delhi",
           "China":"Beijing",
           "Russia":"Moscow"}

#get() - to get the value of the metioned key in the dict
#if not returns none
print(capital.get("USA"))

#update() - to add new key and values or change the existing key and value to the dict
capital.update({"Germany":"Berlin"})
print(capital)

#pop() - to remove key and value
capital.pop("China")
print(capital)

#popitem() - to remove last key and value which has been added
#capital.popitem()
#print(capital)

#clear() - to delete all the key and values in the dict
#capital.clear()
#print(capital)

#keys() - to is used return all the keys in the dictionary
key = capital.keys()
print(key)

#in for loop
for i in capital.keys():
    print(i)

#values() - is used return all the values in the dictionary
value = capital.values()
print(value)

#in for loop
for i in capital.values():
    print(i)

#items() - to list the values in 2D tuple form
item = capital.items()
print(item)

#in for loop
for key,value in capital.items():
    print(f"{key}:{value}")





