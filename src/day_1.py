import os


def solve_first(file_name: str) -> int:
    with open(f"{os.path.dirname(os.path.realpath(__file__))}/../in/{file_name}", "r") as f:
        data = [x.strip() for x in f]
    current_elf_total = 0
    elf_numbers = []
    for line in data:
        try:
            number = int(line)
            current_elf_total += number
        except ValueError:
            elf_numbers.append(current_elf_total)
            current_elf_total = 0

    return max(elf_numbers)


def solve_second(file_name: str) -> int:
    with open(f"{os.path.dirname(os.path.realpath(__file__))}/../in/{file_name}", "r") as f:
        data = [x.strip() for x in f]
    current_elf_total = 0
    elf_numbers = []
    for line in data:
        try:
            number = int(line)
            current_elf_total += number
        except ValueError:
            elf_numbers.append(current_elf_total)
            current_elf_total = 0

    elf_numbers.sort(reverse=True)

    return sum(elf_numbers[:3])
