from io import StringIO
from typing import List
from part_1 import convert_to_decimal, count_bit_occurrencies, retrieve_bits


def life_support_rating(report: StringIO) -> int:
    rates = [rate.strip() for rate in report]
    
    oxygen_generator = calculate_rating(rates, 'oxygen_generator')
    co2_scrubber = calculate_rating(rates, 'co2_scrubber')
    
    return oxygen_generator * co2_scrubber


def calculate_rating(rates: List[str], type_rating: str) -> int:
    rates = rates.copy()
    presence = type_rating == 'oxygen_generator'

    for idx in range(len(rates[0])):
        if len(rates) == 1:
            break

        counter = count_bit_occurrencies(rates)
        curr_bit = retrieve_bits(counter=counter, most_common=presence)

        remaining_rates = []
        for rate in rates:
            if curr_bit[idx] == rate[idx]:
                remaining_rates.append(rate)

        rates = remaining_rates

    return convert_to_decimal(rates[0])
