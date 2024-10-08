def calculator():
    # Requesting the first number
    num1 = input("Enter the first number (0-9): ")
    while not num1.isdigit() or not (0 <= int(num1) <= 9):
        num1 = input("Invalid input. Please enter a number between 0 and 9: ")

    # Requesting the second number
    num2 = input("Enter the second number (0-9): ")
    while not num2.isdigit() or not (0 <= int(num2) <= 9):
        num2 = input("Invalid input. Please enter a number between 0 and 9: ")

    # Requesting the operator
    operator = input("Enter an operator (+, -, *, /): ")
    while operator not in ['+', '-', '*', '/']:
        operator = input("Invalid operator. Please enter one of +, -, *, /: ")

    # Performing the calculation
    num1 = int(num1)
    num2 = int(num2)
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error! Division by zero."
        result = num1 / num2

    return f"The result of {num1} {operator} {num2} is: {result}"

# Running the calculator
print(calculator())