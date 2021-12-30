#itertools iterators are datatype for use in a for loop the most common is the list
# prodtuct -  permutations  -  combinations  - accumulate function  -  groupby function  -  infinite itarators

from itertools import product

a = [1,2]
b= [3]

prod = product (a,b)

print(prod)
print(list(prod))

#repeat



prod = product (a,b, repeat=2)

print("\n-Repeating the product: ",list(prod))

from itertools import permutations

#return all posibles orderings

a= ['p','o','r']
perm = permutations(a,2)

print(f"-Printing the permutation of: {list(a)}: \n{list(perm)}")

from itertools import combinations, combinations_with_replacement
#make all posible combinations with specify len with out repeating elements
comb = combinations(a,2)

print(f"\n-Printing the combinations of: {list(a)}: \n{list(comb)} ")

comb_wr = combinations_with_replacement(a,2)

print(f"\n-Printing the combinations with replacement of: {list(a)}: \n{list(comb_wr)} ")

from itertools import accumulate
#make a iterators return an accumulate somes or other binary function 

acc = accumulate(a)

print(f"\n-Printing the acumulate of: {list(a)}: \n{list(acc)} ")

#also we can import operator for multiply instead plus 

import operator
b=[1,2,3,2]

acc2= accumulate(b, func=operator.mul)
print(f"\n-Printing the acumulate with operator of: {list(b)}: \n{list(acc2)} ")

from itertools import groupby

#is  an itarator that return keys and groups

def smaller_than1_3(x):
    return x<3

a = [1,2,3,4]

group_obj = groupby(a, key=smaller_than1_3)

print("\nGroup by:")
for key, value in group_obj:
    print(key, list(value))

#groupby dictionaries
print("\nGroup by age:")

persons = [{'name':'Tim', 'age':25},{'name':'Dan', 'age':25},
        {'name':'Liam', 'age':31},{'name':"Tim" ,'age':23}]

group_persons = groupby(persons,key=lambda x: x['age'])

for key, value in group_persons:
    print(key, list(value))

from itertools import count, cycle, repeat #count(inicial_value) repeat(n, times)

for i in count(10):
    print(i)

    if i==20:
        break

print("\n\n#Count cycle repeat")

a = [1,2,3]

#for i in cycle(a):
#    print(i)
    #untilcondition

for i in repeat(1,4):
    print(i)
