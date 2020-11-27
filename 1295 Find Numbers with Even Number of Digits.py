"""1295. Find Numbers with Even Number of Digits https://leetcode.com/problems/find-numbers-with-even-number-of-digits/ """

import time
from typing import List


class Solution:
    def findNumbers1(self, nums: List[int]) -> int:
        return sum([1 for i in nums if len(str(i)) % 2 == 0])

    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            k = 0
            while i > 0:
                i //= 10
                k += 1
            if k % 2 == 0:
                res += 1
        return res


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().findNumbers([12, 345, 2, 6, 7896]))

    print("--- %s seconds ---" % (time.time() - start_time))
