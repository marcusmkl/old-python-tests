'''
This is where you will write your code.
All class and function definitions must be placed inside the try block
so that the program won't crash if there's something wrong in your code.
Please DO NOT REMOVE OR MODIFY THE EXISTING TRY-CATCH BLOCK HERE
OBSERVE PROPER INDENTATION TO AVOID CRASHING THE PROGRAM
'''


from abc import ABC, abstractmethod

try:
    # place all your class definitions here
    # remove the 'pass' statement before you start coding


    # Coding Challenge #1
    class Calculator(ABC):
        @abstractmethod
        def add(self, operand_1: int, operand_2: int) -> int:
            pass

        @abstractmethod
        def subtract(self, operand_1: int, operand_2: int) -> int:
            pass

        @abstractmethod
        def multiply(self, operand_1: int, operand_2: int) -> int:
            pass

        @abstractmethod
        def divide(self, operand_1: int, operand_2: int) -> float:
            pass

        @property
        @abstractmethod
        def mem(self):
            pass
    

    # Coding Challenge #2

    class ScientificCalculator(Calculator):
        instance_count = 0

        def __init__(self, brand: str):
            self.brand = brand
            self.update_count()

        def add(self, operand_1: int, operand_2: int) -> int:
            return operand_1 + operand_2


        def subtract(self, operand_1: int, operand_2: int) -> int:
            return operand_1 - operand_2


        def multiply(self, operand_1: int, operand_2: int) -> int:
            return operand_1 * operand_2


        def divide(self, operand_1: int, operand_2: int) -> float:
            return operand_1 / operand_2

        @property
        def mem(self):
            pass

        def raise_to_power(self, base: int, power: int) -> int:
            return base ** power

        def add_float(self, num1: float, num2: float) -> float:
            return num1 + num2

        @staticmethod
        def modulo(dividend: int, divisor: int) -> int:
            return dividend % divisor

        @classmethod
        def update_count(cls):
            cls.instance_count += 1


    # Coding Challenge #3
    class ScientificCalculator(Calculator):
        __instance_count = 0

        def __init__(self, brand: str):
            self.__brand = brand
            self.update_count()

        def add(self, operand_1: int, operand_2: int) -> int:
            return operand_1 + operand_2

        def subtract(self, operand_1: int, operand_2: int) -> int:
            return operand_1 - operand_2

        def multiply(self, operand_1: int, operand_2: int) -> int:
            return operand_1 * operand_2


        def divide(self, operand_1: int, operand_2: int) -> float:
            return operand_1 / operand_2

        @property
        def mem(self):
            pass

        def raise_to_power(self, base: int, power: int) -> int:
            return base ** power

        def add_float(self, num1: float, num2: float) -> float:
            return num1 + num2

        @staticmethod
        def modulo(dividend: int, divisor: int) -> int:
            return dividend % divisor

        @classmethod
        def update_count(cls):
            cls.__instance_count += 1

        @classmethod
        def get_instance_count(cls):
            return cls.__instance_count

        @property
        def brand(self):
            return self.__brand

        @brand.setter
        def brand(self, value):
            self.__brand = value


    # Coding Challenge #4
    class Calculator1(ScientificCalculator):
        
        def add(self, operand_1: int, operand_2: int, operand_3: int) -> int:
            return operand_1 + operand_2 + operand_3

    class Calculator2(ScientificCalculator):

        def add(self, operand_1: int, operand_2: int, operand_3: int) -> list:
            return [operand_1, operand_2, operand_3]


    class Calculator3(ScientificCalculator):

        def add(self, operand_1: int, operand_2: int, operand_3: int) -> str:
            return f"{operand_1}{operand_2}{operand_3}"

    calculators = [Calculator1("Brand1"), Calculator2("Brand2"), Calculator3("Brand3")]


except Exception as e:
    print(f"Error in the code! {e}")