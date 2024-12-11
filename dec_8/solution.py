from collections import defaultdict
from itertools import combinations


def part1(input: list[str]):
    frequency_positions = defaultdict(list)
    for r, row in enumerate(input):
        for c, spot in enumerate(row):
            if spot != '.':
                frequency_positions[spot].append((r, c))

    anti_nodes = set()
    for positions in frequency_positions.values():
        for pos1, pos2 in combinations(positions, 2):
            left, right = (pos1, pos2) if pos1[1] < pos2[1] else (pos2, pos1)
            rise, run = left[0] - right[0], right[1] - left[1]
            for anti_node in [
                (right[0] - rise, right[1] + run),
                (left[0] + rise, left[1] - run),
            ]:
                if 0 <= anti_node[0] < len(input) and 0 <= anti_node[1] < len(input[0]):
                    anti_nodes.add(anti_node)
    return len(anti_nodes)


def part2(input: list[str]):
    frequency_positions = defaultdict(list)
    for r, row in enumerate(input):
        for c, spot in enumerate(row):
            if spot != '.':
                frequency_positions[spot].append((r, c))

    anti_nodes = set()
    for positions in frequency_positions.values():
        for pos1, pos2 in combinations(positions, 2):
            left, right = (pos1, pos2) if pos1[1] < pos2[1] else (pos2, pos1)
            rise, run = left[0] - right[0], right[1] - left[1]
            while 0 <= right[0] < len(input) and 0 <= right[1] < len(input[0]):
                anti_nodes.add(right)
                right = (right[0] - rise, right[1] + run)

            while 0 <= left[0] < len(input) and 0 <= left[1] < len(input[0]):
                anti_nodes.add(left)
                left = (left[0] + rise, left[1] - run)
    return len(anti_nodes)
