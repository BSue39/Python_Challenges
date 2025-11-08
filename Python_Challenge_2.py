# PYTHON CHALLENGE 2: Calculate Factorial
import math

def calculate_factorial_builtin(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    return math.factorial(n)

# Example usage:
num = 5
print(f"The factorial of {num} using math.factortial() is: {calculate_factorial_builtin(num)}")