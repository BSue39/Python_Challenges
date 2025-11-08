# PYTHON CHALLENGE 4: Find the largest element in a list
def find_largest_element(input_list):
    """
    Finds the largest element in a given list.

    Args:
        input_list: A list of comparable elements (e.g., numbers, strings).

    Returns:
        The largest element in the list.
        Raises ValueError if the input_list is empty.
    """
    if not input_list:
        raise ValueError("The input list cannot be empty.")
    return max(input_list)

# Example usage:
my_numbers = [10, 324, 45, 90, 9808]
largest_number = find_largest_element(my_numbers)
print(f"The largest number in {my_numbers} is: {largest_number}")

my_strings = ["apple", "banana", "kiwi", "orange"]
largest_string = find_largest_element(my_strings)
print(f"The largest string in {my_strings} is: {largest_string}")

empty_list = []
try:
    find_largest_element(empty_list)
except ValueError as e:
    print(f"Error: [e]")