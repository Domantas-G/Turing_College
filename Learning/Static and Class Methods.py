"""Static Methods
Static methods are methods within a class that have no access to anything else in the class (no self keyword or cls keyword). They cannot change or look at any object attributes or call other methods within the class. They can be thought of as a special kind of function that sits inside of the class. When we create a static method we must use something called a decorator. The decorator for a static method is "@staticmethod".
"""
class myClass:
    def __init__(self):
        self.x = x

    @staticmethod
    def staticMethod():  
        return "i am a static method"

"""Class Methods
Class methods are methods within a class that only have access to class variables and other class methods. They are passed the name of the class and therefore can access anything within the class. Like static methods they cannot access any instance attributes. You can create a class method by using the "@classmethod" decorator.
"""
class myClass:
    count = 0

    def __init__(self):
        self.x = x

    @classmethod
    def classMethod(cls):  
        cls.count += 1



class person(object):
  # Class variables
  population = 50
  
  def __init__(self, name, age):
    self.name = name
    self.age = age

    # Class Method
  @classmethod
  def getPopulation(cls):
    return cls.population
  
   # Static method
  @staticmethod
  def isAdult(age):
    return age >= 18
  
  def display(self):
    print(self.name, "is", self.age, "years old")
    
newPerson = person('tim', 18)

print(person.getPopulation())
print(person.isAdult(21))