"""414. Third Maximum Number https://leetcode.com/problems/third-maximum-number/ """

import time
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            count += 1
            if count == 3:
                return nums[i]
        return nums[0]

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().thirdMax([2, 2, 3, 1]))

    print("--- %s seconds ---" % (time.time() - start_time))
