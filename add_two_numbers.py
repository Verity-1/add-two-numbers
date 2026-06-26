def add_two_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = add_two_numbers(num1, num2)
    print(f"Result: {num1} + {num2} = {result}")
