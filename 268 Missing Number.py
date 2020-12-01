"""268. Missing Number https://leetcode.com/problems/missing-number/ """

import time
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return list(set(i for i in range(len(nums)+1)) - set(nums))[0]

    def missingNumber1(self, nums: List[int]) -> int:
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().missingNumber([3, 0, 1]))
    print(Solution().missingNumber([0]))

    print("--- %s seconds ---" % (time.time() - start_time))
