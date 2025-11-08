# PYTHON CHALLENGE 9: Find the second smallest element in a list
def find_second_smallest(data_list):
    """
    Finds the second smallest element in a list of numbers.

    Args:
        data_list: A list of numbers.

    Returns:
        The second smallest element in a list, or None if the list
        has fewer than two distint elements.
    """
    if len(data_list) < 2:
        return None # Not enough elements to find a second smallest
    
    # Convert to a set to remove duplicates, then convert back to a list and sort
    unique_sorted_list = sorted(list(set(data_list)))

    if len(unique_sorted_list) < 2:
        return None # Not enough distinct elements
    
    return unique_sorted_list[1]

# Example usage:
my_list1 = [5, 2, 8, 1, 9, 3]
print(f"The second smallest element in {my_list1} is: {find_second_smallest(my_list1)}")

my_list2 = [10, 10, 5, 5, 20]
print(f"The second smallest element in {my_list2} is: {find_second_smallest(my_list2)}")

my_list3 = [7]
print(f"The second smallest element in {my_list3} is: {find_second_smallest(my_list3)}")

my_list4 = [4, 4]
print(f"The second smallest element in {my_list4} is: {find_second_smallest(my_list4)}")