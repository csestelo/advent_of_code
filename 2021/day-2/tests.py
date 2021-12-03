import unittest
from io import StringIO

from part_1 import calculate_position
from part_2 import calculate_position_as_in_manual


class PartOne(unittest.TestCase):
    def test_sample_input(self):
        instructions = StringIO('''
            forward 5
            down 5
            forward 8
            up 3
            down 8
            forward 2
        '''.strip())

        self.assertEqual(150, calculate_position(instructions))

    def test_original_input(self):
        with open('2021/day-2/input.txt', encoding='utf-8') as instructions:
            self.assertEqual(1524750, calculate_position(instructions))

    

class PartTwo(unittest.TestCase):
    def test_sample_input(self):
        instructions = StringIO('''
            forward 5
            down 5
            forward 8
            up 3
            down 8
            forward 2
        '''.strip())

        self.assertEqual(900, calculate_position_as_in_manual(instructions))

    def test_original_input(self):
        with open('2021/day-2/input.txt', encoding='utf-8') as instructions:
            self.assertEqual(1592426537, calculate_position_as_in_manual(instructions))


if __name__ == '__main__':
    unittest.main()
