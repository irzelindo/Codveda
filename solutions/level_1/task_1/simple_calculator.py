def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def calculator():
    """
    Simple calculator program that asks the user to select an operation and two numbers to perform the operation on.

    The program will then print the result of the operation.

    If the user enters an invalid operation, the program will print an error message.
    """
    print("Select operation: +, -, *, /")
    choice = input("Enter operation: ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    if choice in operations:
        print("Result:", operations[choice](a, b))
    else:
        print("Invalid operation!")

if __name__ == "__main__":
    calculator()
