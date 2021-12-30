#collections : counter, namedtuple, OrderDict, defaultdict, deque
from collections import Counter

a = "aaaaaabbbbcccc"

my_counter = Counter(a)

print(my_counter)

print(my_counter.items())

print(my_counter.keys())

print(my_counter.values())

print(my_counter.most_common(1))

#to see only the element

print(my_counter.most_common(1)[0][0])

#printing elements of my collection

print("\n.\n.\n.\n#")

print(my_counter.elements())

print(list(my_counter.elements()))

from collections import namedtuple
print("\n.\n.\n.\n#")

Point = namedtuple('Point', 'x,y')

pt = Point(1,-4)

print(pt)

print("\n#")

print(pt.x, pt.y)

from collections import OrderedDict

ordered_dict = OrderedDict()


ordered_dict['b']=2
ordered_dict['c']=3
ordered_dict['d']=4
ordered_dict['a']=1


print(ordered_dict)

#default dict

from collections import defaultdict

print("\n.\n.\n.\n#")

d = defaultdict(int)
d['a'] = 1
d['b'] = 2

print(d['c']) #print de default value of  defaultdict in brackets with a normal dict this show a key error 

d=defaultdict(float)

print(d['c'])

d=defaultdict(str)

print(d['c'])

#deque  Deque is preferred over a list in the cases where we need quicker append and pop operations from both the ends of the container

from collections import deque
d = deque()

print("\n.\n.\n.\n#")

d.append(1)
d.append(2)

d.appendleft(3)


print(d)

d.pop()
print("-Removing the last elemnet: ", d)

d.append(2)
d.popleft()
print("-Removing the first element", d)

d.clear()

print("-Removing all the items: ", d)

d.extend([4,5,6])

print("-Adding elements with extend: ", d)

d.extendleft([1,2,3])

print("-Adding elements at left: ", d)

d.rotate(1)

print("-Rotating my deque a place to the right: " ,d)




