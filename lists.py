mylist= ["banana", "cherry", "apple"]

print("\n printiing  my list manually ")
print(mylist)
#print manually my list
item = mylist[0]
item2= mylist[1]
item3 = mylist[2]

print("This is the item number 1 " + item)
print("This is the item number 2 "+ item2)
print("This is the item number 3 "+ item3)

#print mylist in a loop
print("\n.\n.\n.\n printing mylist in a loop")
number= len(mylist)

for i in range(0,number):
    print ("This is the item number " + str(i+1)+" "+ mylist[i])

#Checking if an item is on mylist
print("\n.\n.\n.\n Checking if an item is on mylist")

if "banana" in mylist:
    print("yes")
else:
    print("no")

if "orange" in mylist:
    print("yes")
else:
    print("no")

#Appending an item on mylist
print("\n.\n.\n.\n Appending an item on mylist")
print(mylist)
mylist.append("lemon")
print(mylist)

#Insert an item in a specific position
print("\n.\n.\n.\nInsert an item in a specific position. Ex. position number 1")

mylist.insert(1,"blueberry")
print(mylist)

#Removing an item 
print("\n.\n.\n.\nRemoving an item, the last one")

item= mylist.pop()

print(item)
print(mylist)

print("\n.\n.\n.\nRemoving an item, an especific")

item= mylist.remove("blueberry")
print(item)
print(mylist)

#removing all items
print("\n.\n.\n.\nRemoving all items")
mylist.clear()
print(mylist)

#Reverse the list
print("\n.\n.\n.\nReverse the list")
mylist= ["banana", "cherry", "apple"]
print(mylist)
mylist.reverse()

print(mylist)


#Sorting my list
print("\n.\n.\n.\nSorting mylist")
print(mylist)
mylist.sort()
print(mylist)

#sorting with out change original list

print("\n.\n.\n.\nSorting with out change original list")

mylist2 = [4, 3, 1,-4,-2 ,-1]
print("Printing my list")
print(mylist2)

new_list= sorted(mylist2)
print(new_list)

print("Printing my list")
print(mylist2)

#creating a list with repeat element
print("\n.\n.\n.\nCreating a list with repeat element")

mylist= [0] * 5
print(mylist)

#concatenate with + operator
print("\n.\n.\n.\nConcatenate with + operator")
b=mylist+mylist2
print(b)

#Creating a list with an existing list

print("\n.\n.\n.\nCreating a list with an existing list")

a=b[5:9]
print(a)
#Reversing
a=b[::-1]
print(a)

a=b[::2]
print(a)

#coping a list and copy() method

print("\n.\n.\n.\nCoping a list")
list_org =  ["banana", "cherry", "apple"]

list_cpy = list_org
list_cpy.append("lemon")
print("without copy method")
print(list_org)
print(list_cpy)

#we can use list_cpy=list(list_org) or list_cpy=list_org[:]
print("\n with copy() method")
list_org =  ["banana", "cherry", "apple"]

list_cpy = list_org.copy()
list_cpy.append("blueberry")

print(list_org)
print(list_cpy)


list_cpy.append

#if i modify my list_cpy i will modify the original one too

#create a list with changes on one line of code
print("\n.\n.\n.\nCoping a list with changes on one line of code")


mylist = [1,2,3,4,5,6]

b= [i*i for i in mylist]

print(mylist)
print(b)
