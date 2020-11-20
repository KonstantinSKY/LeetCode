""" 961 https://leetcode.com/problems/n-repeated-element-in-size-2n-array/"""

import time
from typing import List


class Solution:
    def repeatedNTimes2(self, A: List[int]) -> int:
        for num in A:
            if A.count(num) == len(A) / 2:
                return num

    def repeatedNTimes(self, A: List[int]) -> int:
        new = []
        for num in A:
            if num not in new:
                new.append(num)
            else:
                return num

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]))

    print("--- %s seconds ---" % (time.time() - start_time))
