"""
EXCEPTION HANDLING

An exception is an error that happens during execution of a program.
When that error occurs, Python generate an exception that can be handled,
which avoids your program to crash.

Why use Exceptions?
Exceptions are convenient in many ways for handling errors and special conditions in a program.
When you think that you have a code which can produce an error then you can use exception handling.

Below demonstrates what will happen if you implemented exception handling in your code

Tests:
    Divide by zero: 1 / 0          > throws ZeroDivisionError
    Non-digit numbers: One + 1     > throws ValueError
    Invalid operation: 1 % 2       > else block changed to manually raising an exception
"""


# best practice: adding type hinting in function signature
# so other programmers can understand what to pass to your function
def perform_operation(numbers: list, operation: str):
    first_number = numbers[0].strip()
    second_number = numbers[1].strip()
    result = None
    # since the ValueError exception might occur from all int() executions,
    # we insert the whole match (case statements) in the try block.
    try:
        match operation:
            case '+':
                result = int(first_number) + int(second_number)
            case '-':
                result = int(first_number) - int(second_number)
            case '*':
                result = int(first_number) * int(second_number)
            case '/':
                result = int(first_number) / int(second_number)
        # end of try block
    except ValueError:
        print("ValueError encountered within the function")
        raise ValueError("One of the operands is invalid. Please use digits 0-9 only. Returning None result.")

    # combining the initial try-except block for ZeroDivisionError here
    # for a cleaner look code
    except ZeroDivisionError:
        result = "Undefined"

    # and you can add as many as except blocks here
    # the more specific exceptions, the better
        '''
        except NameError as e:
            print(e)
        except TypeError as e:
            print(e)
        '''
    # this is the 'catch all' exception.
    # this is not a good practice but you can use this as last option
    except Exception as e:
        print(e)

    else:
        # else block is optional
        print("Yay! No exception encountered.")
    finally:
        # finally block is optional - only use when you have a line/s of code
        # that need to execute regardless if an exception is encountered or not
        print("Finally block is always get executed")
        return result


# below is an example of docstring which explains what the function does
# this is a best practice to aid other programmer to understand your function
# it is enclosed by triple single quotation characters
def parse_input(input_expr: str) -> tuple:
    '''
    :param input_expr:
        a string consisting of <operand1><operation><operand2>
        example: 1+1
    :return: tuple
        returns the parsed_operands which is a list
        and operator which is a string together as tuple object
    '''
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

