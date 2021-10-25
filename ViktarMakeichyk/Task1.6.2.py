# Task 1.6.2
# Write a program which makes a pretty print of a part of the multiplication table.


a = int(input('Please, enter a:'))
b = int(input('Please, enter b:'))
c = int(input('Please, enter c:'))
d = int(input('Please, enter d:'))

print('\t', end="")

for i in range(c, d + 1):
    print(i, end='\t')
print()

for i in range(a, b + 1):
    print(i, end="\t")

    for j in range(c, d + 1):
        print(j * i, end="\t")
    print()
