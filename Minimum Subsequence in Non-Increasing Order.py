"""1403 https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/ """

import time
from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        i = 1
        while sum(nums[:i]) <= sum(nums[i:]):
            i += 1
        return nums[:i]


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().minSubsequence([4, 3, 10, 9, 8]))
    print(Solution().minSubsequence([4, 4, 7, 6, 7]))

    print(Solution().minSubsequence([8, 8]))
    print("--- %s seconds ---" % (time.time() - start_time))
