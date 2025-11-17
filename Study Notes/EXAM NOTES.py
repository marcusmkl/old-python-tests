
# ==================================================
#               String Manipulation
# ==================================================

'''

String manipulation in Python allows you to process and modify strings using various 
methods like slicing, searching, replacing, and formatting.

Strings in Python are arrays of bytes representing Unicode characters. 

Strings are immutable. This means that elements of a string cannot be changed once it 
has been assigned. We can simply reassign different strings to the same name.

s = "Hello, Python!"

# Basic string operations

print(s.lower())        # hello, python!
print(s.upper())        # HELLO, PYTHON!
print(s.strip("!"))     # Hello, Python
print(s.replace("Python", "World"))  # Hello, World! - first argument is the word to replace, second is the new word
print(s.split(", "))   # ['Hello', 'Python!']
print(s.find("Python"))  # 7
print(s.capitalize) # Hello, Python!
print(s.title)  # Hello, Python!
print(s.find("Python"))  # 7
print(s.replace("Python", "World"))  # Hello, World!
print(s.join(["Hello", "World"]))  # Hello World
print(s.split(", "))   # ['Hello', 'Python!']
print(s.swapcase())  # hELLO, pYTHON!
print(s.count("o"))  # 2 - counts occurrences of 'o'
print(s.find("Python"))  # 7 - finds the index of 'Python'
print(s.index("Python"))  # 7 - finds the index of 'Python', raises ValueError if not found
print(s.startswith("Hello"))  # True - checks if string starts with 'Hello'
print(s.endswith("!"))  # True - checks if string ends with '!'
print(s.isdigit())  # False - checks if string contains only digits


name = "Seo Nari"

print(name.ljust(12, "a")) # left justify with padding - adds 'a' to the right until length is 12
print(name.rjust(12, "a")) # right justify with padding - adds 'a' to the left until length is 12
print(name.center(12, "a")) # center justify with padding - adds 'a' to both sides until length is 12


# String slicing - first argument is the start index, second is the end index, and third is the step
s = "Hello, Python"
print(s[0:5])           # Hello
print(s[::-3])          # !nohtyP ,olleH

# String formatting

# name = "seyonari"
# age = 19
# print(f"My name is {name} and I am {age} years old.")


# name = "Seo Nari"
# vowels = "aeiouAEIOU"
# symbol = "@!#"

# for vowel in vowels:
#     name = name.replace(vowel, symbol)

# print(name)

'''
# names = ["marcus", "jana", "erin", "mikel"]


# name = "marcus"

# for letters in name:
#     print(letters in name)


# ==================================================
#                  File Handling
# ==================================================

'''
File handling 
    - used to read and write data to files. Python provides built-in functions like open(), read(), write(), and close().

File
    - named location on disk to store related information. It is used to permanently store data in a non-volatile memory (e.g., hard disk).

Text files
    - used to store characters or strings.  

Binary files 
    - can be used to store text, images, audio and video.  

Image files
    - generally available in .jpg, .gif or .png formats

r = read (default mode, opens file for reading)
w = write (overwrites the file if it exists, creates a new file if it does not exist)
a = append (opens file for appending, creates a new file if it does not exist)

r+ = read and write (does not overwrite the file, but allows reading and writing)  
w+ = write and read (overwrites the file if it exists) 
a+ = read and append

# Writing to a file

with open("sample.txt", "w") as f:
    f.write("Hello, File Handling!\n")
    f.write("This is Python.")

# Reading from a file

with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

# Appending to a file

with open("sample.txt", "a") as f:
    f.write("\nAppending new line.")



# =================== Example of file handling with reading, writing, and appending
    

# instantiate a file object
my_file = "anime_girls.txt"

# Write initial entries (overwrite if file exists)
with open(my_file, "w") as file:
    file.write("1. Seo Nari\n")
    file.write("2. Yi Xuan\n")
    file.write("3. Miyabi\n")

# Read and print file content
with open(my_file, "r") as file:
    content = file.read()
    print("Initial content:\n", content)
    
# Append to the end of the file
with open(my_file, "a") as file:
    file.write("4. Zhu Yuan\n")
    file.write("5. Evelynn\n")

# Read and print updated content
with open(my_file, "r") as file:
    content = file.read()
    print("Updated content:\n", content)

# Replace "Seo Nari" with "Yanagi"
with open(my_file, "r") as file:
    lines = file.readlines()

# Replace the name 
updated_lines = []
for line in lines:
    updated_lines.append(line.replace("Seo Nari", "Yanagi"))

# Write updated content back to file
with open(my_file, "w") as file:
    file.writelines(updated_lines)

# Print final content
with open(my_file, "r") as file:
    content = file.read()
    print("Final content after replacement:\n", content)

'''

