from unittest import TestCase

from input import input_1
from part_1 import santa_claus_floor


class TestPart1(TestCase):
    def test_simple_instructions_returns_floor_0(self):
        inputs = ["(())", "()()"]

        for i in inputs:
            self.assertEqual(0, santa_claus_floor(i))

    def test_simple_instructions_returns_floor_3(self):
        inputs = ["(((", "(()(()(", "))((((("]

        for i in inputs:
            self.assertEqual(3, santa_claus_floor(i))

    def test_simple_instructions_returns_floor_minus_1(self):
        inputs = ["())", "))("]

        for i in inputs:
            self.assertEqual(-1, santa_claus_floor(i))

    def test_simple_instructions_returns_floor_minus_3(self):
        inputs = [")))", ")())())"]

        for i in inputs:
            self.assertEqual(-3, santa_claus_floor(i))

    def test_input_instructions_returns_floor_138(self):
        self.assertEqual(138, santa_claus_floor(input_1))
