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