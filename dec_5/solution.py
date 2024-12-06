from collections import defaultdict
from itertools import takewhile

from rich import print  # noqa: F401


def part1(input: list[str]):
    input = iter(input)

    page_to_dependencies = defaultdict(set)

    for line in takewhile(lambda line: line, input):
        page, dependency = line.split('|')
        page_to_dependencies[page].add(dependency)

    total = 0
    for update in input:
        update = update.split(',')
        update_pages = set()
        for page in update:
            if page_to_dependencies[page] & update_pages:
                break
            update_pages.add(page)
        else:
            total += int(update[len(update) // 2])
    return total


def part2(input: list[str]):
    input = iter(input)

    page_to_dependencies = defaultdict(set)
    dependency_to_pages = defaultdict(set)

    for line in takewhile(lambda line: line, input):
        page, dependency = line.split('|')
        page_to_dependencies[page].add(dependency)
        dependency_to_pages[dependency].add(page)

    total = 0
    for update in input:
        update = update.split(',')
        update_pages = set()
        for page in update:
            if page_to_dependencies[page] & update_pages:
                update_set = set(update)
                # Hacky and not correct. It relies on there only being one valid order
                # for every update. If more than one exists, this function fails pretty
                # terribly.
                fixed_update = [
                    item[0]
                    for item in sorted(
                        (
                            (num, len(dependency_to_pages[num] & update_set))
                            for num in update
                        ),
                        key=lambda item: item[1],
                    )
                ]
                total += int(fixed_update[len(fixed_update) // 2])
                break
            update_pages.add(page)
    return total
