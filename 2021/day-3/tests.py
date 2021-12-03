import unittest
from io import StringIO

from part_1 import calculate_position


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

        self.assertEqual(198, calculate_position(instructions))

    def test_original_input(self):
        with open('2021/day-3/input.txt', encoding='utf-8') as instructions:
            self.assertEqual(0, calculate_position(instructions))

    

class PartTwo(unittest.TestCase):
    def test_sample_input(self):
        pass

    def test_original_input(self):
        pass


if __name__ == '__main__':
    unittest.main()
