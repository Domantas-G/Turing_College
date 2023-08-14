"""
Filter Function
The filter function is similar to the map function. They both make use of a function and and a list. The filter function will pass every element of the given list into a function that returns a Boolean value. If the function returns True for a given element that element will be added to the new returned list. Otherwise it will not.
"""
def isAOne(x):
    return x == 1

nums = [1,1,6,7,8,0,1,1]

newList = list(filter(isAOne,nums))

print(newList)

def add6(x):
  return x+7

def isOdd(x):
  return x%2 != 0

a = [1,2,3,4,5,6,7,8,9,10,11,12]
b = list(filter(isOdd,a))
print(a)
print(b)

c = list(map(add6,b))
# c = list(map(add6,list(filter(isOdd,a))))
print(c)