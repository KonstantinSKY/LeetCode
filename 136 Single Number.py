"""136. Single Number https://leetcode.com/problems/single-number/ """

import time
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sorted(nums, key=lambda n: nums.count(n))[0]


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().singleNumber([1,2,4, 1,2]))
    print(Solution().singleNumber([2,2,1]))

    print("--- %s seconds ---" % (time.time() - start_time))
