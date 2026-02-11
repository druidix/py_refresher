#!/opt/homebrew/bin/python3.14

import math


def multiply(a, b):
    """
    Multiply two numbers. Supports integers and floats, including negative values.
    Returns an error message if either value is None or not a valid number.
    """
    if a is None or b is None:
        return "Neither value can be empty"
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: both values must be numbers (int or float)."
    # Only floats can be NaN/Inf; avoid calling math.isnan/math.isinf on int
    if (isinstance(a, float) and math.isnan(a)) or (isinstance(b, float) and math.isnan(b)):
        return "Error: values cannot be NaN."
    if (isinstance(a, float) and math.isinf(a)) or (isinstance(b, float) and math.isinf(b)):
        return "Error: values must be finite numbers."
    return a * b


def parse_number(s):
    """Parse a string to int if it's a whole number, otherwise float."""
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s

""" Run the program """
first_in = input("Enter first number: ")
second_in = input("Enter second number: ")
a, b = parse_number(first_in), parse_number(second_in)

result = multiply(a, b)
if isinstance(result, str):
    print(result)
else:
    print("The product of " + first_in + " and " + second_in + " is: <" + str(result) + ">")
