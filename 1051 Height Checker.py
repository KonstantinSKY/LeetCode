"""1051. Height Checker https://leetcode.com/problems/height-checker/ """

import time
from typing import List


class Solution:
    def heightChecker2(self, heights: List[int]) -> int:
        new_arr = sorted(heights)
        return sum([1 for i in range(len(heights)) if heights[i] != new_arr[i]])

    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        for i, j in zip(heights, sorted(heights)):
            if i != j:
                res += 1
        return res

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().heightChecker([1, 1, 4, 2, 1, 3]))

    print("--- %s seconds ---" % (time.time() - start_time))
