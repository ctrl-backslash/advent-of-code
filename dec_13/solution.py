import re
from itertools import takewhile

X_Y_REGEX = re.compile(r'X[+=](\d+), Y[+=](\d+)')


def part1(input: list[str], offset: int = 0):
    total_cost = 0
    for idx in range(0, len(input), 4):
        button_a, button_b, prize = map(
            lambda line: tuple(map(int, X_Y_REGEX.search(line).groups())),
            takewhile(lambda line: line, input[idx : idx + 3]),
        )
        prize = (prize[0] + offset, prize[1] + offset)
        demoninator = (button_a[1] * button_b[0]) - (button_a[0] * button_b[1])
        button_a_presses = (
            (button_b[0] * prize[1]) - (button_b[1] * prize[0])
        ) / demoninator
        button_b_presses = (
            (button_a[1] * prize[0]) - (button_a[0] * prize[1])
        ) / demoninator
        if button_a_presses.is_integer() and button_b_presses.is_integer():
            total_cost += button_a_presses * 3 + button_b_presses
    return total_cost


def part2(input: list[str]):
    return part1(input, 10000000000000)
