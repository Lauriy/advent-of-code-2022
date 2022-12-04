from src.day_4 import solve_first, solve_second


def test_solve_first():
    answer = solve_first("day_4_example.txt")

    print(answer)
    assert answer == 2

    answer = solve_first("day_4_1.txt")

    print(answer)
    assert answer == 567


def test_solve_second():
    answer = solve_second("day_4_example.txt")

    print(answer)
    assert answer == 4

    answer = solve_second("day_4_1.txt")

    print(answer)
    assert answer == 907
