import os
import sys
import unittest
sys.path.append(os.pardir)
from  import Solution


class PalindromeNumberTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.romanToInt("III"), 3)

    def test_example2(self):
        self.assertEqual(self.solution.romanToInt("IV"), 4)

    def test_example3(self):
        self.assertEqual(self.solution.romanToInt("IX"), 9)

    def test_example4(self):
        self.assertEqual(self.solution.romanToInt("LVIII"), 58)

    def test_example5(self):
        self.assertEqual(self.solution.romanToInt("MCMXCIV"), 1994)

    def test_example6(self):
        self.assertEqual(self.solution.romanToInt("VII"), 7)

    def test_example7(self):
        self.assertEqual(self.solution.romanToInt("X"), 10)

    def test_example8(self):
        self.assertEqual(self.solution.romanToInt("XIV"), 14)

    def test_example9(self):
        self.assertEqual(self.solution.romanToInt("CXIV"), 114)


if __name__ == '__main__':
    unittest.main()
