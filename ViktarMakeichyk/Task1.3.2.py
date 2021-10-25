# Task 1.3.2
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number


num, result = int(input()), list()

for i in range(1, num + 1):
    if num % i == 0:
        result.append(i)

print(result)
