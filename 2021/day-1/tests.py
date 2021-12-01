import unittest
from io import StringIO

from part_1 import larger_measurement_count


class PartOne(unittest.TestCase):
    def test_sample_input(self):
        measurements = StringIO('''
            199
            200
            208
            210
            200
            207
            240
            269
            260
            263
        '''.strip())

        self.assertEqual(7, larger_measurement_count(measurements))

    def test_original_input(self):
        with open('2021/day-1/input.txt', encoding='utf-8') as measurements:
            self.assertEqual(1553, larger_measurement_count(measurements))

    

class PartTwo(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
