""" 665. Non-decreasing Array https://leetcode.com/problems/non-decreasing-array/"""

import time
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        res = True
        i = 0
        while i <= len(nums)-1:
            if nums[i] > nums[i+1] and nums[i + 1] - nums[i] > 2:

        # return sum([1 for i in range(1, len(nums)) if nums[i] < nums[i - 1]]) < 2
        res = 0
        for i in range(len(nums), -1):
            if nums[i - 1] < nums[i]:
            if nums[i - 1] < nums[i] and nums[i+1]-nums[i] > 2:
                res += 1
        return res < 2


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().checkPossibility([4, 2, 3]))
    print(Solution().checkPossibility([4, 2, 1]))
    print(Solution().checkPossibility([3, 4, 2, 3]))

    print("--- %s seconds ---" % (time.time() - start_time))
