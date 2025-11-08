# PYTHON CHALLENGE 10: Check if two strings are anagrams
def are_anagrams(str1, str2):
    """
    Checks if two strings are anagrams
    (contains the same characters in a different order)
    of each other.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    # Convert strings to lowercase and remove spaces for case-insensitive and space-agnostic comparison
    str1_processed = sorted(str1.lower().replace(" ", ""))
    str2_processed = sorted(str2.lower().replace(" ", ""))

    # Anagrams must have the same characters with the same frequencies,
    # so their sorted versions will be identical.
    return str1_processed == str2_processed

# Example usage:
string1 = "Listen"
string2 = "Silent"

if are_anagrams(string1, string2):
    print(f"'{string2}' and '{string2}' are anagrams.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams.")

string3 = "Hello"
string4 = "World"

if are_anagrams(string3, string4):
    print(f"'{string3}' and '{string4}' are anagrams.")
else:
    print(f"'{string3}' and '{string4}' are not anagrams.")

string5 = "Debit Card"
string6 = "Bad Credit"

if are_anagrams(string5, string6):
    print(f"'{string5}' and '{string6}' are anagrams.")
else:
    print(f"'{string5}' and '{string6}' are not anagrams.")