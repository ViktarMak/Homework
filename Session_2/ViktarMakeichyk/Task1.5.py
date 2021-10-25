# Task 1.5
# Write a Python program to print all unique values of all dictionaries in a list.

lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
unique_values = set()
for i in lst:
    for value in i.values():
        if value not in unique_values:
            unique_values.add(value)
print(unique_values)
