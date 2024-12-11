import concurrent
from concurrent.futures import ProcessPoolExecutor
from functools import lru_cache, reduce
from itertools import product
from operator import add, mul


@lru_cache
def reduce_fn(acc, op_num):
    operator, num = op_num
    match operator:
        case '+':
            return add(acc, num)
        case '*':
            return mul(acc, num)
        case '|':
            return int(str(acc) + str(num))


def is_valid(line: str, operators: list[str]) -> int:
    test_value, numbers = line.split(':')
    test_value = int(test_value)
    numbers = [int(num) for num in numbers.strip(' ').split(' ')]
    for operator_set in product(operators, repeat=len(numbers) - 1):
        if test_value == reduce(
            reduce_fn,
            zip(operator_set, numbers[1:]),
            numbers[0],
        ):
            return test_value
    return 0


def part1(input: list[str], operators: list[str] = '+*'):
    total = 0
    # This is not the proper way to handle this. There are heuristics that indicate which operator is valid for each spot that is much more efficient.
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(is_valid, line, operators) for line in input]
        for future in concurrent.futures.as_completed(futures):
            try:
                total += future.result()
            except Exception as exc:
                raise RuntimeError(f'Failed to run future: {exc}')
    return total


def part2(input: list[str]):
    return part1(input, '+*|')
