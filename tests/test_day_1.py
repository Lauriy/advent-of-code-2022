from src.day_1 import solve_first, solve_second


def test_solve_first():
    answer = solve_first("day_1_example.txt")

    print(answer)
    assert answer == 24000

    answer = solve_first("day_1_1.txt")

    print(answer)
    assert answer == 66616


def test_solve_second():
    answer = solve_second("day_1_example.txt")

    print(answer)
    assert answer == 45000

    answer = solve_second("day_1_1.txt")

    print(answer)
    assert answer == 199172
