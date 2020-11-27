"""1295. Find Numbers with Even Number of Digits https://leetcode.com/problems/find-numbers-with-even-number-of-digits/ """

import time
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([1 for i in nums if len(str(i)) % 2 == 0])


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().findNumbers([12, 345, 2, 6, 7896]))

    print("--- %s seconds ---" % (time.time() - start_time))
