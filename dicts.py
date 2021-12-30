#Dictionary: KeyValues pairs, Unorder, Mutable

myDict =  {"name":"Max" , "age": 25, "city":"Boston"}

print(myDict)

#Creating a dict with dict(function)

myDict2= dict(name="Mary",age=24,city="New York")
print(myDict2)

#Calling values with its keys

print("\n.\n.\n.\n#")

value_name= myDict["name"]
value_age = myDict["age"]

print(value_name)

print(value_age)

#New key in dict
print("\n.\n.\n.\n#")

myDict["email"]="max@xyz.com"

print(myDict)

#Delete items

print("\n.\n.\n.\n#")

del myDict["name"]

print(myDict)

myDict.pop("age")
print(myDict)

myDict =  {"name":"Max" , "age": 25, "city":"Boston"}

#Search a key on a Dict

print("\n.\n.\n.\n#")

if "name" in myDict:
    print(myDict["name"])

try:
    print(myDict["lastname"])
except:
    print("Error")


#loop a Dict
print("\n.\n.\n.\n#")

for key in myDict:
    print(key)

for value in myDict.values():
    print(value)

#two in one

for key, value in myDict.items():
    print(key, ": " ,value)

#tuples and numbers can be keys

print("\n.\n.\n.\n#")

mytuple=(8,7)
mydicti={mytuple:15}

print(mydicti)