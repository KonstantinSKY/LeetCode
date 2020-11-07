import unittest
from palindrome_number import Solution


class DatabasesTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution(121), True)

    def test_example2(self):
        self.assertEqual(self.solution(-121), False)

    def test_example3(self):
        self.assertEqual(self.solution(10), False)

    def test_example4(self):
        self.assertEqual(self.solution(-101), False)

    def test_example5(self):
        self.assertEqual(self.solution(1001), True)

    def test_example6(self):
        self.assertEqual(self.solution(34433443), True)

    def test_example7(self):
        self.assertEqual(self.solution(3434435), True)

    def test_example8(self):
        self.assertEqual(self.solution(101001010), True)

    def test_example9(self):
        self.assertEqual(self.solution(54645433), False)


if __name__ == '__main__':
    unittest.main()