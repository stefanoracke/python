#is a function one line and anonymous function --> 
'''lambda arguments:expression'''
#We use lambda function if we need use it only once in our code or like an argumente to higher other function

add10= lambda x: x + 10

'''
def add10(n)    
    return n+10
'''

print(add10(5))

mult = lambda x,y: x*y

print(f"-The multiply of 2 and 7 is: {mult(2,7)}")

points2D = [(1,2),(15,1),(5,-1),(10,4)]

points2D_sorted= sorted(points2D, key=lambda x: x[1])

'''
def sorted(x):
    return x[1]
    
points2D_sorted= sorted(points2D, key=sorted)
'''
print(f"\nExamples of sorting with lambda function: \n{points2D} \n{points2D_sorted}")

points2D_sorted_plus= sorted(points2D, key=lambda x: x[0]+x[1])

print(f"Summatory of x,y sort: {points2D_sorted_plus}")

#map func map(func, seq)

a = [1,2,3,4,5]

b= map(lambda x: x*2, a)

print(f"\nMap function: {list(b)}")

c= [x*2 for x in a]
print(c)

#filter function filter(func, seq), return all elements of value=True

a = [1,2,3,4,5,6]

b= filter(lambda x: x%2==0, a)

print(f"\n Filter function evens numbers: {list(b)}")

#reduce function reduce(func, seq), repeatly aplly the function to the elements and return a single value
from functools import reduce
a=[1,2,3]
prod_a= reduce(lambda x,y: x*y,a)

print("The reduce function with a product = ",prod_a)


