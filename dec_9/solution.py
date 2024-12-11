from functools import reduce
from operator import add


def part1(input: list[str]):
    disk_map = input[0]
    stack = list()
    for idx, disk_num in enumerate(disk_map):
        stack.extend([idx // 2 if idx % 2 == 0 else None] * int(disk_num))

    total = 0
    block_pos = 0
    while stack:
        if stack[-1] is None:
            stack.pop()
            continue

        if stack[0] is None:
            stack.pop(0)
            total += block_pos * stack.pop()
        else:
            total += block_pos * stack.pop(0)
        block_pos += 1
    return total


def part2(input: list[str]):
    disk_map = input[0]
    stack = list()
    for idx, disk_num in enumerate(disk_map):
        stack.append((idx // 2 if idx % 2 == 0 else None, int(disk_num)))

    for block_idx, block_size in reversed(stack):
        for idx in range(len(stack)):
            if block_idx == stack[idx][0]:
                break
            if stack[idx][0] is not None or stack[idx][1] < block_size:
                continue
            if stack[idx][1] > block_size:
                stack.insert(idx + 1, (None, stack[idx][1] - block_size))
            stack[idx] = (block_idx, block_size)
            break

    total = 0
    block_pos = 0
    used = set()
    for block_idx, block_size in stack:
        if block_idx is not None and block_idx not in used:
            total += reduce(
                add,
                [idx * block_idx for idx in range(block_pos, block_pos + block_size)],
            )
            used.add(block_idx)
        block_pos += block_size
    return total
