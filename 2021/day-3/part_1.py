from collections import defaultdict
from io import StringIO
from typing import List


def convert_to_decimal(rate: List[str]) -> int:
    return int(''.join(rate), 2)

def power_comsumption(report: StringIO) -> int:
    counter = defaultdict(int)

    for line in report:
        for idx, bit in enumerate(line.strip()):
            if bit == '0':
                counter[idx] -= 1
            else:
                counter[idx] += 1

    gamma_rate = [str(int(v > 0)) for v in counter.values()]
    epsilon_rate = [str(int(v < 0)) for v in counter.values()]

    return convert_to_decimal(gamma_rate) * convert_to_decimal(epsilon_rate)
