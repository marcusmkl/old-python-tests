"""
EXCEPTION HANDLING

An exception is an error that happens during execution of a program.
When that error occurs, Python generate an exception that can be handled,
which avoids your program to crash.

Why use Exceptions?
Exceptions are convenient in many ways for handling errors and special conditions in a program.
When you think that you have a code which can produce an error then you can use exception handling.

Below demonstrates what will happen if you implemented no exception handling in your code

Tests:
    Divide by zero: 1 / 0          > throws ZeroDivisionError
    Non-digit numbers: One + 1     > throws ValueError
"""


# best practice: adding type hinting in function signature
# so other programmers can understand what to pass to your functio
def perform_operation(numbers: list, operation: str) -> int:
    first_number = numbers[0].strip()    # remove any whitespace characters such as newline, space, tab
    second_number = numbers[1].strip()
    match operation:
        case '+':
            return int(first_number) + int(second_number)
        case '-':
            return int(first_number) - int(second_number)
        case '*':
            return int(first_number) * int(second_number)
        case '/':
            return int(first_number) / int(second_number)


# below is an example of docstring which explains what the function does
# this is a best practice to aid other programmer to understand your function
# it is enclosed by triple single quotation characters
def parse_input(input_expr: str) -> tuple:
    """
    :param input_expr:
        a string consisting of <operand1><operation><operand2>
        example: 1+1
    :return: tuple
        returns both the parsed_operands (a list) and operator (a str)
        together as a tuple object
    """
    if '+' in input_expr:
        parsed_operands = expression.split('+')
        optr = '+'
    elif '-' in input_expr:
        parsed_operands = expression.split('-')
        optr = '-'
    elif '*' in input_expr:
        parsed_operands = expression.split('*')
        optr = '*'
    elif '/' in input_expr:
        parsed_operands = expression.split('/')
        optr = '/'
    else:
        # manually raise the exception here
        # if operation is invalid
        raise ValueError("Invalid operation")

    return parsed_operands, optr


# execution of the program starts here...
expression = input("Enter your input here:")
operands, operator = parse_input(expression)
answer = perform_operation(operands, operator)
print(f"{expression} = {answer}")

