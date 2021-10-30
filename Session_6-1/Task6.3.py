# Task 4.3
# Implement The Keyword encoding and decoding for latin alphabet. The Keyword Cipher uses a Keyword to rearrange the
# letters in the alphabet. Add the provided keyword at the begining of the alphabet. A keyword is used as the key, and
# it determines the letter matchings of the cipher alphabet to the plain alphabet. Repeats of letters in the word are
# removed, then the cipher alphabet is generated with the keyword matching to A, B, C etc. until the keyword is used up,
# whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those already used in the key.

# Encryption: Keyword is "Crypto"
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# C R Y P T O A B D E F G H I J K L M N Q S U V W X Z


import string


class Cipher:

    alphabet = list(string.ascii_lowercase)
    alphabet_with_uppercase = alphabet + list(string.ascii_letters.upper())

    def __init__(self, keyword: str) -> None:
        self.__crypto_alphabet = sorted(
            set(list(keyword.lower()) + self.alphabet), key=lambda x: (list(keyword.lower()) + self.alphabet).index(x)
        )
        self.__crypto_alphabet += [i.upper() for i in self.__crypto_alphabet]

    def decode(self, string: str) -> str:
        result = ''
        for i in string:
            if i in self.alphabet_with_uppercase:
                result += self.alphabet_with_uppercase[self.__crypto_alphabet.index(i)]
            else:
                result += i
        return result

    def encode(self, string: str) -> str:
        result = ''
        for i in string:
            if i in self.alphabet_with_uppercase:
                result += self.__crypto_alphabet[self.alphabet_with_uppercase.index(i)]
            else:
                result += i
        return result


d = Cipher('Crypto')
print(d.encode('Hello World'))
print(d.decode('d ch atidjsn'))
