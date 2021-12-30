# Sets: mutable, no duplicates, unorder

myset = {1,2,3,4,5,1,2}

print(myset)

#set function

print("\n.\n.\n.\n#")
mylist=[1,"banana",2]

myset = set(mylist)

print(myset)

mysetstring= set("hello")

print(mysetstring)

#create a empty set must be with set function

print("\n.\n.\n.\n#")
emptyset= set()

print(emptyset)

#Add elemnts to my set wit add method

print("\n.\n.\n.\n#")
emptyset.add(1)

print(emptyset)

#Remove elemets with the remove method


print("\n.\n.\n.\n#")
emptyset.remove(1)
#emptyset.discard(1) do the same thing but if the element isnt in the set, nothing happens, no error in this method.
#myset.clear()
#myset.pop()

print(emptyset)

#loop set

print("\n.\n.\n.\n#")
for i in myset:
    print(i)

#element in set?

print("\n.\n.\n.\n#")
if 1 in myset:
    print(True)

#union with set

print("\n.\n.\n.\n#")
odds= {1,3,5,7,9}

evens = {0,2,4,6,8}

primes= {2,3,5,7}

u = odds.union(evens)

print(u)

#intersection two sets


print("\n.\n.\n.\n#")

inter= odds.intersection(primes)

print(inter)

#difference of two sets 

print("\n.\n.\n.\n#")
setB={1,2,3,10,12,4,5,14}

diference=u.difference(setB)

diference2=setB.difference(u)

print(diference)

print("\n#")

print(diference2)

diference3=u.symmetric_difference(setB)

print(diference3)


#updating sets

print("\n.\n.\n.\n#")
u.update(setB)

print(u)

setA={1,2,3,4,5,6,7,8,9}

setA.intersection_update(setB)

print(setA)

#superset


print("\n.\n.\n.\n#")

setA = {1,2,3,4,5,6}
setB = {1,2,3}
setC = {7,8,9}

print(setA.issuperset(setB))
print(setB.issubset(setA))
print(setA.isdisjoint(setC))

#a=frozenset([1,2,3,4]) 