# file = "imtired.txt"

# with open("imtired.txt", "w") as file:
#     file.write("just end me at this point \n")

# file.close()

# with open("imtired.txt", "a") as file:
#     file.write("lmao lmao \n")
#     file.write("man, i just want some reciprocated energy \n")
#     file.write("sadge")

# file.close


# ==================================================
#               Exception Handling
# ==================================================


'''

Exception handling allows you to manage errors gracefully in your program using try-except blocks.

Exception
    - an error that happens during execution of a program
    - When that error occurs, Python generates an exception that can be handled, which avoids your program to crash

Try
    - used to test a block of code for errors

Except
    - used to handle errors

Finally 
    - used to execute block of code regardless of the result of the try and except block

Raise
    - used to throw an exception if a condition occurs

Types of Exceptions:

Checked(Compile-time) Exceptions
    - These are checked at compile time, such as syntax errors.
    - Subject to the “catch” or “specify requirement”

Unchecked(Runtime) Exceptions
    - These are checked at runtime, such as division by zero or null pointer exceptions.
    - Not subject to the “catch” or “specify requirement”

1. ValueError: Raised when a function receives an argument that has the right type but an inappropriate value.
2. ZeroDivisionError: Raised when a division or modulus operation is performed with zero as the divisor.
3. TypeError: Raised when an operation or function is applied to an object of inappropriate type.
4. IOError: Raised when an I/O operation (like reading or writing a file) fails.
5. ImportError: Raised when an import statement fails to find the module definition.
6. Exception: Raised for any other exception not previously caught.

Some other errors but not included in the discussion:

7. SyntaxError: Raised when the parser encounters a syntax error.
8. IndexError: Raised when a sequence subscript is out of range.
9. NameError: Raised when a local or global name is not found.
10. KeyError: Raised when a dictionary key is not found.
11. AttributeError: Raised when an invalid attribute reference is made.
12. FileNotFoundError: Raised when a file or directory is requested but cannot be found.


# ========================= Example of Exception Handling in a Calculator App



def calculator_app():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = a / b
        else:
            raise ValueError("Invalid operation. Use +, -, *, or /.")

        print(f"Result: {result}")

    except ValueError:
        print("ValueError: Input must be a number or a valid operation.")
    except TypeError:
        print("TypeError: Inputs must be valid.")
    except Exception as e:
        print(f"Unexpected error: {e}")

calculator_app()

'''

# ==================================================
#               Classes and Objects
# ==================================================


