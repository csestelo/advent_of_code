import unittest
from io import StringIO

from part_1 import power_comsumption
from part_2 import life_support_rating


class PartOne(unittest.TestCase):
    def test_sample_input(self):
        instructions = StringIO('''
            00100
            11110
            10110
            10111
            10101
            01111
            00111
            11100
            10000
            11001
            00010
            01010
        '''.strip())

        self.assertEqual(198, power_comsumption(instructions))

    def test_original_input(self):
        with open('2021/day-3/input.txt', encoding='utf-8') as instructions:
            self.assertEqual(3958484, power_comsumption(instructions))

    

class PartTwo(unittest.TestCase):
    def test_sample_input(self):
        instructions = StringIO('''
            00100
            11110
            10110
            10111
            10101
            01111
            00111
            11100
            10000
            11001
            00010
            01010
        '''.strip())

        self.assertEqual(230, life_support_rating(instructions))

    def test_original_input(self):
        with open('2021/day-3/input.txt', encoding='utf-8') as instructions:
            self.assertEqual(1613181, life_support_rating(instructions))


if __name__ == '__main__':
    unittest.main()
