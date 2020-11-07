import os
import sys
import unittest
sys.path.append(os.pardir)
from palindrome_number import Solution


class PalindromeNumberTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.isPalindrome(121), True)

    def test_example2(self):
        self.assertEqual(self.solution.isPalindrome(-121), False)

    def test_example3(self):
        self.assertEqual(self.solution.isPalindrome(10), False)

    def test_example4(self):
        self.assertEqual(self.solution.isPalindrome(-101), False)

    def test_example5(self):
        self.assertEqual(self.solution.isPalindrome(1001), True)

    def test_example6(self):
        self.assertEqual(self.solution.isPalindrome(34433443), True)

    def test_example7(self):
        self.assertEqual(self.solution.isPalindrome(3434435), False)

    def test_example8(self):
        self.assertEqual(self.solution.isPalindrome(101001010), False)

    def test_example9(self):
        self.assertEqual(self.solution.isPalindrome(54645433), False)


if __name__ == '__main__':
    unittest.main()
