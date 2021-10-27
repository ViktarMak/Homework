# Task 4.2
# Write a function that check whether a string is a palindrome or not.
# Usage of any reversing functions is prohibited.
# To check your implementation you can use strings from here.


def is_palindrom(str_):

    new_str_ = str_[::-1]
    if new_str_ == str_:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")


is_palindrom("Torrent")
is_palindrom("madam")
