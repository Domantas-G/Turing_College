"""Similar to if, elif, and else statements, match statements can be used to conditionally run code that matches certain values.
Consider the following program:"""
name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

"""A match statement compares the value following the match keyword with each of the values following the case keywords. In the event a match is found, the respective indented code section is executed and the program stops the matching."""
name = "Ron"

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

if name in ["Harry", "Hermione", "Ron"]:
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
