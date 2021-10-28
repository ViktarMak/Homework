# Task 4.2
# Implement a function which search for most common words in the file. Use data/lorem_ipsum.txt file as a example.
# def most_common_words(filepath, number_of_words=3):
#    pass

# print(most_common_words('lorem_ipsum.txt'))
# ['donec', 'etiam', 'aliquam']
# NOTE: Remember about dots, commas, capital letters etc.


import collections
import re

with open("lorem_ipsum.txt") as file:
    text = file.read()

words = re.compile(r"[\w']+").findall(text)
counts = collections.Counter(words).most_common(3)
print(counts)