'''

Classes
    - user-defined data structure that binds the data members and methods into a single unit.
    - blueprint or code template for object creation
    - defined using the class keyword, followed by the class name and a colon.
    - encapsulate data for the object and methods to manipulate that data.

Objects 
    - instances of classes.
    - collection of attributes (variables) and methods. We use the object of a class to perform actions
    - has the following properties:
        Identity: Every object must be uniquely identified.
        State: An object has an attribute that represents a state of an object, and it also reflects the property of an object.
        Behavior: An object has methods that represent its behavior.


    Instantiation
        - the process of creating an object from a class.
        - done by calling the class as if it were a function, passing any required arguments to the class's __init__ method.
        - also called the instance of a class
    
Class Attributes
    - attributes that are shared by all instances of the class.
    - defined within the class but outside the methods.

    Instance Variables
        - attributes that are unique to each instance of the class.
        - Objects do not share instance attributes. Unique attributes are created for each object.
    Class Variables
        - attributes that are declared inside of a class but outside of any instance method.
        - class variables are shared by all instances of the class.

Class Methods
    - methods that are bound to the class and not the instance.
    - defined using the @classmethod decorator.
    - take the class as the first argument, conventionally named cls.

    Instance Methods
        - methods that are bound to the instance of the class.
        - used to access and modify the instance's attributes.
    Class Methods
        - methods that are bound to the class and not the instance.
        - used to access and modify class attributes.
    Static Methods
        - methods that do not depend on class or instance attributes.
        - general utility method that performs a task in isolation.
        - doesn't have access to the instance or class attributes.

Constructor
    - a special method that is automatically called when an object is created.
    - used to create and initialize the attributes of the class.
    - primary use is to declare the data member / instance variables of the class.
    - divided into object creation and object initialization.
        __new__ method is responsible for creating the object
        __init__ method is responsible for initializing the object.
    
    Types of Constructors:
        - Default Constructor: A constructor that does not take any arguments. Python provides a default constructor if no constructor is defined.
        - Parameterized Constructor: A constructor that takes arguments to initialize the object with specific values.
        - Non-Parameterized Constructor: A constructor that does not take any arguments but initializes the object with default values.
        - Constrcutor with Default Arguments: A constructor that takes arguments with default values, will be used if no arguments are passed during object creation.

Self Keyword in Python
    - refers to the current instance of the class.
    - used to access variables that belong to the class.

# ================================================== Example of Classes and Objects


# Define a class named Student
class Student: 

    # Class variable shared by all instances
    school_name = "ACNSTHS"

    # Constructor method to initialize instance variables
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Class method to display the school name
    @classmethod
    def display_school(cls):
        print(f"School Name: {cls.school_name}")
    
    # Doesn't use instance or class attributes, has its own logic
    @staticmethod
    def greet():
        return "Hello, welcome to the Student class!"

    # Instance method to return student information
    def info(self):
        return f"Name: {self.name}, Age: {self.age}, School: {self.school_name}"
    

# Create instances of the Student class and demonstrate functionality

student_1 = Student("Seo Nari", 18)
print(student_1.info())

student_1.name = "Park Dayoung"
print(student_1.info())

student_2 = Student("Jana Erin", 18)
print(student_2.info())
print(student_2.name)
print(student_2.age)

print(Student.greet())  # Static method call


'''

# ==================================================
#                  Inheritance
# ================================================== 
'''

Inheritance
    - process of inheriting the properties of the parent class into a child class
    - the existing class is called a base class or parent class and the new class is called a subclass or child class or derived class.
    - code reusability 
    - the child class inherits the properties and methods of the parent class.
    - allows us to create a new class based on an existing class, inheriting its attributes and methods.
    - a child class can also override or extend the functionality of the parent class.

Types of Inheritance:
    - Single Inheritance: A child class inherits from a single parent class.
    - Multiple Inheritance: A child class inherits from multiple parent classes.
    - Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another parent class.
    - Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
    - Hybrid Inheritance: A combination of two or more types of inheritance.

Super() Function
    - used to call a method from the parent class.
    - allows you to access methods and properties of the parent class from the child class.
    - can be used to call the constructor of the parent class.
    - We are not required to remember or specify the parent  class name to access its methods.
    - We can use the super()function in both single and multiple inheritances.
    - The super() function support code reusability as there is no need to write the entire function

Method Overriding
    - allows a child class to provide a specific implementation of a method that is already defined in its parent class.
    - The child class method overrides the parent class method.
    - It is used to change or extend the behavior of the parent class method in the child class.
    - The overridden method in the child class must have the same name, parameters, and return type as the method in the parent class.

# ================================================== Example of Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def details(self):
        return f"My name is {self.name}. I am {self.age} and I study {self.course}"

    def speak(self):
        return f"I want to get out of this class already."

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def details(self):
        return f"My name is {self.name}. I am {self.age} and I teach {self.subject}"
    
class Employee(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job

    def details(self):
        return f"My name is {self.name}. I am {self.age} and I work as a {self.job}"
    
class Father(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

    def details(self):
        return f"My name is {self.name}. I am {self.age}. I am a {self.role}."
    
    @staticmethod
    def hobbies():
        return "Now that I am retired, I usually spend my time watching TV shows and playing golf."


student_1 = Student("Seyonari", 19, "Computer Engineering")
print(student_1.details())
print(student_1.speak())

teacher_1 = Teacher("Park Dayoung", 30, "Object Oriented Programming")
print(teacher_1.details())

employee_1 = Employee("Pan Yinhu", 25, "Software Engineer")
print(employee_1.details())

father_1 = Father("Lee Nari", 50, "father")
print(father_1.details())
print(father_1.hobbies())



'''

