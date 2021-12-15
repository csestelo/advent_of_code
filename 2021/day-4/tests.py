import unittest
from io import StringIO

from part_1 import calculate_score
from part_2 import calculate_loser_score


class PartOne(unittest.TestCase):
    pass
    def test_sample_input(self):
        bingo_info = StringIO('''
            7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

            22 13 17 11  0
            8  2 23  4 24
            21  9 14 16  7
            6 10  3 18  5
            1 12 20 15 19

            3 15  0  2 22
            9 18 13 17  5
            19  8  7 25 23
            20 11 10 24  4
            14 21 16 12  6

            14 21 17 24  4
            10 16 15  9 19
            18  8 23 26 20
            22 11 13  6  5
            2  0 12  3  7
        '''.strip())

        self.assertEqual(4512, calculate_score(bingo_info))

    def test_original_input(self):
        with open('2021/day-4/input.txt', encoding='utf-8') as bingo_info:
            self.assertEqual(58374, calculate_score(bingo_info))

    

class PartTwo(unittest.TestCase):
    def test_sample_input(self):
        bingo_info = StringIO('''
            7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

            22 13 17 11  0
            8  2 23  4 24
            21  9 14 16  7
            6 10  3 18  5
            1 12 20 15 19

            3 15  0  2 22
            9 18 13 17  5
            19  8  7 25 23
            20 11 10 24  4
            14 21 16 12  6

            14 21 17 24  4
            10 16 15  9 19
            18  8 23 26 20
            22 11 13  6  5
            2  0 12  3  7
        '''.strip())

        self.assertEqual(1924, calculate_loser_score(bingo_info))

    def test_original_input(self):
        with open('2021/day-4/input.txt', encoding='utf-8') as bingo_info:
            self.assertEqual(11377, calculate_loser_score(bingo_info))



if __name__ == '__main__':
    unittest.main()
