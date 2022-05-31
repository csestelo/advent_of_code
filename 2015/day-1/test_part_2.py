from unittest import TestCase

from input import input_2
from part_2 import santa_claus_enters_basement


class TestPart2(TestCase):
    def test_simple_instructions_returns_position_1(self):
        self.assertEqual(1, santa_claus_enters_basement(")"))

    def test_simple_instructions_returns_position_5(self):
        self.assertEqual(5, santa_claus_enters_basement("()())"))

    def test_input_instructions_returns_floor_1771(self):
        self.assertEqual(1771, santa_claus_enters_basement(input_2))
