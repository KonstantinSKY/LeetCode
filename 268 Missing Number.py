"""268. Missing Number https://leetcode.com/problems/missing-number/ """

import time
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return list(set(i for i in range(len(nums)+1)) - set(nums))[0]


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().missingNumber([3, 0, 1]))
    print(Solution().missingNumber([0]))

    print("--- %s seconds ---" % (time.time() - start_time))
