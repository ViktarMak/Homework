# Task 4.3
# Implement a function which works the same as str.split method (without using str.split itself, of course).


def spl_str(data: str):

    new_var = []
    split_list = ''
    for i in data:
        if i == ' ' and split_list != '':
            new_var.append(split_list.strip())
            split_list = ''
        elif i != ' ':
            split_list += i
        else:
            continue
    if split_list:
        new_var.append(split_list)

    return new_var


if __name__ == '__main__':
    print(spl_str('monday  sunday   saturday wednesday         week'))
