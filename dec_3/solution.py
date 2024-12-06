import math
import re

mul_regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
instruction_regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)|(?:do|don\'t)\(\)')


def part1(input: list[str]):
    instruction = '\n'.join(input)
    total = 0
    for match in mul_regex.findall(instruction):
        total += math.prod(map(int, match))
    return total


def part2(input: list[str]):
    instruction = '\n'.join(input)
    total = 0
    enabled = True
    for match in instruction_regex.finditer(instruction):
        if match.group(0).startswith("don't"):
            enabled = False
        elif match.group(0).startswith('do'):
            enabled = True
        elif enabled and match.group(0).startswith('mul'):
            total += math.prod(map(int, match.groups()))

    return total
