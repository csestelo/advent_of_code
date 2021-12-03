import unittest
from io import StringIO

from part_1 import calculate_position


class PartOne(unittest.TestCase):
    def test_sample_input(self):
        measurements = StringIO('''
            forward 5
            down 5
            forward 8
            up 3
            down 8
            forward 2
        '''.strip())

        self.assertEqual(150, calculate_position(measurements))

    def test_original_input(self):
        with open('2021/day-2/input.txt', encoding='utf-8') as measurements:
            self.assertEqual(1524750, calculate_position(measurements))

    

class PartTwo(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
