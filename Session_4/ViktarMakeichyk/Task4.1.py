# Task 4.1
# Implement a function which receives a string and replaces all " symbols with ' and vise versa.


Example = input("Please, enter the text: ")


def symbol_replace(string):

    result = ''

    for char in string:
        if char == "'":
            result += '"'
        elif char == '"':
            result += "'"
        else:
            result += char
    return result


print(symbol_replace(Example))
