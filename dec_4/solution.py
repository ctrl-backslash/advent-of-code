PHRASE = 'XMAS'


def phrase_count(grid: list[str], row: int, col: int) -> int:
    phrases = 0
    for row_offset, col_offset in (
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
    ):
        for idx, c in enumerate(PHRASE):
            if not (0 <= row + idx * row_offset < len(grid)) or not (
                0 <= col + idx * col_offset < len(grid[0])
            ):
                break
            if c != grid[row + idx * row_offset][col + idx * col_offset]:
                break
        else:
            phrases += 1
    return phrases


def is_x_mas(grid: list[str], row: int, col: int) -> bool:
    if not (1 <= row < len(grid) - 1) or not (1 <= col < len(grid[0]) - 1):
        return False
    return {grid[row - 1][col - 1], grid[row + 1][col + 1]} == {'M', 'S'} and {
        grid[row - 1][col + 1],
        grid[row + 1][col - 1],
    } == {'M', 'S'}


def part1(input: list[str]):
    phrases = 0
    for row in range(len(input)):
        for col in range(len(input[row])):
            if input[row][col] == PHRASE[0]:
                phrases += phrase_count(input, row, col)
    return phrases


def part2(input: list[str]):
    phrases = 0
    for row in range(len(input)):
        for col in range(len(input[row])):
            if input[row][col] == 'A' and is_x_mas(input, row, col):
                phrases += 1
    return phrases
