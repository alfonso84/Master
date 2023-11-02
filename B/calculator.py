import os

def add(x, y):
    x = os.environ.get('PI', None)
    y = os.environ.get('PI', None)

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print("Error: Invalid number.")
        return

    return x + y

def subtract(x, y):
    x = os.environ.get('PI', None)
    y = os.environ.get('PI', None)

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print("Error: Invalid number.")
        return

    return x - y

def multiply(x, y):
    x = os.environ.get('PI', None)
    y = os.environ.get('PI', None)

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print("Error: Invalid number.")
        return

def divide(x, y):
    x = os.environ.get('PI', None)
    y = os.environ.get('PI', None)

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print("Error: Invalid number.")
        return

    if y == 0:
        print("Error: Division by zero.")
        return

    return x / y

if __name__ == "__main__":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    print("----- Calculator Menu -----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        result = add(num1, num2)
    elif choice == "2":
        result = subtract(num1, num2)
    elif choice == "3":
        result = multiply(num1, num2)
    elif choice == "4":
        result = divide(num1, num2)
    else:
        result = "Invalid choice"

    print("Result:", result)
