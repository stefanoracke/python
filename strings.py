#string are inmutable

mystring = 'Hello World!'

print(mystring)

my_string= 'I\'m a programmer'

print(my_string)

otherwise= "I'm a programmer"

print(otherwise)

#multiple lines

print("\n.\n.\n.\n#")

multiple="""Hello
World"""#use for documentation

print(multiple)

#Characters in strings


print("\n.\n.\n.\n#")
char = mystring[0]


print(char)

#looping a string
for i in mystring:
    print(i)

#substring


print("\n.\n.\n.\n#")

substring = mystring[1:5]

print(substring)

#sentence

greeting= "Hello"

name = "Tom"

print(greeting+ " " +name)

#strip Method

print("\n.\n.\n.\n#")
mystring = "    Hello World!     "
print(mystring)
mystring = mystring.strip()

print(mystring)

#uppercase

print("\n.\n.\n.\n#")
print(mystring.upper())

#lower


print("\n.\n.\n.\n#")
print(mystring.lower())

#Start with a charecter starwith() endswoth()

print(mystring.startswith("H"))

#find a char

print(mystring.find("o"))

#count char

print(mystring.count("o"))

#replace

print("\n.\n.\n.\n#")
print(mystring.replace("World", "Universe"))

#split method, transform a string in a list

mystring = "how are you doing"

mylist = mystring.split()

print(mylist)

#method join

newstring= ' '.join(mylist)
print(newstring)

from timeit import default_timer as timer

mylist = ['a']*100000

#badway to transform
start = timer()
my_string = ''

for i in mylist:
    my_string += i

stop = timer()
print(stop-start)

#good
start= timer()
my_string = ''.join(mylist)
stop = timer()
print(stop-start)

#methods %, format(), f-Strings %s = string  -- %d = integer -- %.(n)f = floating n=indicates the number of decimals
var = "Tom"
var1 = 3
var2= 3.14323213
my_string = "The variable is %s" %var
#my_string = "The variable is %d" %var1
#my_string = "The variable is %f" %var2

print(my_string)

#format method
print("\n.\n.\n.\n#")
my_string = "The variable is {} and {:.2f}".format(var,var2)
print(my_string)

#the newest way f-strings
print("\n.\n.\n.\n#")
my_string=f"The most efficient is {var*2}"
print(my_string)



