# PYTHON CHALLENGE 5: Check if a given string is a pangram (contains all letters of the alphabet)
import string

def is_pangram(text):
    """
    Checks if a given string is a pangram.

    A pangram is a sentence or phrase containing  every letter of the alphabet
    at least once. This function considers only the lowercase English alphabet.

    Args:
        text: The input string to check.

    Returns:
        True if the string is a pangram, False otherwise.
    """
    # Convert the input text to lowercase to handle case-insensitivity
    text_lower = text.lower()

    # Create a set of all unique alphabetic characters in the input text
    # Filter out non-alphabetic characters
    text_letters = {char for char in text_lower if char.isalpha()}

    # Get a set of all lowercase English alphabet letters
    english_alphabet = set(string.ascii_lowercase)

    #C Check if the set of English alphabet letters is a subset of the
    # set of letters found in the input text.
    # This means all letters of the alphabet must be present in the text.
    return english_alphabet.issubset(text_letters)

# Example usage:
sentence1 = "The quick brown fox jumps over the lazy dog"
sentence2 = "Hello, world!"
sentence3 = "Pack my box with five dozen liquor jugs"

print(f"'{sentence1}' is a pangram: {is_pangram(sentence1)}")
print(f"'{sentence2}' is a pangram: {is_pangram(sentence2)}")
print(f"'{sentence3}' is a pangram: {is_pangram(sentence3)}")