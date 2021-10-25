# Task 1.6.1
# Write a Python program to convert a given tuple of positive integers into an integer.

num = ''

for i in input():
    if i.isdigit():
        num += i

print(int(num))
