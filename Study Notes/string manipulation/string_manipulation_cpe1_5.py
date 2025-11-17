msg = "HELLO WORLD"
print("This is a string: " + msg)

# much like python list, elements of a string can be accessed via indexing
""" index positions
 0   1   2  3  4  5  6  7  8  9  10
 H   E   L  L  O     W  O  R  L  D
-11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
"""
print(f"This is an example of string indexing: {msg[4]}")
print(f"This is an example of string negative indexing: {msg[-3]}")

# This is an example of accessing the last element safely by checking the length of the string
print(f"Last element of the string msg: {msg[len(msg) - 1]}")

"""
STRING SLICING - a technique to extract substrings from a string
use this notation str[start:end:step]
start: specifies the starting index; default value is index 0
end: specifies the last index (non-inclusive); default value is the len of the string
step: specifies how much character to skip; default value is 1
if a negative number is provided for step, it will reverse the direction of the step
"""
""" index positions
 0   1   2  3  4  5  6  7  8  9  10
 H   E   L  L  O     W  O  R  L  D
-11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
"""
print(f"This is a sample of string slicing: {msg[0:5:]}")
print(f"This is a sample of string slicing: {msg[0:11:2]}")
print(f"This is a sample of string slicing: {msg[::2]}")
print(f"This is a sample of string slicing: {msg[-5::]}")
print(f"This is a sample of string slicing: {msg[::-1]}")

# use case of string slicing with negative indexing
# let's say we want to extract the file extension (e.g., .txt, .exe, .xlsx)
myfile = "my.file.is.good.txt"
index = myfile.rfind('.')
print(myfile[index::])

"""
STRING IMMUTABILITY
Strings in Python are immutable, meaning once a string is created, its content cannot be changed.
"""
a = "Hello"   # original string
print(id(a))  # original memory location
b = a.upper() # HELLO
print(a)      # the original string was not modified
a = a.upper() # re-assigning a to store the result of the upper function
print(a)      # now 'a' is modified
print(id(a))  # but has different memory location
              # it didn't modified the string from the old memory location of 'a'


"""
STRING CONCATENATION
Two or more strings can be combined using the + operator
It will throw an error though if combining string with other data types
"""
greet = "My age is "
age = 23

print(greet + str(age))     # since age is int data type, need to convert to str before concatenation




"""
STRING FORMATTING
refers to the process of embedding or inserting values into a string, 
allowing you to create strings dynamically. 
This is useful when you want to build a string with variables or expressions.

two methods:
1. f-string (only available from Python version 3.9 and up)
2. str.format()
"""
# using f-string
name = "Kim Jong Eun"
age = 100
dogs = ['shih-tzu', 'bulldog', 'chihuahua']
greet = f"Hi, my name is {name}, I am {age} years old. My dogs are {', '.join(dogs)}."
print(greet)

# using str.format()
introduction = "Hi, my name is {0}, I am {1} years old. My dogs are {2}."
print(introduction.format(name, age, ', '.join(dogs)))



# coding challenge - looking for the dot character (.) between characters 's' and 'g'
myfile = "my.file.is.good.txt"
key = "."

# function to determine index position of next and previous elements
# handles out of bounds cases such as when index = 0 or index = last element index
def resolve_indices(index)->tuple:
    if index == 0:
        next_idx = index + 1
        prev_idx = index
    elif index == len(myfile) - 1:
        next_idx = index
        prev_idx = index - 1
    else:
        next_idx = index + 1
        prev_idx = index -1

    return next_idx, prev_idx

for index, char in enumerate(myfile):
    next, previous = resolve_indices(index)
    if char == key and myfile[previous] == 's' and myfile[next] == 'g':
        print(f"The index location is {index}")
        break