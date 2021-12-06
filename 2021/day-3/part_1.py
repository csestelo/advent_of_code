from collections import defaultdict
from io import StringIO
from typing import Dict, Iterable, List


def power_comsumption(report: StringIO) -> int:
    counter = count_bit_occurrencies(report)

    gamma_rate = retrieve_bits(counter, True)
    epsilon_rate = retrieve_bits(counter, False)

    return convert_to_decimal(gamma_rate) * convert_to_decimal(epsilon_rate)


def count_bit_occurrencies(report: Iterable) -> Dict[int, int]:
    counter = defaultdict(int)

    for line in report:
        for idx, bit in enumerate(line.strip()):
            if bit == '0':
                counter[idx] -= 1
            else:
                counter[idx] += 1
    return counter


def retrieve_bits(counter: Dict[int, int], most_common: bool) -> List[str]:
    if most_common:
        return [str(int(v >= 0)) for v in counter.values()]

    return [str(int(v < 0)) for v in counter.values()]


def convert_to_decimal(rate: List[str]) -> int:
    return int(''.join(rate), 2)