from io import StringIO
from itertools import tee


def larger_measurement_count(measurements: StringIO) -> int:
    first, second = tee(map(int, measurements))
    next(second)
    increased = 0

    for previous, current in zip(first, second):
        increased += current > previous
    
    return increased
