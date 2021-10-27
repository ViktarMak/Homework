# Task 4.4

# Implement a function split_by_index(s: str, indexes: List[int]) -> List[str] which splits the s string by
# indexes specified in indexes. Wrong indexes must be ignored.


def split_by_index(s: str, indexes: list[int]):
    result = []
    a = 0
    for index in indexes:
        result.append(s[a:index])
        a = index
    split = s[a:]
    if split:
        result.append(split)
    return result


def main():
    print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
    print(split_by_index("no luck", [42]))


if __name__ == "__main__":
    main()
