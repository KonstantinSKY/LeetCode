"""1351 https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/ """

import time
from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in grid:
            for j in i:
                if j < 0:
                    count += 1
        return count

    def countNegatives2 (self, grid: List[List[int]]) -> int:
        return len([j for i in grid for j in i if j < 0])


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))

    print("--- %s seconds ---" % (time.time() - start_time))
