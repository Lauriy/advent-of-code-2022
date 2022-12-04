import os


# https://stackoverflow.com/questions/32480423/how-to-check-if-a-range-is-a-part-of-another-range-in-python-3-x
def _range_subset(range1: range, range2: range):
    """Whether range1 is a subset of range2."""
    if not range1:
        return True  # empty range is subset of anything
    if not range2:
        return False  # non-empty range can't be subset of empty range
    if len(range1) > 1 and range1.step % range2.step:
        return False  # must have a single value or integer multiple step

    return range1.start in range2 and range1[-1] in range2


# https://stackoverflow.com/a/6821298/2517131
def _range_overlap(x: range, y: range):
    return range(max(x[0], y[0]), min(x[-1], y[-1]) + 1)


def solve_first(file_name: str) -> int:
    with open(f"{os.path.dirname(os.path.realpath(__file__))}/../in/{file_name}", "r") as f:
        data = [x.strip() for x in f]

    count = 0
    for line in data:
        elf1, elf2 = line.split(',')
        range1 = range(int(elf1.split('-')[0]), int(elf1.split('-')[1]) + 1)
        range2 = range(int(elf2.split('-')[0]), int(elf2.split('-')[1]) + 1)

        if _range_subset(range1, range2) or _range_subset(range2, range1):
            count += 1

    return count


def solve_second(file_name: str) -> int:
    with open(f"{os.path.dirname(os.path.realpath(__file__))}/../in/{file_name}", "r") as f:
        data = [x.strip() for x in f]

    count = 0
    for line in data:
        elf1, elf2 = line.split(',')
        range1 = range(int(elf1.split('-')[0]), int(elf1.split('-')[1]) + 1)
        range2 = range(int(elf2.split('-')[0]), int(elf2.split('-')[1]) + 1)

        if _range_overlap(range1, range2):
            count += 1

    return count
