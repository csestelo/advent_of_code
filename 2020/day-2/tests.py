import unittest

from io import StringIO
from part_1 import has_ok_policy_qtd


class PartOne(unittest.TestCase):
    def test_sample_test(self):
        passwords = StringIO('''
        1-3 a: abcde
        1-3 b: cdefg
        2-9 c: ccccccccc
        '''.strip())

        self.assertEqual(2, has_ok_policy_qtd(passwords))

    def test_challenge_input(self):
        with open('input.txt', encoding='utf-8') as policies:
            self.assertEqual(600, has_ok_policy_qtd(policies))

    def test_any_passwd_is_valid(self):
        passwords = StringIO('''
        1-3 a: aaaaa
        1-3 b: cdefg
        2-9 c: eeeeee
        '''.strip())

        self.assertFalse(has_ok_policy_qtd(passwords))


if __name__ == '__main__':
    unittest.main()
