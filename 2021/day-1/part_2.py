from io import StringIO
from itertools import tee 


def larger_triple_measurement_count(measurements: StringIO) -> int:
    items = map(int, measurements)
    increased = 0
    first = next(items)
    second = next(items)
    third = next(items)
    last_group = first + second + third

    for next_measurement in items:
        first = second
        second = third
        third = next_measurement

        new_group = first + second + third
        increased += new_group > last_group
        last_group = new_group

    return increased


# second generic solution, `count_increased` works for part 1 as well

def windows(iterator, window_size):
    parts = []

    to_break = iterator
    for _ in range(window_size - 1):
        first, second = tee(to_break)
        next(second)
        parts.append(first)
        to_break = second

    parts.append(second)

    return zip(*parts)


def count_increased(items):
    increased= 0
    for prev, curr in windows(items, 2):
        increased += curr > prev
    return increased

def larger_triple_measurement_count_optional(measurements: StringIO) -> int:
    items = map(int, measurements)
    w3 = windows(items, 3)
    sums = map(sum, w3)
    increased = count_increased(sums)
    return increased
