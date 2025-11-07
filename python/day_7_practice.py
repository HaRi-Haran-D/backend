#1. merge two dict into a new dict and print only the keys of the merge dict?

dict1 = {"name":"Hari","age":25,"location":"chennai"}
dict2 = {"hobby":"Chess","food":"Biriyani"}

dict1.update(dict2)
dict3 = dict1
#dict3={**dict1,**dict2}
print(dict3.keys())

#2. create a dict with a nested dict of person and print his AGE

stud = {"person":{"name":"JK","age":24}}

print(stud.get("person")["age"])

#3. delete all keys in dict

dict4 = {"name":"Hari","age":25,"location":"chennai","hobby":"Chess","food":"Biriyani"}

dict4.pop('name')
print(dict4)
