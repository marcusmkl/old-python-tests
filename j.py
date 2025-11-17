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
    class Calculator(ABC):

        # Coding Challenge #1
        @abstractmethod
        def add(self, operand_1:int, operand_2:int) -> int:
            pass

        # Coding Challenge #2
        @abstractmethod
        def subtract(self, operand_1:int, operand_2:int) -> int:
            pass

        # Coding Challenge #3
        @abstractmethod
        def multiply(self, operand_1:int, operand_2:int) -> int:
            pass

        # Coding Challenge #4
        @abstractmethod
        def divide(self, operand_1:int, operand_2:int) -> int:
            pass
        
        @abstractmethod
        def mem(self):
            pass

    class ScientificCalculator(Calculator):
        instance_count = 0

        def __init__(self, brand: str):
            self._mem = 0
            self.brand = brand
            self.__class__.update_count()

        def add(self, operand_1: int, operand_2: int) -> int:
            self._mem = operand_1 + operand_2
            return self._mem

        def subtract(self, operand_1: int, operand_2: int) -> int:
            self._mem = operand_1 - operand_2
            return self._mem

        def multiply(self, operand_1: int, operand_2: int) -> int:
            self._mem = operand_1 * operand_2
            return self._mem

        def divide(self, operand_1: int, operand_2: int) -> float:
            if operand_2 == 0:
                raise ValueError("Cannot divide by zero.")
            self._mem = operand_1 / operand_2
            return self._mem

        @property
        def mem(self):
            return self._mem

        def raise_to_power(self, base: int, power: int) -> int:
            result = base ** power
            self._mem = result
            return result

        def add_float(self, num1: float, num2: float) -> float:
            result = num1 + num2
            self._mem = result
            return result

        @staticmethod
        def modulo(dividend: int, divisor: int) -> int:
            if divisor == 0:
                raise ValueError("Cannot modulo by zero.")
            return dividend % divisor

        @classmethod
        def update_count(cls):
            cls.instance_count += 1

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
            self._mem = operand_1 + operand_2 + operand_3
            return self._mem

    class Calculator2(ScientificCalculator):
        def add(self, operand_1: int, operand_2: int, operand_3: int) -> list:
            result = [operand_1, operand_2, operand_3]
            self._mem = sum(result)
            return result

    class Calculator3(ScientificCalculator):
        def add(self, operand_1: int, operand_2: int, operand_3: int) -> str:
            result = f"{operand_1}{operand_2}{operand_3}"
            self._mem = int(result)
            return result

    calculators = [Calculator1("A"), Calculator2("B"), Calculator3("C")]

except SyntaxError:
    pass
