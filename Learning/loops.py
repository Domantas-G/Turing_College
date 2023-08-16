"""Essentially, loops are a way to do something over and over again"""

"""While loop
Such a loop will repeat a block of code over and over again.
"""
i = 0
while i < 3:
    print("meow")
    i += 1


"""For Loops
To best understand a for loop, it’s best to begin by talking about a new variable type called a list in Python. As in other areas of our lives, we can have a grocery list, a to-do list, etc.
A for loop iterates through a list of items. For example, in the text editor window, modify your cat.py code as follows:
"""
# for i in [0, 1, 2]:
for i in range(3):
    print("meow")

n = 5
while True:
    n = int(input("What's n? "))
    if n < 0:
        break


def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")


main()

"""More About Lists"""
students = ["Hermoine", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])

for student in students:
    print(student)

for i in range(len(students)):
    print(i + 1, students[i])

"""Dictionaries"""
students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")

students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
