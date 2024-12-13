def in_range(grid: list[str], position: tuple[int, int]) -> bool:
    return 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0])


def count_neighboring_fences(
    perimeter_position: tuple[int, int],
    new_position: tuple[int, int],
    offset: tuple[int, int],
    perimeters: set[tuple[int, int]],
    grid: list[str],
    plant: str,
):
    perimeter_row, perimeter_col = perimeter_position
    new_row, new_col = new_position
    row_offset, col_offset = offset
    return sum(
        (
            (perimeter_row - col_offset, perimeter_col - row_offset) in perimeters
            and (
                not in_range(grid, (new_row - col_offset, new_col - row_offset))
                or grid[new_row - col_offset][new_col - row_offset] != plant
            ),
            (perimeter_row + col_offset, perimeter_col + row_offset) in perimeters
            and (
                not in_range(grid, (new_row + col_offset, new_col + row_offset))
                or grid[new_row + col_offset][new_col + row_offset] != plant
            ),
        )
    )


def calculate_cost(grid: list[str], start: tuple[int, int], visited: set) -> int:
    plant = grid[start[0]][start[1]]
    stack = [start]
    visited.add((start[0], start[1]))
    perimeter, area = 0, 0
    while stack:
        row, col = stack.pop()
        area += 1
        for row_offset, col_offset in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = row + row_offset, col + col_offset
            if (
                not in_range(grid, (new_row, new_col))
                or grid[new_row][new_col] != plant
            ):
                perimeter += 1
                continue
            if (new_row, new_col) not in visited:
                stack.append((new_row, new_col))
                visited.add((new_row, new_col))
    return area * perimeter


def calculate_cost2(grid: list[str], start: tuple[int, int], visited: set) -> int:
    plant = grid[start[0]][start[1]]
    queue = [start]
    visited.add((start[0], start[1]))
    sides, area = 0, 0
    perimeters = set()
    while queue:
        row, col = queue.pop(0)
        area += 1
        for row_offset, col_offset in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = row + row_offset, col + col_offset
            perimeter_row, perimeter_col = row + row_offset / 2, col + col_offset / 2
            if (
                not in_range(grid, (new_row, new_col))
                or grid[new_row][new_col] != plant
            ):
                perimeters.add((perimeter_row, perimeter_col))
                if neighboring_fences := count_neighboring_fences(
                    perimeter_position=(perimeter_row, perimeter_col),
                    new_position=(new_row, new_col),
                    offset=(row_offset, col_offset),
                    perimeters=perimeters,
                    grid=grid,
                    plant=plant,
                ):
                    sides -= neighboring_fences - 1
                else:
                    sides += 1
                continue
            if (new_row, new_col) not in visited:
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))
    return area * sides


def part1(input: list[str]):
    total_cost = 0
    visited = set()
    for r in range(len(input)):
        for c in range(len(input[r])):
            if (r, c) in visited:
                continue
            total_cost += calculate_cost(input, (r, c), visited)
    return total_cost


def part2(input: list[str]):
    total_cost = 0
    visited = set()
    for r in range(len(input)):
        for c in range(len(input[r])):
            if (r, c) in visited:
                continue
            total_cost += calculate_cost2(input, (r, c), visited)
    return total_cost
