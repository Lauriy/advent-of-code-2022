from src.day_2 import solve_first, solve_second


def test_solve_first():
    answer = solve_first("day_2_example.txt")

    print(answer)
    assert answer == 15

    answer = solve_first("day_2_1.txt")

    print(answer)
    assert answer == 13924


def test_solve_second():
    answer = solve_second("day_2_example.txt")

    print(answer)
    assert answer == 12

    answer = solve_second("day_2_1.txt")

    print(answer)
    assert answer == 13448
