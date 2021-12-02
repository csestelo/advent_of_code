from io import StringIO


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
