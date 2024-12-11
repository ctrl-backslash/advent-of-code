def dfs(grid: list[str], start: tuple[int, int], with_replacement: bool = False) -> int:
    visited = set()
    stack = [(start, 0)]
    total = 0
    while stack:
        pos, elevation = stack.pop()

        if not with_replacement and pos in visited:
            continue
        visited.add(pos)

        if elevation == 9:
            total += 1

        for offset_r, offset_c in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            if not (0 <= pos[0] + offset_r < len(grid)) or not (
                0 <= pos[1] + offset_c < len(grid[0])
            ):
                continue

            if int(grid[pos[0] + offset_r][pos[1] + offset_c]) == elevation + 1:
                stack.append(((pos[0] + offset_r, pos[1] + offset_c), elevation + 1))
    return total


def part1(input: list[str]):
    trailheads = list()
    for r, row in enumerate(input):
        for c, elevation in enumerate(row):
            if int(elevation) == 0:
                trailheads.append((r, c))

    total = 0
    for trailhead in trailheads:
        total += dfs(input, trailhead)
    return total


def part2(input: list[str]):
    trailheads = list()
    for r, row in enumerate(input):
        for c, elevation in enumerate(row):
            if int(elevation) == 0:
                trailheads.append((r, c))

    total = 0
    for trailhead in trailheads:
        total += dfs(input, trailhead, True)
    return total
