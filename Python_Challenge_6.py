# PYTHON CHALLENGE 6: Reverse the words in a given sentence
def reverse_words_in_sentence(sentence):
    """
    Reverses the order of words in a given sentence.

    Args:
        sentence: The input string sentence.

    Returns:
        A new string with the words in reversed order.
    """
    words = sentence.split() # Split the sentence into a list of words
    reversed_words = words[::-1] # Reverse the order of words in the list
    reversed_sentence = " ".join(reversed_words) # Join the words back into a sentence
    return reversed_sentence

# Example usage:
input_sentence = "This is a sample sentence for reversing words."
output_sentence = reverse_words_in_sentence(input_sentence)
print(f"Original sentence: '{input_sentence}'")
print(f"Reversed sentence: '{output_sentence}'")

input_sentence_2 = "Python is fun and powerful!"
output_sentence_2 = reverse_words_in_sentence(input_sentence_2)
print(f"Original sentence: '{input_sentence_2}'")
print(f"Reversed sentence: '{output_sentence_2}'")