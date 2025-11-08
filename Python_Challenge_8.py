# PYTHOON CHALLENGE 8: Sort a list of strings based on their lengths, from shortest to longest
def sort_strings_by_length_sorted(string_list):
    """
    Sorts a list  of strings by their length from shortest to longest using sorted().

    Args:
        string_list: A list of strings.

    Returns:
        A new list containing the strings sorted by length.
    """
    return sorted(string_list, key=len)
    
# Example usage:
my_strings = ["apple", "banana", "kiwi", "grapefruit", "cat"]
sorted_strings = sort_strings_by_length_sorted(my_strings)
print(f"Original list: {my_strings}")
print(f"Sorted list (using sorted()): {sorted_strings}")