import bcrypt
import importlib
import inspect
import getpass
import myclass
import re


total_points = 0
stored_hashed_pw = b'$2b$12$wm69OU3OaunTJBwTDc7yU.jfl/aqIAD0I4r1HVnx642X7qTl60f.2'

def display_greet():
    msg = """
Welcome to your Second Practical Exam
Hit enter when you are ready.
"""
    print(msg)
    input()

def parse_slice_expression(expr):
    match = re.match(r'(\w+)\[([^\]]*)\]', expr)
    if not match:
        raise ValueError(f"Invalid slice expression: {expr}")
    name = match.group(1)
    slice_part = match.group(2)
    parts = slice_part.split(':')
    parts += [None] * (3 - len(parts))  # ensure we have exactly 3 elements
    start, end, step = [eval(p) if p not in (None, '') else None for p in parts]

    return name, start, end, step

def is_valid_open_statement(s):
    pattern = r"""
        ^\s*with\s+                            
        open\s*\(\s*                            
        ['"]myfile\.txt['"]\s*,\s*              
        ['"]([rwa])['"]\s*                     
        \)\s+as\s+                              
        (\w+)?                                  
        \s*:?\s*$                              
    """
    return re.match(pattern, s, re.VERBOSE) is not None

def get_class_methods_including_init(cls):
    methods = []
    for name, member in inspect.getmembers(cls):
        if inspect.isfunction(member) or inspect.ismethod(member):
            if name == '__init__' or not name.startswith('__'):
                methods.append(name)
    return methods

def question1():
    my_string = 'jkdnPsadkOsajfOpoiw'
    print("Q1: Using string slicing, how to slice the string called my_string = 'jkdnPsadkOsajfOpoiw' if you want to get the result 'OOP'?")
    while True:
        answer = input("Answer: ")
        try:
            name, start, end, step = parse_slice_expression(answer)
            if name != 'my_string':
                print("Wrong answer. The name of the string variable is my_string.")
                continue
            if my_string[start:end:step] == 'OOP':
                print("Correct! You got 5 pts and may proceed to the next stage.")
                global total_points
                total_points += 5
                break
            else:
                print("Wrong answer. Please try again.")
        except Exception as e:
            print(f"Wrong answer. {e}")

def question2():
    print("Q2: Using 'with' context manager, how do you read a file called 'myfile.txt'?")
    print("Hint: this is just a one-line code.")
    while True:
        answer = input("Answer: ")
        if is_valid_open_statement(answer):
            print("Correct! You got 5 pts and may proceed to the next stage.")
            global total_points
            total_points += 5
            break
        else:
            print("Incorrect! Try again.")

def question3():
    answer = b'$2b$12$H6sI/buYOkdu25Y1xxqBiOrXFRAtzm7A/VvArtZYBlpSx8v2vsGRK'
    print("Q3: What type of exception does Python raise when you try to access a list index that doesn't exist?")
    print("Hint: The answer is case-sensitive.")
    while True:
        user_ans = input("Answer: ").encode('utf-8')
        if bcrypt.checkpw(user_ans, answer):
            print("Correct! You got 5 pts and may proceed to the next stage.")
            global total_points
            total_points += 5
            break
        else:
            print("Incorrect! Try again.")

def question4():
    answer = b'$2b$12$/2oXmygaLyuGw9bUFpThB./xeAZq8yTMFsaSUyFN2yHI4SLXVE8tC'
    print("Q4: A built-in function in Python that allows you to call a method from a parent class?")
    while True:
        user_ans = input("Answer: ").encode('utf-8')
        if bcrypt.checkpw(user_ans, answer):
            print("Correct! You got 5 pts and may proceed to the final stage.")
            global total_points
            total_points += 5
            break
        else:
            print("Incorrect! Try again.")

def stage1():
    msg = """
Stage 1: Open the myclass.py on your IDE and create an abstract class called Calculator.
This Calculator class has the following abstract methods:
- add(self, operand_1:int, operand_2:int)-> int
- subtract(self, operand_1:int, operand_2:int)-> int
- multiply(self, operand_1:int, operand_2:int)-> int
- divide(self, operand_1:int, operand_2:int)-> float

Plus an abstract property called 'mem'
- def mem(self)

Once done, save the file. 
"""
    print(msg)
    while True:
        input("Press any key and hit Enter to validate your code.")
        try:
            importlib.reload(myclass)
            Calculator = myclass.Calculator
            if inspect.isclass(Calculator) and inspect.isabstract(Calculator):
                abc_methods = sorted(list(Calculator.__abstractmethods__))
                print(abc_methods)
                if abc_methods == ['add', 'divide', 'mem', 'multiply', 'subtract']:
                    print("Correct! You got 20 pts and may proceed to the next stage.")
                    global total_points
                    total_points += 20
                    break
                else:
                    print("Incorrect implementation. There are missing abstract methods and/or abstract property.")
            else:
                print("Wrong! Calculator is not an abstract class.")
        except AttributeError as e:
            print(f"Wrong! No Calculator class found. {e}")

