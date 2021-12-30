# Tuple
myTuple = ("Max", 28 , "Boston")

print(myTuple)

#if i want create a single object tuple
print("\n.\n.\n.\n if i want create a single object tuple")
mytuple1= ("Max",)

print(type(mytuple1))

#Create a tuples from tuple() function
print("\n.\n.\n.\n #Create a tuple from tuple() function")
myTuple = tuple(["MAX",28,"BOSTON"])

print(myTuple)
print(type(myTuple))

#tuples behavior is similar to lists

print("\n.\n.\n.\n #tuples behavior is similar to lists")

item1 = myTuple[0]
item2 = myTuple[1]
item3 = myTuple[2]

print("First item")
print(item1)

print("Second item")
print(item2)

print("Third item")
print(item3)

#A tuple is unmutable myTuple[0]="Frank" --> this is wrong

print("\n.\n.\n.\n #Looping a Tuple\n")

for i in myTuple:
    print(i)

#checking items in tuple

print("\n.\n.\n.\n #checking items in tuple")

if "MAX" in myTuple:
    print("YES")
else:
    print("NO")


print("\n.\n.\n.\n #Some usefull method with tuples")

myTuple= ('a','p','p','l','e')
print(len(myTuple))
print(myTuple.count('p'))
print(myTuple.index('p'))

my_list= list(myTuple)

print(type(my_list))

#slicing with tuples
print("\n.\n.\n.\n #slicing with tuples")

a=(1,2,3,4,5,6,7,8,9,10)

b = a[2:5]

print(b)

print("\n.\n.\n.\n #Naming objects in tuple")

myTuple = ("Max", 28 , "Boston")

name,age,origin = myTuple

print(name)
print(age)
print(origin)

#tuples are inmutable
print("\n.\n.\n.\n #Comparing list with tuples")

import sys
myTuple=(0, 1, 2, "hello", True)
myList=[0, 1, 2, "hello", True]

print(sys.getsizeof(myList), "bytes")
print(sys.getsizeof(myTuple), "bytes")

print("\n.\n.\n.\n #Calculate time in tuples")

import timeit

print("Timeing create lists")
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))

print("Timing creating tuples")
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))