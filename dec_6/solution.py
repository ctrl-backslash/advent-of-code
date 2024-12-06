from copy import deepcopy

from rich import print  # noqa: F401

DIRECTION_CHANGE = {
    # UP => RIGHT
    (-1, 0): (0, 1),
    # RIGHT => DOWN
    (0, 1): (1, 0),
    # DOWN => LEFT
    (1, 0): (0, -1),
    # LEFT => UP
    (0, -1): (-1, 0),
}


def part1(map: list[str]):
    visited = set()
    position = None
    for row_idx, row in enumerate(map):
        for col_idx, space in enumerate(row):
            if space == '^':
                position = (row_idx, col_idx)
    visited.add(position)

    direction = (-1, 0)
    while 0 <= position[0] + direction[0] < len(map) and 0 <= position[1] + direction[
        1
    ] < len(map[0]):
        if map[position[0] + direction[0]][position[1] + direction[1]] == '#':
            direction = DIRECTION_CHANGE[direction]
            continue
        position = (position[0] + direction[0], position[1] + direction[1])
        visited.add(position)
    return len(visited)


def is_cycle(
    map: list[str],
    position: tuple[int, int],
    direction: tuple[int, int],
) -> bool:
    visited = set()
    while 0 <= position[0] + direction[0] < len(map) and 0 <= position[1] + direction[
        1
    ] < len(map[0]):
        if (position, direction) in visited:
            return True
        visited.add((position, direction))

        new_position = (position[0] + direction[0], position[1] + direction[1])
        if map[new_position[0]][new_position[1]] == '#':
            direction = DIRECTION_CHANGE[direction]
            continue
        position = new_position
    return False


def part2(map: list[str]):
    possible_obstructions = set()
    visited = set()
    position = None
    for row_idx, row in enumerate(map):
        for col_idx, space in enumerate(row):
            if space == '^':
                position = (row_idx, col_idx)
    start_position = position

    direction = (-1, 0)
    while 0 <= position[0] + direction[0] < len(map) and 0 <= position[1] + direction[
        1
    ] < len(map[0]):
        new_position = (position[0] + direction[0], position[1] + direction[1])
        if map[new_position[0]][new_position[1]] == '#':
            direction = DIRECTION_CHANGE[direction]
            continue

        if new_position in visited:
            position = new_position
            continue

        new_map = deepcopy(map)
        row = new_map[new_position[0]]
        new_map[new_position[0]] = (
            f'{row[: new_position[1]]}#{row[new_position[1] + 1 :]}'
        )
        if is_cycle(new_map, position, direction):
            possible_obstructions.add(new_position)
        visited.add(new_position)
        position = new_position
    return len(possible_obstructions) - (
        1 if start_position in possible_obstructions else 0
    )
