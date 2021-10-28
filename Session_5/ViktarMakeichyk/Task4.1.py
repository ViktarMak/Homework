# Task 4.1
# Open file data/unsorted_names.txt in data folder. Sort the names and write them to a new file called sorted_names.txt.
# Each name should start with a new line as in the following example:
# Adele
# Adrienne
# ...
# Willodean
# Xavier

with open("data/unsorted_names.txt", "r") as file:
    sorted_names = sorted(file.readlines())
    with open("data/sorted_names.txt", "w") as sf:
        sf.writelines(sorted_names)
