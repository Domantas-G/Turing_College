# FOr removing Function place dependency and executing the whole code with a single function. 
def main ():
  × = int (input ("What's x? ")) 
  if is even(x):
    print("Even")
  else:
    print ("Odd")

def is even(n):
  return n % 2 == 0

main()


# We do not need to define True or False outcomes if it can be determined in the function.
# program will evaluate what is happening within the n % 2 == 0 as either true or false and simply return that to the main function.
def is_even(n):
    return n % 2 == 0

# To call the program only when it's main file being executed:
def main():
  pass

if __name__ == '__main__':
  main()
  
# List Comprehensions as a replacement for Map and Filter functions.
list(map(factorial, range(6)))
# [1, 1, 2, 6, 24, 120]

[factorial(n) for n in range(6)]
# [1, 1, 2, 6, 24, 120]

list(map(factorial, filter(lambda n: n % 2, range(6))))
# [1, 6, 120]

[factorial(n) for n in range(6) if n % 2]
# [1, 6, 120]

# Lambda example: to sort by Reverse
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
sorted(fruits, key=lambda word: word[::-1])
# ['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']

# Generators
def infinite_numbers():
    num = 1
    while True:
        yield num
        num += 1

# Using the infinite generator
counter = 0
for num in infinite_numbers():
    print(num)
    counter += 1
    if counter >= 5:
        break

# Generator Expressions:
even_squares = (x ** 2 for x in range(10) if x % 2 == 0)

for square in even_squares:
    print(square)

# List vs Generator: Using a list to store all values
def create_list():
    result = []
    for i in range(1000000):
        result.append(i)
    return result

# Using a generator
def create_generator():
    for i in range(1000000):
        yield i

# Compare memory usage
import sys
list_data = create_list()
generator_data = create_generator()
print(sys.getsizeof(list_data))
print(sys.getsizeof(generator_data))

# Parsing value into 2 different types based on outcome:
from typing import Union

def parse_token(token: str) -> Union[str, float]:
    try:
        return float(token)
    except ValueError:
        return token

# Dataclass example
from dataclasses import dataclass, field

@dataclass
class ClubMember:
    name: str
    guests: list[str] = field(default_factory=list)
    athlete: bool = field(default=False, repr=False)
    all_handles = set()
    handle: str = ''
    
    def __post_init__(self):
        cls = self.__class__
        if self.handle == '':
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            msg = f'handle {self.handle!r} already exists.'
            raise ValueError(msg)
        cls.all_handles.add(self.handle)

@dataclass
class C:
    i: int
    j: int = None
    database: InitVar[DatabaseType] = None

    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = database.lookup('j')

c = C(10, database=my_database)


from dataclasses import dataclass, field
from typing import Optional
from enum import Enum, auto
from datetime import date


class ResourceType(Enum):  1
    BOOK = auto()
    EBOOK = auto()
    VIDEO = auto()


@dataclass
class Resource:
    """Media resource description."""
    identifier: str
    title: str = '<untitled>'
    creators: list[str] = field(default_factory=list)
    date: Optional[date] = None
    type: ResourceType = ResourceType.BOOK
    description: str = ''
    language: str = ''
    subjects: list[str] = field(default_factory=list)

    def __repr__(self):
        cls = self.__class__
        cls_name = cls.__name__
        indent = ' ' * 4
        res = [f'{cls_name}(']
        for f in fields(cls):
            value = getattr(self, f.name)
            res.append(f'{indent}{f.name} = {value!r},')

        res.append(')')
        return '\n'.join(res)

description = 'Improving the design of existing code'
book = Resource('978-0-13-475759-9', 'Refactoring, 2nd Edition',
      ['Martin Fowler', 'Kent Beck'], date(2018, 11, 19),
      ResourceType.BOOK, description, 'EN',
      ['computer programming', 'OOP'])
book  # doctest: +NORMALIZE_WHITESPACE
Resource(identifier='978-0-13-475759-9', title='Refactoring, 2nd Edition',
    creators=['Martin Fowler', 'Kent Beck'], date=datetime.date(2018, 11, 19),
    type=<ResourceType.BOOK: 1>, description='Improving the design of existing code',
    language='EN', subjects=['computer programming', 'OOP'])

# Matching
def match_asian_cities():
    results = []
    for city in cities:
        match city:
            case City(continent='Asia'):
                results.append(city)
    return results

# Assertion
from collections.abc import Iterator
from typing import TYPE_CHECKING

import pytest

from top import top

# several lines omitted

def test_top_tuples() -> None:
    fruit = 'mango pear apple kiwi banana'.split()
    series: Iterator[tuple[int, str]] = (
        (len(s), s) for s in fruit)
    length = 3
    expected = [(6, 'banana'), (5, 'mango'), (5, 'apple')]
    result = top(series, length)
    if TYPE_CHECKING:
        reveal_type(series)
        reveal_type(expected)
        reveal_type(result)
    assert result == expected

# Finding Index for max values
df['Sodium'].idxmax() #to obtain index where Max value appears
for col in df.columns
	print(df [' col' ].idxmax() )
 
 df.at[82, 'Item']
 
 import pandas as pd

def split_series_column(dataframe, series_column_name, separator):
    # Split the specified series column on the separator
    split_series = dataframe[series_column_name].str.split(separator, expand=True)
    
    # Rename the columns
    split_series.columns = [series_column_name, series_column_name + "_nr"]
    
    # Drop the original series column and update the DataFrame
    dataframe = dataframe.drop(columns=[series_column_name])
    dataframe = pd.concat([dataframe, split_series], axis=1)
    
    return dataframe

# Call the function to split the 'series' column
df = split_series_column(df, 'series', '#')

# Print the modified DataFrame
print(df)

# Split the 'series' column on '#'
split_series = df['series'].str.split('#', expand=True)

# Rename the columns
split_series.columns = ['series', 'series_nr']

# Update the original DataFrame with the split columns
df['series'] = split_series['series']
df['series_nr'] = split_series['series_nr']

# Print the modified DataFrame
print(df)

pandas.DataFrame.convert_dtypes
pandas.DataFrame.astype
pandas.to_datetime

# median for Continuous and Mode for ordinal

# Save data before Normalization
df.memory_usage(deep=True) / (1024 * 1024)  # Convert bytes to MB
# Before NORMALIZATION
df['description'] = df['description'].str[:5] # Only for the description to be saved
df['coverImg'] = df['coverImg'].str[:5] # Only for the description to be saved
file_path = "/Volumes/Workspace/Turing_College/1.3_project/before_normalization.csv"
df.to_csv(file_path, index=False)

"""Import and load the data into a dataframe."""
# data = pd.read_csv("cleaned_best_books_ever.csv")
data = pd.read_csv("before_normalization.csv")
df = pd.DataFrame(data)