import unittest

from io import StringIO
from main import ok_policy_qtd
from part_1 import is_valid_passwd as validator1
from part_2 import is_valid_passwd as validator2


class PartOne(unittest.TestCase):
    def test_sample_test(self):
        passwords = StringIO('''
        1-3 a: abcde
        1-3 b: cdefg
        2-9 c: ccccccccc
        '''.strip())

        self.assertEqual(2, ok_policy_qtd(passwords, validator1))

    def test_challenge_input(self):
        with open('input.txt', encoding='utf-8') as policies:
            self.assertEqual(600, ok_policy_qtd(policies, validator1))

    def test_no_passwd_is_valid(self):
        passwords = StringIO('''
        1-3 a: aaaaa
        1-3 b: cdefg
        2-9 c: eeeeee
        '''.strip())

        self.assertFalse(ok_policy_qtd(passwords, validator1))


class PartTwo(unittest.TestCase):
    def test_sample_test(self):
        passwords = StringIO('''
        1-3 a: abcde
        1-3 b: cdefg
        2-9 c: ccccccccc
        '''.strip())

        self.assertEqual(1, ok_policy_qtd(passwords, validator2))

    def test_challenge_input(self):
        with open('input.txt', encoding='utf-8') as policies:
            self.assertEqual(245, ok_policy_qtd(policies, validator2))

    def test_no_passwd_is_valid(self):
        passwords = StringIO('''
        1-3 a: aaaaa
        1-3 b: cdefg
        2-9 c: eeeeee
        2-9 d: ffffffffff
        '''.strip())

        self.assertFalse(ok_policy_qtd(passwords, validator2))


if __name__ == '__main__':
    unittest.main()