# ==================================================
#                  Abstraction
# ================================================== 

'''

Abstraction
    - representing essential features without bg details or explanations
    - hiding the workstyle of an object and only show info of an obj in understandable manner

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

d = Dog()
d.make_sound()

'''

# ==================================================
#                  Encapsulation
# ================================================== 

'''

Encapsulation 
    - wrapping up of data and functions into a single unit 
    - insulation of data from direct access is called data hiding or info hiding
    - process of enclosing one or more details from outside world through access right
    - restrict access to methods and variables from outside of class. 

Public Member
    self.name --> accessible within or outside of class
Protected Member
    self._name --> accessible within the class and its sub classes
Private Member
    self.__name --> accessible only within a class

    

We can acess private data members through:
    1. Name Mangling 
        - directly access private and protected member by using _classname_dataMember
    2. Getters and Setters
        - implement proper encapsulation

    The getters and setters methods are often used when:
        - avoid direct access to private variables
        - add validation logic for setting a value

        @property - getter 
        @xyz.setter - setter


class Student:
    def __init__(self, name, age):
        self.__name = name  # private attribute - denoted by double underscore (cannot be accessed outside the class)
        self._age = age    # protected attribute - denoted by single underscore (can be accessed in subclasses)

    @property # getter method
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name  # setter method to modify the private attribute

    def details(self):
        return f"Name: {self.__name}, Age: {self._age}"

student_1 = Student("Seo Nari", 20)
print(student_1.details())  # Name: Seo Nari, Age: 20
print(student_1.name)  # Name: Seo Nari

student_1.name = "Kim Nari"  # using setter to change the name
print(student_1.details())  # Name: Kim Nari, Age: 20
print(student_1.name)  # Name: Kim Nari
print(student_1.__name)  # Raises AttributeError: 'Student' object has no attribute '__name'

'''


# ==================================================
#                  Polymorphism
# ================================================== 


'''

Polymorphism 
    - ability of an object to take on many forms.
    - allows us to perform the same action in different ways.
    - len function is an example of polymorphism.
        - used to find the length of different data types like strings, lists, and tuples.
    - can be achieved through method overriding and method overloading.
    - Python first checks the object's class type and executes the appropriate method when we call the method

Polymorphism with Inheritance

    Method Overriding
        - process of re-implementing the inherited method in the child class 
        - allows us to defines methods in the child class that have the same name as the methods in the parent class
        - effective when we want to extend the functionality by altering the inherited method
        - useful when a parent class has multiple child classes, and one of them wants to redefine the method

    Method Overloading
        - the process of calling the same method with different parameters
        - python doesnt support this


class Vehicle:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def details(self):
        return f"Details: {self.name}, {self.color}, {self.price}"
    
    def max_speed(self):
        print("150 kph")
    
    def change_gear(self):
        print("Change to gear 4")

class Car(Vehicle):
    
    def __init__(self, name, color, price):
        super().__init__(name, color, price)  
    
    def max_speed(self):
        print("100 kph")
    
    def change_gear(self):
        print("Change to gear 3")


car_1 = Car("Sedan", "Red", "3 million")
print(car_1.details())      #
car_1.max_speed()           
car_1.change_gear()         

vehicle_1 = Vehicle("Truck", "Gray", "500k")
print(vehicle_1.details())
vehicle_1.max_speed()
vehicle_1.change_gear()


'''


