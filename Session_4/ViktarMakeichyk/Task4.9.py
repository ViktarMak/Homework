# Task 4.9
# Implement a bunch of functions which receive a changeable number of strings and return next parameters:
# characters that appear in all strings
# characters that appear in at least one string
# characters that appear at least in two strings
# characters of alphabet, that were not used in any string
# Note: use string.ascii_lowercase for list of alphabet letters
# test_strings = ["hello", "world", "python", ]
# print(test_1_1(*strings))
# {'o'}
# print(test_1_2(*strings))
# {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
# print(test_1_3(*strings))
# {'h', 'l', 'o'}
# print(test_1_4(*strings))
# {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}


import string


def test1_1(*strings):

    a = len(strings)
    chars = {}
    for i in strings:
        for char in set(i.lower()):
            chars[char] = chars.get(char, 0) + 1
    return sorted({k for k, v in chars.items() if v == a})


def test1_2(*strings):
    return sorted({char for word in strings for char in word.lower()})


def test1_3(*strings):

    chars = {}
    for word in strings:
        for char in set(word.lower()):
            chars[char] = chars.get(char, 0) + 1
    return sorted({k for k, v in chars.items() if v > 1})


def test1_4(*strings):
    return sorted(set(string.ascii_lowercase) - {char for word in strings for char in word.lower()})


test_strings = ["hello", "world", "python", ]

print(test1_1(*test_strings))
print(test1_2(*test_strings))
print(test1_3(*test_strings))
print(test1_4(*test_strings))
