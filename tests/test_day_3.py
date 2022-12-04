from src.day_3 import solve_first, solve_second


def test_solve_first():
    answer = solve_first("day_3_example.txt")

    print(answer)
    assert answer == 157

    answer = solve_first("day_3_1.txt")

    print(answer)
    assert answer == 7674


def test_solve_second():
    answer = solve_second("day_3_example.txt")

    print(answer)
    assert answer == 70

    answer = solve_second("day_3_1.txt")

    print(answer)
    assert answer == 2805
