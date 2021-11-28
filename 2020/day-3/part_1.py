from typing import List, TextIO


def parse_map(_map: TextIO) -> List[List[str]]:
    return [list(line.strip()) for line in _map]


def count_trees(toboggan_map: TextIO) -> int:
    # pace right 3 and down 1
    found_trees = 0
    index_x = 0

    parsed_map = parse_map(toboggan_map)
    max_y = len(parsed_map)
    max_x = len(parsed_map[0]) - 1

    for index_y in range(1, max_y):  # down walk
        index_x += 3  # side walk

        if index_x > max_x:
            index_x = index_x - max_x - 1  # start again from the beginning

        if parsed_map[index_y][index_x] == '#':
            found_trees += 1

    return found_trees
