"""https://leetcode.com/problems/number-of-good-pairs/ """

import time
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        for i, num in enumerate(nums):
            pairs += nums[i + 1:].count(num)
        return pairs


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]))
    print(Solution().numIdenticalPairs([1, 1, 1, 1]))
    print(Solution().numIdenticalPairs([1, 2, 3]))

    print("--- %s seconds ---" % (time.time() - start_time))