def stage2():
    msg = """
Stage 2: Open the myclass.py on your IDE and add a subclass called ScientificCalculator.
It's parent class must be the Calculator abstract class.
Class Attribute:
    instance_count - an integer that tracks the count of objects made from this class
                   - default value is zero
Instance Attributes:
    brand - a str that represents the brand of your scientific calculator e.g., Casio
It must implement all the abstract methods and the below additional functions:
- raise_to_power(self, base: int, power:int)->int
>> this function raises the base to a certain power e.g., 2^2 = 4

- add_float(self, num1: float, num2: float)->float
>> this function add two floating numbers e.g., 5.4 + 3.1 = 8.5

- modulo(dividend: int, divisor: int )-> int
>> a static method that returns the remainder after dividing the divident to the divisor

- update_count(cls)
>> a classmethod that update the instance_count when a new object is created.
>> call this inside the __init__()

Once done, save the file.
""" 
    print(msg)
    while True:
        input("Hit enter to validate your code.")
        has_error = False
        try:
            importlib.reload(myclass)
            Calculator = myclass.Calculator
            ScientificCalculator = myclass.ScientificCalculator

            if inspect.isclass(ScientificCalculator) and issubclass(ScientificCalculator, Calculator):
                methods = get_class_methods_including_init(ScientificCalculator)
                print(methods)
                if methods != ['__init__', 'add', 'add_float', 'divide', 'modulo', 'multiply', 'raise_to_power', 'subtract', 'update_count']:
                    has_error = True
                    print(f"Some required functions are missing. {methods}")
                
                class_methods = [name for name, attr in ScientificCalculator.__dict__.items() if isinstance(attr, classmethod)]
                if class_methods != ['update_count']:
                    has_error = True
                    print("update_count is not a class method.")
                
                static_methods = [name for name, attr in ScientificCalculator.__dict__.items() if isinstance(attr, staticmethod)]
                if static_methods != ['modulo']:
                    has_error = True
                    print("modulo is not a static method.")

                my_calc = ScientificCalculator('Casio')
                if ScientificCalculator.instance_count != 1:
                    has_error = True
                    print("The class method update_count was not called within the constructor or incorrectly implemented.")
            else:
                has_error = True
                print(f"Wrong. Either ScientificCalculator is not a valid class or not a subclass of Calculator.")
        except AttributeError as e:
            has_error = True
            print(f"Wrong! No ScientificCalculator class found. {e}")
        except TypeError as te:
            has_error = True
            print(f"Wrong! Incorrect implementation of Scientific Calculator class. Here's the actual error: {te}")
        
        if not has_error:
            print("Correct! You got 20 pts and may proceed to the next stage.")
            global total_points
            total_points += 20
            break

def stage3():
    msg = """
Stage 3: Open the myclass.py on your IDE and encapsulate the attributes of ScientificCalculator class.
Class Attribute:
    instance_count - an integer that tracks the count of objects made from this class
                   - default value is zero
Instance Attributes:
    brand - a str that represents the brand of your scientific calculator e.g., Casio

Make the attributes private
For instance attribute, create a getter and setter functions using @property decorator
For class attribute, modify the class method update_count and add a new
classmethod called get_instance_count(cls) where it returns the instance_count value.

Once done, save the file.
"""
    print(msg)
    while True:
        input("Hit enter to validate your code.")
        has_error = False
        try:
            importlib.reload(myclass)
            ScientificCalculator = myclass.ScientificCalculator

            if inspect.isclass(ScientificCalculator):
                methods = get_class_methods_including_init(ScientificCalculator)
                print(methods)
                if methods != ['__init__', 'add', 'add_float', 'divide', 'get_instance_count', 'modulo', 'multiply', 'raise_to_power', 'subtract', 'update_count']:
                    has_error = True
                    print(f"Some required functions are missing. {methods}")
                
                class_methods = sorted([name for name, attr in ScientificCalculator.__dict__.items() if isinstance(attr, classmethod)])
                if class_methods != ['get_instance_count', 'update_count']:
                    has_error = True
                    print("get_instance_count is not a class method.")
                
                prop = getattr(ScientificCalculator, 'brand', None)
                if not isinstance(prop, property):
                    has_error = True
                    print("The brand attribute has no getter and setter functions.")

                try:
                    my_calc = ScientificCalculator('casio')
                    my_calc.brand 
                except NameError as e:
                    print("Setter and Getter functions are incorrectly set up.")
            else:
                has_error = True
                print(f"Wrong. Either ScientificCalculator is not a valid class or not a subclass of Calculator.")
        except AttributeError as e:
            has_error = True
            print(f"Wrong! Here's the actual error: {e}")
        
        if not has_error:
            print("Correct! You got 20 pts and may proceed to the next stage.")
            global total_points
            total_points += 20
            break

