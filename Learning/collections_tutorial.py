# Containers
# list
# set
# dict
# tuple - immuttable

# Types
# 1 counter
# 2 deque
# 3 namedTuple()
# 4 orderedDict
# 5 defaultdict

import collections

# from collections import Counter

"""COUNTER"""
"""The counter will count every instance of a certain element from any collection data type. """
""
c = Counter("hello")
print(c)
print(c["h"])
print(c.most_common(1))  # returns [(1, 3)]
c.most_common(2)  # returns [(1, 3), (7, 2)]

c = Counter([1, 1, 1, 3, 4, 5, 6, 7, 7])
d = [1, 1, 3, 4, 4]

c.subtract(d)

print(c)  # prints Counter({1:1, 3:0, 4:-2, 5:1, 6:1, 7:2})

print(list(c.elements()))
c.update(d)

print(c)

c.clear()
print(c)""

"""NamedTuple"""
"""used to give names to the elements within a tuple object and make for easier code readability. """
import collections
from collections import namedtuple

# Point = namedtuple("name", "paramater1, parameter2, parameterx")
# p = Point(1,4,5)
# print(p)  # prints name(parameter1=1 ,parameter2=4 , parameterx=5)

Point = namedtuple("Point", "x y")

p = Point(1, 4)

print(p.x)  # prints 1
print(p.y)  # prints 4
print(p)  # prints Point(x=1, y=4)
print(p.x, p.y)
print(p._asdict())  # prints

p = p._replace(y=6)  # because _replace is not able to update/replace tuple object

"""DEQUE"""
"""The deque object is typically used to perform fast operations on the beginning and and of a list. It should only be used when you care more about manipulating data and taking items from the beginning and end of the list rather than random lookups of elements.
"""
import collections
from collections import deque

d = deque("hello")  # Takes and iterable argument
print(d)  # prints deque(["h", "e", "l", "l","o"])

d = deque("hello")  # Takes and iterable argument
d.appendleft(5)  # d is now deque([5, "h", "e", "l","l", "o"])
d.append(4)  # d is now deque([5, "h", "e", "l","l", "o", 4])
print(d)

d.pop()  # would return 4
d.popleft()  # would return 5
print(d)

d.extend([7, 8])
print(d)

# d.extendleft(100)
d.extend(
    [
        100,
    ]
)
print(d)

d.rotate(1)
print(d)  # prints deque(["o", "h", "e", "l", "l"])

d.rotate(-2)

print(d)  # prints deque(["e", "l", "l", "o", "h"])

# Adding max length
max_length = deque("Hello, world!", maxlen=100)
