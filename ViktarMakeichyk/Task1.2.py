# Task 1.2
# Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters)

string = input('Enter string:').lower()

char_frequency = {}

for element in string:
    if element in char_frequency:
        char_frequency[element] += 1
    else:
        char_frequency[element] = 1

print(char_frequency)
