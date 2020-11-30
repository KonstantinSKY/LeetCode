"""136. Single Number https://leetcode.com/problems/single-number/ """

import time
from typing import List

class Solution:
    def singleNumber2(self, nums: List[int]) -> int:
        return sorted(nums, key=lambda n: nums.count(n))[0]

    def singleNumber3(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums)-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]

    def singleNumber(self, nums: List[int]) -> int:
        while True:
            if nums[0] in nums[1:]:
                del nums[nums.index(nums[0], 1)]
                del nums[0]
            else:
                return nums[0]


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().singleNumber([1,2,4, 1,2]))
    # print(Solution().singleNumber([2,2,1]))
    # print(Solution().singleNumber([4, 1, 2, 1, 2]))

    print("--- %s seconds ---" % (time.time() - start_time))
