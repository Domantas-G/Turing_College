"""Lambda Functions
In python lambda stands for an anonymous function. It is used for creating small functions that are typically only used a few times. A lambda function can only perform one lines worth of operations on a given input. To declare a lambda function is similar to creating a variable.
"""
# def func(x): 
#   return x+5
func = lambda x: x+5

print(func(2))
# Prints 7
"""The parameter(s) for a lambda function comes before the colon (in our case x) and what will be returned comes after (x+5). We can use our lambda function the same as a regular function.

Lambda functions can also use multiple parameters.
"""
func = lambda x, y: x+y

print(func(2,2))
# Prints 4
"""Lambda with Map() & Filter()
The most common place to use a lambda function is within the map or filter functions."""

myList = [1,4,6,7,8,11,3,4,6]

newList = list(filter(lambda x: return x > 5, myList))
# newList is [6,7,8,11,6]

newList2 = list(map(lambda x: x+1, myList))
# newList 2 is [2,5,7,8,9,12,4,5,7]
