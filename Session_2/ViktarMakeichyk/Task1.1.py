# Task 1.1
# Write a Python program to calculate the length of a string without using the 'len' function

string = input("Enter string:")
count = 0
for i in string:
    count = count+1

print(f'Length of string: {count}')
