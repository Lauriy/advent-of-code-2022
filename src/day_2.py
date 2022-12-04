import os

ROCK = ('A', 'X')
PAPER = ('B', 'Y')
SCISSORS = ('C', 'Z')

SCORE_MATRIX = (
    (4, 8, 3),
    (1, 5, 9),
    (7, 2, 6)
)

WIN_LOSS_MAP = {
    'A': {
        'X': 'Z',  # Rock played, need to lose, response scissors
        'Y': 'X',
        'Z': 'Y'
    },
    'B': {
        'X': 'X',  # Paper played, need to lose, response rock
        'Y': 'Y',
        'Z': 'Z'
    },
    'C': {
        'X': 'Y',  # Scissors played, need to lose, response paper
        'Y': 'Z',
        'Z': 'X'
    }
}


def _score_move(opponent: str, me: str) -> int:
    if opponent in ROCK:
        row = 0
    elif opponent in PAPER:
        row = 1
    else:
        row = 2
    if me in ROCK:
        column = 0
    elif me in PAPER:
        column = 1
    else:
        column = 2

    return SCORE_MATRIX[row][column]


def solve_first(file_name: str) -> int:
    with open(f"{os.path.dirname(os.path.realpath(__file__))}/../in/{file_name}", "r") as f:
        data = [x.strip() for x in f]

    return sum(_score_move(x.split(' ')[0], x.split(' ')[1]) for x in data)


def solve_second(file_name: str) -> int:
    with open(f"{os.path.dirname(os.path.realpath(__file__))}/../in/{file_name}", "r") as f:
        data = [x.strip() for x in f]

    total = 0
    for line in data:
        opponent, me = line.split(' ')
        correct_move = WIN_LOSS_MAP[opponent][me]
        total += _score_move(opponent, correct_move)

    return total
