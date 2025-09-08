""""
A simple math utilities module providing basic arithmetic operations.
Functions: add, subtract, multiply, divide.
Authors: Masoumeh Tafvizi
Date: October 2025
"""

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a and b. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


__all__ = ['add',]

if __name__ == "__main__":
    assert add(2, 3) == 5
    assert subtract(5, 3) == 2
    assert multiply(4, 3) == 12
    assert divide(10, 2) == 5
    print("All tests passed.")
    
else:
    print("not running my_math.py directly")