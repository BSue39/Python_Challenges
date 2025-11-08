# PYTHON CHALLENGE 3: Count the number of vowels in a given string
def count_vowels(input_string):
    """
    Counts the number of vowels (a, e, i, o, u) in a given string,
    case-insensitively.

    Args:
        input_string: The string to analyze.

    Returns:
        The total count of vowels in the string.
    """
    vowels = "aeiou"
    vowel_count = 0
    for char in input_string:
        if char.lower() in vowels:
            vowel_count += 1
        return vowel_count

# Example usage:
my_string = "Hello World! This is a Test String."
num_vowels = count_vowels(my_string)
print(f"The string '{my_string}' contains {num_vowels} vowels.")

another_string = "Python Programming is Fun!"
num_vowels_2 = count_vowels(another_string)
print(f"The string '{another_string}' contains {num_vowels_2} vowels.")