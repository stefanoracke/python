#change from python dict to JSON object
import json

person = {
    "name":"Jhon",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer","programmer"]
}

personJSON = json.dumps(person, indent=4, sort_keys=True)

print(personJSON)

#Create a json file with a python dict.
with open('person.json', 'w') as file:
    json.dump(person, file,indent=4)

#Convert back into a dict personJSON

person = json.loads(personJSON)

print("\n\nConverting in python dict:\n",person)

#converting with json file

with open('person.json', 'r') as file:
    person = json.load(file)
    print("\n\nConverting with json file:\n",person)

class User:

    def __init__(self,name,age):
        self.name = name
        self.age = age

user = User('Max',27)

def endcode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)



user1JSON= UserEncoder().encode(user)
print("using UserEncoder: ", user1JSON)


userJSON = json.dumps(user, default=endcode_user)

print("The User is: \n",userJSON)

with open('user.json','w') as file:
    json.dump(userJSON,file)

#is not an object then we use decode

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'],age=dct['age'])

    return dct

user = json.loads(userJSON, object_hook=decode_user)

print(f"Decode_user calling like an object:\n The name is:{user.name} \n The age is:{user.age}")