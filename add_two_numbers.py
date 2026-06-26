# ─────────────────────────────────────────────
# math_operations.py
# Basic arithmetic operations: addition and multiplication
# ─────────────────────────────────────────────


def add_two_numbers(a, b):
    """Return the sum of two numbers.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        Sum of a and b
    """
    return a + b


def multiply_two_numbers(a, b):
    """Return the product of two numbers.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        Product of a and b
    """
    return a * b


if __name__ == "__main__":
    # Prompt user for two numeric inputs
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Display results for both operations
    print(f"Addition:       {num1} + {num2} = {add_two_numbers(num1, num2)}")
    print(f"Multiplication: {num1} x {num2} = {multiply_two_numbers(num1, num2)}")
