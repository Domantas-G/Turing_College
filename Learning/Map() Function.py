"""
Map Function
The map function can be used to apply a function to every element in a given list. For example, if we wanted to apply a function f1 to a list of numbers we would usually do something like this:
"""
def f1(x):
    return x + x/2

nums = [1,5,6,7,2]

newList = []
for item in nums:
    numList.append(f1(nums))

"""However the map function can eleminate a lot of this work and perform this same task in one line."""

def f1(x):
    return x + x/2

nums = [1,5,6,7,2]

newList = list(map(f1, nums))

# Example
li = [1,2,3,4,5]
def func(x):
  return x**x

print(list(map(func, li)
# Alternative with List comprehension
print([func(x) for x in li if x%2==0])