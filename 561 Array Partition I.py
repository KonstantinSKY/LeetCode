"""561. Array Partition I https://leetcode.com/problems/array-partition-i/ """

import time
from typing import List


class Solution:
    def arrayPairSum2(self, nums: List[int]) -> int:
        nums.sort()
        return sum([nums[i] for i in range(0, len(nums), 2)])

    def arrayPairSum1(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(0, len(nums), 2):
            res += nums[i]
        return res

    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().arrayPairSum([6, 2, 6, 5, 1, 2]))
    print(Solution().arrayPairSum([1, 4, 3, 2]))

    print("--- %s seconds ---" % (time.time() - start_time))
