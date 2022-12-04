import os
import string


def _get_common_elements(string1: str, string2: str):
    return set(string1) & set(string2)


def solve_first(file_name: str) -> int:
    with open(f"{os.path.dirname(os.path.realpath(__file__))}/../in/{file_name}", "r") as f:
        data = [x.strip() for x in f]

    score = 0
    for s in data:
        common = _get_common_elements(s[:len(s) // 2], s[len(s) // 2:])
        score += sum(string.ascii_lowercase.index(x) + 1 for x in common if x in string.ascii_lowercase)
        score += sum(string.ascii_uppercase.index(x) + 27 for x in common if x in string.ascii_uppercase)

    return score


def solve_second(file_name: str) -> int:
    with open(f"{os.path.dirname(os.path.realpath(__file__))}/../in/{file_name}", "r") as f:
        data = [x.strip() for x in f]

    total = 0
    for i in range(int(len(data) / 3)):
        common_1_2 = _get_common_elements(data[i * 3], data[i * 3 + 1])
        common_3_rest = _get_common_elements(''.join(common_1_2), data[i * 3 + 2])
        common_element = list(common_3_rest)[0]
        if common_element in string.ascii_lowercase:
            total += string.ascii_lowercase.index(common_element) + 1
        else:
            total += string.ascii_uppercase.index(common_element) + 27

    return total
