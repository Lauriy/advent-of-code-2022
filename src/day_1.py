import os


def _extract_elves(data_lines: [str]) -> [int]:
    current_elf_total = 0
    elf_numbers = []
    end = len(data_lines) - 1
    for i, line in enumerate(data_lines):
        if line == '':
            elf_numbers.append(current_elf_total)
            current_elf_total = 0
            continue

        current_elf_total += int(line)
        if i == end:
            elf_numbers.append(current_elf_total)

    return elf_numbers


def solve_first(file_name: str) -> int:
    with open(f"{os.path.dirname(os.path.realpath(__file__))}/../in/{file_name}", "r") as f:
        data = [x.strip() for x in f]

    return max(_extract_elves(data))


def solve_second(file_name: str) -> int:
    with open(f"{os.path.dirname(os.path.realpath(__file__))}/../in/{file_name}", "r") as f:
        data = [x.strip() for x in f]
    elf_numbers = _extract_elves(data)
    elf_numbers.sort(reverse=True)

    return sum(elf_numbers[:3])
