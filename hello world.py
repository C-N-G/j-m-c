import random

def my_function(input):
  if input > 200:
    print("hello world")
  elif input < 200:
    print("goodbye world")
  else:
    print("you suck")

def MYadd():
  first_numberadsasdasdasd = input("enter a number ")
  second_numberasdasdasdasd = input("enter another number ")
  print(int(first_numberadsasdasdasd) + int(second_numberasdasdasdasd))

def subtract():
  first_number = input("enter a number")
  second_number = input("SECOND NUMBER")
  print(int(first_number) - int(second_number))

def multiply():
  first_number = input("FIRST NAMBER")
  second_number = input("SECOND NAMBER")
  print(int(first_number) * int(second_number))


def divide():
  first_number = input("FIRST NAMBER")
  second_number = input("SECOND NAMBER")
  print(int(first_number) / int(second_number))

def jwajg():
  # = assignment 
  # == equivalent
  # input("TEXT PROMPT")
  # > INPUT SOMETHING
  # input 
  dogsoup = input("asdfasdf")
  if dogsoup == "0":
    MYadd()
  if dogsoup =="1":
    subtract()
  if dogsoup =="3":
    multiply()
  if dogsoup =="2":
    divide()
  
def guess():
  myGuess = input("Guess a number ")
  number = random.randint(0, 10)
  if int(myGuess) == number:
    print("you win")
  else:
    print("you lose")
    print("the number was " + str(number))
  choice = input("would you like to play again? yes/no: ")
  print(" ")
  if choice == "yes":
    guess()

guess()

# jwajg()


myINT = 200 #integers 1 2 3 4 5 -1 -2 -3 -4 -5
myString = "200" #string
myString = '200 a;dslhjfkal;kdsjhflakdjhsflaksdjhflaksjdhflaksdjhflaksjdhfalksdjhflakjsdhf' #string
myString = """200
asdfsgadfsgsdfg
sfdgsdfgsdf
gsfgsdfg
sdfgsgf
sdfgsdfg""" #string

myLong = 200.51234123 #long or double
myBool = True
alsoMyBool = False


# my_function(myINT) # you suck
# my_function(myINT+1) # hello world
# my_function(myINT-1) # goodbye world

# myList = ["apple", "banana", "pear", "orange"]
# mylist = range(10) # [0,1,2,3,4,5,6,7,8,9]

# for number in range(100):
#   print(number*" " + "star")

# for number in range(100, 0, -1):
#   print(number*" " + "star")

int(dog)