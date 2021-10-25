# Task1.3.1
# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words
# in sorted form.

items = input('Please, enter words:')
some_list = items.split(',')
print(some_list)
unique_words = []
for word in some_list:
    if word not in unique_words:
        unique_words.append(word)
print(sorted(unique_words))
