def add_two_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


def multiply_two_numbers(a, b):
    """Return the product of two numbers."""
    return a * b


if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Addition:       {num1} + {num2} = {add_two_numbers(num1, num2)}")
    print(f"Multiplication: {num1} x {num2} = {multiply_two_numbers(num1, num2)}")
