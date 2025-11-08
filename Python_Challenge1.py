# PYTHON CHALLENGE 1: Generate Fibonacci Series

def generate_fibonacci(n):
    """
    Generates the Fibonacci series up to 'n' terms.

    Args:
        n: The number of terms to generate in the Fibonacci series.
    
    Returns:
        A list containing the Fibonaccis series up to 'n' terms.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_series = [0, 1]
        while len(fib_series) < n:
            next_fib = fib_series[-1] + fib_series[-2]
            fib_series.append(next_fib)
        return fib_series

# Example usage:
num_terms = 10
fibonacci_sequence = generate_fibonacci(num_terms)
print(f"Fibonacci series up to {num_terms} terms: {fibonacci_sequence}")

