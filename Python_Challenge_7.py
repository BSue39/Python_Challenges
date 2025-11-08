# PYTHON CHALLENGE 7: Find the first non-repeated character in a given string
from collections import Counter

def find_first_non_repeated_char(s):
    """
    Finds the first non-repeated character in a given string.

    Args:
        s: The input string.

    Returns:
        The first non-repeated character in the string, or None if no such character exists.
    """
    char_counts = Counter(s) # Count the frequency of each character

    for char in s:
        if char_counts[char] == 1:
            return char # Return the first character with a count of 1
        
        return None # No non-repeated character found 
    
# Example usage:
string1 = "programming"
result1 = find_first_non_repeated_char(string1)
print(f"The first non-repeated character in '{string1}' is: {result1}")

string2 = "aabbcc"
result2 = find_first_non_repeated_char(string2)
print(f"The first non-repeated character in '{string2}' is: {result2}")

string3 = "level"
result3 = find_first_non_repeated_char(string3)
print(f"The first non-repeated character in '{string3}' is: {result3}")

string4 = ""
result4 = find_first_non_repeated_char(string4)
print(f"The first non-repeated character in '{string4}' is: {result4}")