from collections import Counter


def part1(input: list[str]):
    left_list, right_list = list(), list()
    for line in input:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

    total_distance = 0
    for left, right in zip(sorted(left_list), sorted(right_list)):
        total_distance += abs(left - right)
    return total_distance


def part2(input: list[str]):
    left_list, right_list = list(), list()
    for line in input:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))
    right_counter = Counter(right_list)
    return sum(num * right_counter[num] for num in left_list)
