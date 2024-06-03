import math
import calculator_art

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def substraction(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a and b. If b is zero, return an error message."""
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def sqrt(a):
    """Return the square root of a."""
    if a < 0:
        return "Cannot take the square root of a negative number"
    return math.sqrt(a)

def perform_operation(a, op, b=None):
    """
    Perform the arithmetic operation based on the operator provided.
    
    Parameters:
    a (float): The first operand.
    op (str): The operator as a string.
    b (float, optional): The second operand. Defaults to None for unary operations.
    
    Returns:
    float or str: The result of the operation or an error message if the operation is invalid.
    """
    if op in operation:
        if b is not None:
            return operation[op](a, b)
        return operation[op](a)
    return "Invalid operation"

def main():
    """Main function to perform a series of arithmetic operations based on user input."""
    print(calculator_art.logo)
    while True:
        a = float(input("Enter the first number: "))

        print("Operations available:")
        for symbol in operation:
            print(symbol)

        op = input("Enter the operation you want to perform: ")

        if op == '√':
            result = perform_operation(a, op)
            print(f"The result of {op}{a} is: {result}")
        else:
            b = float(input("Enter the second number: "))
            result = perform_operation(a, op, b)
            print(f"The result of {a} {op} {b} is: {result}")

        while True:
            another_operation = input("Do you want to perform another operation with the result? (yes/no): ").lower()
            if another_operation == 'no':
                break

            print("Operations available:")
            for symbol in operation:
                print(symbol)

            op = input("Enter the next operation you want to perform: ")

            if op == '√':
                result = perform_operation(result, op)
                print(f"The result of {op}{result} is: {result}")
            else:
                c = float(input("Enter the next number: "))
                result = perform_operation(result, op, c)
                print(f"The result of the previous result {op} {c} is: {result}")

        start_over = input("Do you want to start the calculation from the beginning? (yes/no): ").lower()
        if start_over == 'no':
            break

if __name__ == "__main__":
    operation = {
        '+': add,
        '-': substraction,
        '*': multiply,
        '/': divide,
        '√': sqrt
    }
    main()
