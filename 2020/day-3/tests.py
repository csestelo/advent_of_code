import unittest
from io import StringIO
from part_1 import count_trees


class PartOne(unittest.TestCase):
    def test_simple_scenario(self):
        input_sample = StringIO("""
            ..##.......
            #...#...#..
            .#....#..#.
        """.strip())

        self.assertEqual(1, count_trees(input_sample))

    def test_sample_scenario(self):
        input_sample = StringIO("""
            ..##.......
            #...#...#..
            .#....#..#.
            ..#.#...#.#
            .#...##..#.
            ..#.##.....
            .#.#.#....#
            .#........#
            #.##...#...
            #...##....#
            .#..#...#.#
        """.strip())

        self.assertEqual(7, count_trees(input_sample))

    def test_challenge_input(self):
        with open('input.txt', encoding='utf-8') as file:
            self.assertEqual(178, count_trees(file))


class PartTwo(unittest.TestCase):
    def test_sample_test(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
