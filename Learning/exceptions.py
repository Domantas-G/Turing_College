"""
Exceptions are things that go wrong within our coding.try
In Python try and except are ways of testing out user input before something goes wrong. Modify your code as follows:
"""
while True:
    try:
        x = int(input("What's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
