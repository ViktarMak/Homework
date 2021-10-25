# Task 1.4
# Write a Python program to sort a dictionary by key.


def sort_dictionary_by_key(input_dict):
    return dict(sorted(input_dict.items()))


test_dict = {4: 10, 6: 8, 1: 4, 5: 25, 2: 12, 3: 74}
print(sort_dictionary_by_key(test_dict))