def stage4():
    msg = """
Stage 3: Open the myclass.py on your IDE and create three subclasses of ScientificCalculator.
Each subclass overrides the inherited add function as follows:
Calculator1 - its add function accepts three integer inputs and return the sum. e.g., 1 + 2 + 3 = 6
Calculator2 - its add function accepts three integer inputs and return a list. e.g., [1, 2, 3]
Calculator3 - its add function accepts three integer inputs and return the concatenated form. e.g., '4' + '1' + '3' = '413' 

Instantiate the three subclasses and add them to a list called 'calculators'.

Once done, save the file.
"""
    print(msg)
    while True:
        input("Hit enter to validate your code.")
        has_error = False
        try:
            importlib.reload(myclass)
            ScientificCalculator = myclass.ScientificCalculator
            Calculator1 = myclass.Calculator1
            Calculator2 = myclass.Calculator2
            Calculator3 = myclass.Calculator3

            if (
                inspect.isclass(Calculator1) and issubclass(Calculator1, ScientificCalculator)
                and inspect.isclass(Calculator2) and issubclass(Calculator2, ScientificCalculator)
                and inspect.isclass(Calculator3) and issubclass(Calculator3, ScientificCalculator)
            ):
                try:
                    objects = myclass.calculators
                    if isinstance(objects, list):
                        if objects and len(objects) == 3:
                            expected_answers = [6, [1, 2, 3], '123']
                            for obj in objects:
                                if isinstance(obj, Calculator1) or isinstance(obj, Calculator2) or isinstance(obj, Calculator3):
                                    result = obj.add(1, 2, 3)
                                    if result not in expected_answers:
                                        has_error = True
                                        print("Incorrect implementation of overriding add function.")
                                        break
                                    else:
                                        expected_answers.remove(result)
                                else:
                                    has_error = True
                                    print("Wrong! One or more passed objects are not instances of any of the Calculator subclasses.")
                                    break
                        else:
                            has_error = True
                            print("The calculator list must contain three calculator objects.")
                    else:
                        has_error = True
                        print("The calculator object is not a list.")
                except AttributeError as e:
                    has_error = True
                    print("Wrong! You did not create a list of calculator objects called 'calculators'")
            else:
                has_error = True
                print(f"Wrong. One or more Calculator are not valid classes or not subclasses of ScientificCalculator.")
        except AttributeError as e:
            has_error = True
            print(f"Wrong! {e}")
        except Exception as ex:
            has_error = True
            print(f"Your implementation of Calculator subclasses is not complete. : {ex}")
        
        if not has_error:
            print("Correct! You got 20 pts!.")
            global total_points
            total_points += 20
            break

def check_pwd():
    while True:
        user_pwd = getpass.getpass("Ask the proctor to enter the password:").encode('utf-8')
        if bcrypt.checkpw(user_pwd, stored_hashed_pw):
            display_greet()
            break
        else:
            print("Incorrect password. Try again.")

def main():
    check_pwd()
    print(f"Your total points: {total_points}")
    print("========= Knowledge Checkpoint #1 =========")
    question1()
    print(f"Your total points: {total_points}")
    input("Hit enter when you're ready.")
    print("========= Coding Challenge #1 =========")
    stage1()
    print(f"Your total points: {total_points}")
    input("Hit enter when you're ready.")
    print("========= Knowledge Chekpoint #2 =========")
    question2()
    print(f"Your total points: {total_points}")
    input("Hit enter when you're ready.")
    print("========= Coding Challenge #2 =========")
    stage2()
    print(f"Your total points: {total_points}")
    input("Hit enter when you're ready.")
    print("========= Knowledge Chekpoint #3 =========")
    question3()
    print(f"Your total points: {total_points}")
    input("Hit enter when you're ready.")
    print("========= Coding Challenge #3 =========")
    stage3()
    print(f"Your total points: {total_points}")
    input("Hit enter when you're ready.")
    print("========= Knowledge Checkpoint #4 =========")
    question4()
    print(f"Your total points: {total_points}")
    input("Hit enter when you're ready.")
    print("========= Coding Challenge #4 =========")
    stage4()
    print("Congratulations! You just have finished the exam!")
    print(f"Your total points: {total_points}")
    print("========= End of Exam =========")
    print("\nPresent this to the proctor before exiting.")

if __name__ == '__main__':
    main()