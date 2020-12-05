"""977 Squares of a Sorted Array  https://leetcode.com/problems/squares-of-a-sorted-array/"""

import time
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num * num for num in nums])



        
if __name__ == "__main__":
    start_time = time.time()
    print(Solution().sortedSquares([-4, -1, 0, 3, 10]))

    print("--- %s seconds ---" % (time.time() - start_time))
