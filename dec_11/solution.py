from collections import Counter, defaultdict
from functools import reduce
from operator import add


def part1(input: list[str], iterations: int = 25):
    rock_collection = Counter(map(int, input[0].split(' ')))
    for _ in range(iterations):
        new_rock_collection = defaultdict(lambda: 0)
        for rock, count in rock_collection.items():
            if rock == 0:
                new_rock_collection[1] += count
            elif (rock_length := len(str(rock))) % 2 == 0:
                new_rock_collection[int(str(rock)[: rock_length // 2])] += count
                new_rock_collection[int(str(rock)[rock_length // 2 :])] += count
            else:
                new_rock_collection[rock * 2024] += count
        rock_collection = new_rock_collection
    return reduce(add, rock_collection.values())


def part2(input: list[str]):
    return part1(input, 75)
